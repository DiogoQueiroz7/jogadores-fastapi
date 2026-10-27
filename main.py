from fastapi import FastAPI
from pydantic import BaseModel


class JogadorEntrada(BaseModel):
    nome: str
    posicao: str


class JogadorSaida(JogadorEntrada):
    id: int


app = FastAPI()


jogadores = [
    {"id": 1, "nome": "Carlos Miguel", "posicao": "goleiro"},
    {"id": 2, "nome": "Gustavo Gomez", "posicao": "zagueiro"},
    {"id": 3, "nome": "Andreas Pereira", "posicao": "meia"},
    {"id": 4, "nome": "Flaco Lopez", "posicao": "atacante"},
]


@app.get("/jogadores/")
def listar_jogadores(posicao: str | None = None) -> list[JogadorSaida]:
    if posicao is None:
        return jogadores
    resultado = []
    for j in jogadores:
        if j["posicao"].lower() == posicao.lower():
            resultado.append(j)
    return resultado


@app.get("/jogadores/{jogador_id}")
def ver_jogador(jogador_id: int) -> JogadorSaida | None:
    for j in jogadores:
        if j["id"] == jogador_id:
            return j
    return None


@app.post("/jogadores/")
def criar_jogador(jogador: JogadorEntrada) -> JogadorSaida:
    novo_id = 1
    for j in jogadores:
        if j["id"] >= novo_id:
            novo_id = j["id"] + 1

    novo = {"id": novo_id, "nome": jogador.nome, "posicao": jogador.posicao.lower()}
    jogadores.append(novo)
    return novo


@app.put("/jogadores/{jogador_id}")
def atualizar_jogador(jogador_id: int, jogador: JogadorEntrada) -> JogadorSaida | None:
    for j in jogadores:
        if j["id"] == jogador_id:
            j["nome"] = jogador.nome
            j["posicao"] = jogador.posicao.lower()
            return j
    return None


@app.delete("/jogadores/{jogador_id}")
def remover_jogador(jogador_id: int) -> JogadorSaida | None:
    for j in jogadores:
        if j["id"] == jogador_id:
            jogadores.remove(j)
            return j
    return None
