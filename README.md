📚 API REST da Biblioteca
Esta é uma API REST simples desenvolvida em Python com o framework Flask para gerenciar recursos do tipo Livro. Ela foi criada como parte de um exercício para demonstrar o uso de endpoints RESTful (GET e POST) e a manipulação de diferentes formatos de serialização de dados, como JSON e XML, com base no cabeçalho Accept.

Nota: Esta é uma API in-memory (os dados não são persistidos em um banco de dados). Os livros são perdidos quando o servidor é reiniciado.

🚀 Como Rodar a API
Para executar este projeto, você precisará ter o Python 3 instalado.

1. Configurar o Ambiente Virtual
Recomendamos o uso de um ambiente virtual (venv) para isolar as dependências do projeto.

# 1. Crie o ambiente virtual
python -m venv venv

# 2. Ative o ambiente virtual
# No Windows PowerShell:
.\venv\Scripts\Activate
# No Linux/macOS ou Git Bash:
source venv/bin/activate

2. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias (Flask para o servidor e xmltodict para a serialização XML):

pip install Flask xmltodict

3. Executar o Servidor
Execute o arquivo principal da aplicação:

python app.py

O servidor estará disponível em: http://127.0.0.1:5000/

🗺️ Endpoints da API
O recurso principal da API é o Livro, que possui os campos id, titulo, autor e ano.

1. Boas-Vindas (Root)
Método

URI

Descrição

GET

/

Mensagem de boas-vindas e instruções.

Exemplo de Resposta (JSON):

{
    "mensagem": "Bem-vindo(a) à API REST da Biblioteca!",
    "instrucoes": "Acesse /livros para listar ou adicionar livros."
}

2. Gerenciar Livros (Lista)
Este endpoint suporta a leitura e a criação de livros.

GET /livros
Retorna a lista completa de livros. O formato da resposta depende do cabeçalho Accept enviado na requisição.

Cabeçalho Accept

Formato Retornado

application/json (Padrão)

JSON

application/xml

XML

Exemplo de Teste (HTTPie para XML):

http GET [http://127.0.0.1:5000/livros](http://127.0.0.1:5000/livros) Accept:application/xml

POST /livros
Adiciona um novo livro à coleção. Espera o envio de um objeto JSON.

Exemplo de Corpo da Requisição (JSON):

{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899
}

Exemplo de Teste (HTTPie):

http POST [http://127.0.0.1:5000/livros](http://127.0.0.1:5000/livros) titulo="Dom Casmurro" autor="Machado de Assis" ano:=1899

Observação: O uso de := garante que o valor de ano seja enviado como um número inteiro (integer).

📊 Comparação de Formatos (JSON vs. XML)
Este projeto demonstra a diferença entre os formatos de serialização. Abaixo estão as conclusões da análise:

Característica

JSON

XML

Legibilidade Humana

Alta (Mais legível)

Baixa (Muito verboso)

Tamanho do Arquivo

Compacto e leve

Grande (Devido à repetição de tags)

Preferencia Corporativa

Padrão atual para APIs REST modernas.

Preferido historicamente (e em sistemas legados) devido ao suporte nativo a XSD (Schema Definition), que garante uma validação de dados mais rigorosa.
