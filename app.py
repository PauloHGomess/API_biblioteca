from flask import Flask, request, jsonify, make_response
import xmltodict
import json
import uuid 

app = Flask(__name__)

# Simulação do "banco de dados"
livros = {
    "1": {"id": "1", "titulo": "1984", "autor": "George Orwell", "ano": 1949},
    "2": {"id": "2", "titulo": "Admirável Mundo Novo", "autor": "Aldous Huxley", "ano": 1932},
}

# Variável para rastrear o próximo ID sequencial
next_id_int = 3

# Função auxiliar para converter a lista de livros para XML
def lista_para_xml(lista_de_livros):
    """
    Converte uma lista de dicionários Python (livros) para uma string XML bem formada.
    Garante que há uma única chave raiz ('livros') para evitar erros.
    """
    root = {"livros": {"livro": lista_de_livros}}
    xml_string = xmltodict.unparse(root, pretty=True, full_document=True)
    return xml_string

# --- NOVA ROTA DE BOAS-VINDAS (HOME) ---
@app.route('/', methods=['GET'])
def home():
    """Retorna uma mensagem de boas-vindas e instrui sobre o uso da API."""
    return jsonify({
        "mensagem": "Bem-vindo(a) à API REST da Biblioteca!",
        "instrucoes": "Acesse /livros para listar ou adicionar livros.",
        "endpoints_disponiveis": {
            "GET /livros": "Lista todos os livros (JSON ou XML via Accept Header)",
            "POST /livros": "Adiciona um novo livro (enviar JSON no corpo da requisição)"
        }
    }), 200

# Rota 1: GET /livros -> Retorna todos os livros em JSON ou XML
@app.route('/livros', methods=['GET'])
def get_livros():
    # Converte o dicionário de livros em uma lista de valores para serialização
    lista_de_livros = list(livros.values())
    
    # Verifica o cabeçalho Accept
    accept_header = request.headers.get('Accept', 'application/json')

    if 'application/xml' in accept_header:
        # Responde em XML
        xml_data = lista_para_xml(lista_de_livros)
        response = make_response(xml_data, 200)
        response.headers['Content-Type'] = 'application/xml'
        return response
    else:
        # Responde em JSON (padrão)
        return jsonify(lista_de_livros), 200

# Rota 2: POST /livros -> Recebe dados em JSON e adiciona um novo livro
@app.route('/livros', methods=['POST'])
def add_livro():
    global next_id_int

    if not request.is_json:
        return jsonify({"erro": "Requisição deve ser em JSON."}), 400

    novo_livro = request.get_json()

    # Validação dos campos obrigatórios
    if not all(k in novo_livro for k in ("titulo", "autor", "ano")):
        return jsonify({"erro": "Campos 'titulo', 'autor' e 'ano' são obrigatórios."}), 400

    # Cria o novo ID e o livro completo
    novo_id = str(next_id_int)
    
    livro_completo = {
        "id": novo_id,
        "titulo": novo_livro["titulo"],
        "autor": novo_livro["autor"],
        "ano": novo_livro["ano"],
    }
    
    # Adiciona o livro ao "banco de dados" e incrementa o ID
    livros[novo_id] = livro_completo
    next_id_int += 1

    # Retorna o livro recém-criado com status 201 Created
    return jsonify(livro_completo), 201

if __name__ == '__main__':
    # Roda a aplicação na porta 5000
    app.run(debug=True)
