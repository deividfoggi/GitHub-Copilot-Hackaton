"""Lógica de negócio do sistema de Boletim de Ocorrência.

Este é o coração do sistema: a partir da descrição livre informada pelo
cidadão, classificamos o tipo da ocorrência e geramos o boletim estruturado.

A classificação é feita por palavras-chave (regras simples). Não há
inteligência artificial aqui — essa é justamente a oportunidade de evolução
do sistema durante o workshop.
"""

from app.models import BoletimOcorrencia, Ocorrencia

# Tipo atribuído quando nenhuma palavra-chave é encontrada na descrição.
TIPO_PADRAO = "Outros"

# Mapeia cada tipo de ocorrência às palavras-chave que o identificam.
# A ordem importa: o primeiro tipo com palavra-chave encontrada é escolhido.
PALAVRAS_CHAVE = {
    "Furto": ["furto", "furtaram", "subtraiu", "levaram sem"],
    "Roubo": ["roubo", "assalto", "assaltaram", "arma", "ameaça", "rendido"],
    "Acidente de Trânsito": ["acidente", "colisão", "batida", "atropelamento", "veículo"],
    "Perturbação do Sossego": ["barulho", "som alto", "festa", "perturbação", "sossego"],
    "Dano ao Patrimônio": ["vandalismo", "depredação", "pichação", "quebraram", "dano"],
    "Desaparecimento": ["desaparecido", "desaparecimento", "sumiu", "não voltou"],
}


def classificar_tipo(descricao: str) -> str:
    """Classifica o tipo da ocorrência a partir da descrição livre.

    Percorre as palavras-chave de cada tipo e retorna o primeiro tipo cuja
    palavra-chave aparecer na descrição. Caso nenhuma seja encontrada,
    retorna o tipo padrão.
    """
    descricao_normalizada = descricao.lower()
    for tipo, palavras in PALAVRAS_CHAVE.items():
        for palavra in palavras:
            if palavra in descricao_normalizada:
                return tipo
    return TIPO_PADRAO


def gerar_numero_bo(total_existente: int) -> str:
    """Gera o número sequencial do boletim, ex.: BO-2026-0001."""
    from datetime import datetime

    ano = datetime.now().year
    sequencial = total_existente + 1
    return f"BO-{ano}-{sequencial:04d}"


def montar_boletim(ocorrencia: Ocorrencia, total_existente: int) -> BoletimOcorrencia:
    """Monta o boletim estruturado a partir dos dados da ocorrência.

    Aplica a classificação automática do tipo e gera o número do boletim.
    """
    tipo = classificar_tipo(ocorrencia.descricao)
    numero_bo = gerar_numero_bo(total_existente)
    return BoletimOcorrencia(
        numero_bo=numero_bo,
        solicitante=ocorrencia.solicitante,
        data_hora=ocorrencia.data_hora,
        local=ocorrencia.local,
        tipo=tipo,
        descricao=ocorrencia.descricao,
    )
