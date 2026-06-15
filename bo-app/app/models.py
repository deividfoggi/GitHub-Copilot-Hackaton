"""Modelos de dados do sistema de Boletim de Ocorrência (BO).

Define as estruturas de entrada (dados informados no formulário) e de saída
(o boletim já estruturado e classificado pelo sistema).
"""

from datetime import datetime

from pydantic import BaseModel, Field


class Ocorrencia(BaseModel):
    """Dados informados pelo cidadão no formulário de registro."""

    solicitante: str = Field(..., description="Nome de quem está registrando a ocorrência")
    data_hora: str = Field(..., description="Data e hora em que o fato ocorreu")
    local: str = Field(..., description="Endereço ou local onde o fato ocorreu")
    descricao: str = Field(..., description="Descrição livre do que aconteceu")


class BoletimOcorrencia(BaseModel):
    """Boletim de Ocorrência já estruturado e classificado pelo sistema."""

    numero_bo: str = Field(..., description="Número único do boletim, ex.: BO-2026-0001")
    solicitante: str
    data_hora: str
    local: str
    tipo: str = Field(..., description="Tipo da ocorrência, classificado automaticamente")
    descricao: str
    data_registro: str = Field(
        default_factory=lambda: datetime.now().strftime("%d/%m/%Y %H:%M"),
        description="Data e hora em que o boletim foi registrado no sistema",
    )
