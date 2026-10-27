# jogadores-fastapi

Atividade da matéria do professor Rogério, onde fiz uma API usando FastAPI para cadastrar jogadores do Palmeiras.

Os jogadores ficam salvos em uma lista no próprio codigo, sem banco... então ao atualizar, voltam para os 4 principais

Integrantes

- Diogo Queiroz

## Como rodar

Primeiro precisa ter o Python instalado.

1- Clonar o projeto: git clone https://github.com/DiogoQueiroz7/jogadores-fastapi.git
2- Entrar na pasta: cd jogadores-fastapi
3- Criar o ambiente virtual: python -m venv .venv
4- Ativar o ambiente virtual:
   - Windows: .venv\Scripts\activate
   - Linux/Mac: source .venv/bin/activate
5- Instalar as dependências: pip install -r requirements.txt
6- Rodar a API: fastapi dev main.py

Depois é só acessar http://127.0.0.1:8000/docs para testar as rotas pelo Swagger.

## Rotas

- GET /jogadores/ - Lista os jogadores.
- GET /jogadores/{jogador_id} - Busca um jogador pelo ID.
- POST /jogadores/ - Cadastra um jogador.
- PUT /jogadores/{jogador_id} - Edita um jogador.
- DELETE /jogadores/{jogador_id} - Exclui um jogador.

Também dá pra filtrar pela posição, tipo: /jogadores/?posicao=goleiro


