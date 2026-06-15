"""Esqueleto do agente inteligente de Boletim de Ocorrência (Microsoft Foundry).

Este arquivo é o ponto de partida da Etapa 3 do workshop. O objetivo é criar um
agente no **Azure AI Foundry Agent Service** que conversa com o usuário em
linguagem natural e usa as ferramentas de `ferramentas.py` para registrar e
consultar boletins no sistema existente.

O código abaixo segue o "happy path" do SDK `azure-ai-projects` /
`azure-ai-agents`. Procure pelos comentários `TODO` — são os pontos que você
vai completar (com a ajuda do GitHub Copilot!) durante o workshop.

Antes de rodar:
1. Tenha um projeto no Foundry e um modelo implantado (ex.: gpt-4o-mini).
2. Copie `.env.example` para `.env` e preencha FOUNDRY_PROJECT_ENDPOINT.
3. Autentique-se com `az login`.
4. Deixe o app rodando em outro terminal (uvicorn app.main:app --reload).
"""

import os

from azure.ai.agents.models import FunctionTool, ListSortOrder, ToolSet
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

from ferramentas import consultar_boletim, consultar_historico, gerar_bo

# Endpoint do projeto Foundry e modelo implantado (configurados no .env).
PROJECT_ENDPOINT = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
MODEL_DEPLOYMENT = os.getenv("FOUNDRY_MODEL_DEPLOYMENT", "gpt-4o-mini")

# Instruções do agente: definem a personalidade e o comportamento esperado.
# TODO (Etapa 3): refine estas instruções para o agente extrair os dados da
# conversa e classificar melhor as ocorrências.
INSTRUCOES_AGENTE = """
Você é um atendente virtual de uma central de Boletins de Ocorrência.
Converse de forma educada e objetiva. A partir do relato do cidadão,
identifique os dados necessários (solicitante, data e hora, local e descrição)
e registre o boletim usando a ferramenta disponível. Se faltar alguma
informação, pergunte antes de registrar. Ao final, informe o número do
boletim gerado e o tipo classificado.
""".strip()


def criar_agente(project_client: AIProjectClient):
    """Cria o agente com as ferramentas (tools) disponíveis."""
    # Registra as funções de ferramentas.py como ferramentas do agente.
    funcoes = FunctionTool(functions={gerar_bo, consultar_historico, consultar_boletim})
    toolset = ToolSet()
    toolset.add(funcoes)

    # Habilita a execução automática das funções pelo SDK.
    project_client.agents.enable_auto_function_calls(toolset)

    agente = project_client.agents.create_agent(
        model=MODEL_DEPLOYMENT,
        name="agente-bo",
        instructions=INSTRUCOES_AGENTE,
        toolset=toolset,
    )
    return agente


def conversar(project_client: AIProjectClient, agente, mensagem_usuario: str) -> str:
    """Envia uma mensagem ao agente e retorna a resposta final."""
    # Cria uma thread (conversa) e adiciona a mensagem do usuário.
    thread = project_client.agents.threads.create()
    project_client.agents.messages.create(
        thread_id=thread.id, role="user", content=mensagem_usuario
    )

    # Executa o agente — o SDK chama as ferramentas automaticamente.
    run = project_client.agents.runs.create_and_process(
        thread_id=thread.id, agent_id=agente.id
    )
    if run.status == "failed":
        return f"A execução falhou: {run.last_error}"

    # Recupera a última mensagem do agente.
    mensagens = project_client.agents.messages.list(
        thread_id=thread.id, order=ListSortOrder.ASCENDING
    )
    resposta = ""
    for mensagem in mensagens:
        if mensagem.role == "assistant" and mensagem.text_messages:
            resposta = mensagem.text_messages[-1].text.value
    return resposta


def main():
    """Fluxo simples de demonstração do agente."""
    if not PROJECT_ENDPOINT:
        raise SystemExit(
            "Defina FOUNDRY_PROJECT_ENDPOINT no arquivo .env antes de rodar o agente."
        )

    project_client = AIProjectClient(
        endpoint=PROJECT_ENDPOINT, credential=DefaultAzureCredential()
    )

    with project_client:
        agente = criar_agente(project_client)
        print(f"Agente criado: {agente.id}\n")

        # TODO (Etapa 4): troque por um loop de conversa interativo (input()).
        relato = (
            "Meu nome é Carla Dias. Hoje, 15/06/2026 às 08:00, na Rua das "
            "Flores 123, minha bicicleta foi furtada da garagem."
        )
        print(f"Usuário: {relato}\n")
        resposta = conversar(project_client, agente, relato)
        print(f"Agente: {resposta}\n")

        # Limpeza: remove o agente criado para a demonstração.
        project_client.agents.delete_agent(agente.id)


if __name__ == "__main__":
    main()
