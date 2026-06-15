"""Ferramentas (tools) que o agente Foundry pode usar.

Cada função aqui é um wrapper sobre a API do app de Boletim de Ocorrência.
O agente não fala diretamente com o sistema: ele chama estas ferramentas, que
por sua vez chamam os endpoints /api do app.

Mantenha as funções simples e bem descritas — o agente usa o nome, os
parâmetros e a docstring para decidir quando chamá-las.
"""

import os

import requests

# URL base do app. Configurável via variável de ambiente BO_API_URL.
BO_API_URL = os.getenv("BO_API_URL", "http://localhost:8000")


def gerar_bo(solicitante: str, data_hora: str, local: str, descricao: str) -> dict:
    """Registra um novo Boletim de Ocorrência no sistema.

    Use esta ferramenta quando o usuário descrever um fato que precisa ser
    registrado como boletim. O sistema classifica o tipo automaticamente.

    Parâmetros:
        solicitante: nome de quem está registrando a ocorrência.
        data_hora: data e hora em que o fato ocorreu (ex.: "14/06/2026 22:30").
        local: endereço ou local onde o fato ocorreu.
        descricao: descrição livre do que aconteceu.

    Retorna o boletim gerado, incluindo o número e o tipo classificado.
    """
    resposta = requests.post(
        f"{BO_API_URL}/api/boletins",
        json={
            "solicitante": solicitante,
            "data_hora": data_hora,
            "local": local,
            "descricao": descricao,
        },
        timeout=10,
    )
    resposta.raise_for_status()
    return resposta.json()


def consultar_historico() -> list[dict]:
    """Consulta o histórico de Boletins de Ocorrência já registrados.

    Use esta ferramenta quando o usuário quiser saber sobre boletins
    anteriores, estatísticas ou ocorrências parecidas.

    Retorna a lista de boletins registrados.
    """
    resposta = requests.get(f"{BO_API_URL}/api/boletins", timeout=10)
    resposta.raise_for_status()
    return resposta.json()


def consultar_boletim(numero_bo: str) -> dict | None:
    """Consulta os detalhes de um boletim específico pelo seu número.

    Parâmetros:
        numero_bo: número do boletim, ex.: "BO-2026-0001".

    Retorna o boletim encontrado ou None.
    """
    resposta = requests.get(f"{BO_API_URL}/api/boletins/{numero_bo}", timeout=10)
    resposta.raise_for_status()
    return resposta.json()
