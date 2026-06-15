# Agente Inteligente de Boletim de Ocorrência (Microsoft Foundry)

Esta é a pasta onde **você vai construir**, do zero e com a ajuda do GitHub
Copilot, o agente das Etapas 3 e 4 do workshop. O agente conversa em linguagem
natural e usa o app de Boletim de Ocorrência como ferramenta — registrando e
consultando boletins pela API.

```
[ Usuário ] → [ Agente Foundry ] → [ ferramentas ] → [ API do app /api ]
```

## O que você vai criar

| Arquivo | Você cria na | Descrição |
|---------|--------------|-----------|
| `ferramentas.py` | Etapa 3 | Ferramentas (tools) que chamam a API do app |
| `agente_bo.py` | Etapas 3 e 4 | O agente Foundry e o loop de conversa |

> Estes arquivos **não vêm prontos** de propósito. Construí-los com o Copilot é o
> objetivo do workshop. Siga o passo a passo em
> [`workshop/fase3-agente.md`](../workshop/fase3-agente.md) e
> [`workshop/fase4-integracao.md`](../workshop/fase4-integracao.md).

O `requirements.txt` já lista as dependências necessárias para te ajudar no setup.

## Pré-requisitos

1. **Projeto no Microsoft Foundry** com um modelo implantado (ex.: `gpt-4o-mini`).
2. **Azure CLI** autenticado: `az login`.
3. O **app rodando** em outro terminal:
   ```bash
   uvicorn app.main:app --reload
   ```

## Setup do ambiente

> **Importante:** use o **mesmo ambiente virtual** (`bo-app/.venv`) criado
> nas etapas anteriores. Se você abriu um terminal novo, ative-o antes de
> instalar. Sem o venv ativo, o `pip` usa o Python do sistema e falha com
> `externally-managed-environment` (PEP 668) no macOS/Linux.

```bash
# 1. A partir da pasta bo-app/, ative o ambiente virtual
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Entre na pasta do agente
cd agente

# 3. Instale as dependências do agente
pip install -r requirements.txt

# 4. Copie o .env de exemplo e preencha os valores do Foundry
cp ../.env.example ../.env
#   FOUNDRY_PROJECT_ENDPOINT=https://<seu-projeto>.services.ai.azure.com/api/projects/<projeto>
#   FOUNDRY_MODEL_DEPLOYMENT=gpt-4o-mini
```

> Se ainda não criou o `.venv`, crie a partir de `bo-app/`:
> `python3 -m venv .venv && source .venv/bin/activate`.

> Dica: use o GitHub Copilot para descobrir o SDK e gerar o código.
> Se o setup do Foundry estiver disponível, o facilitador pode usar a skill
> **microsoft-foundry** para criar o projeto e implantar o modelo.
