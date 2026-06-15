# Agente Inteligente de Boletim de Ocorrência (Microsoft Foundry)

Esta pasta contém o **esqueleto** do agente que você vai construir na Etapa 3 do
workshop. O agente conversa em linguagem natural e usa o app de Boletim de
Ocorrência como ferramenta — registrando e consultando boletins pela API.

```
[ Usuário ] → [ Agente Foundry ] → [ ferramentas.py ] → [ API do app /api ]
```

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `ferramentas.py` | Ferramentas (tools) que chamam a API do app |
| `agente_bo.py` | Esqueleto do agente Foundry com `TODO`s a completar |
| `requirements.txt` | Dependências do agente |

## Pré-requisitos

1. **Projeto no Microsoft Foundry** com um modelo implantado (ex.: `gpt-4o-mini`).
2. **Azure CLI** autenticado: `az login`.
3. O **app rodando** em outro terminal:
   ```bash
   uvicorn app.main:app --reload
   ```

## Passo a passo (happy path)

```bash
# 1. A partir da pasta bo-app/, entre na pasta do agente
cd agente

# 2. Instale as dependências do agente
pip install -r requirements.txt

# 3. Copie o .env de exemplo e preencha os valores do Foundry
cp ../.env.example ../.env
#   FOUNDRY_PROJECT_ENDPOINT=https://<seu-projeto>.services.ai.azure.com/api/projects/<projeto>
#   FOUNDRY_MODEL_DEPLOYMENT=gpt-4o-mini

# 4. Rode o agente
python agente_bo.py
```

## O que completar (Etapas 3 e 4)

Procure pelos comentários `TODO` em `agente_bo.py`:

- **Etapa 3** — Refinar as instruções do agente para extrair os dados da
  conversa e registrar o boletim corretamente.
- **Etapa 4** — Transformar a demonstração em um loop de conversa interativo e
  conectar o agente ao fluxo do sistema.

> Dica: use o GitHub Copilot para completar os `TODO`s e entender o SDK.
> Se o setup do Foundry estiver disponível, o facilitador pode usar a skill
> **microsoft-foundry** para criar o projeto e implantar o modelo.
