"""Persistência dos boletins em arquivo JSON.

Mantém os boletins registrados em `dados/boletins.json`. É um repositório
simples, propositalmente fácil de inspecionar e entender durante o workshop.
"""

import json
from pathlib import Path

from app.models import BoletimOcorrencia

# Caminho do arquivo JSON onde os boletins são armazenados.
CAMINHO_DADOS = Path(__file__).resolve().parent.parent / "dados" / "boletins.json"


def carregar_boletins() -> list[dict]:
    """Carrega todos os boletins do arquivo JSON.

    Retorna uma lista vazia caso o arquivo ainda não exista.
    """
    if not CAMINHO_DADOS.exists():
        return []
    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_boletim(boletim: BoletimOcorrencia) -> None:
    """Adiciona um novo boletim ao arquivo JSON."""
    boletins = carregar_boletins()
    boletins.append(boletim.model_dump())
    CAMINHO_DADOS.parent.mkdir(parents=True, exist_ok=True)
    with open(CAMINHO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(boletins, arquivo, ensure_ascii=False, indent=2)


def buscar_por_numero(numero_bo: str) -> dict | None:
    """Busca um boletim específico pelo seu número."""
    for boletim in carregar_boletins():
        if boletim.get("numero_bo") == numero_bo:
            return boletim
    return None


def contar_boletins() -> int:
    """Retorna a quantidade de boletins registrados."""
    return len(carregar_boletins())
