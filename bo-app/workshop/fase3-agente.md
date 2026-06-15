# Etapa 3 — Introdução ao agente com o Microsoft Foundry

**Objetivo:** entender o que é um **agente** e criar o primeiro agente no
**Microsoft Foundry** que conversa em linguagem natural sobre ocorrências.

**Tempo sugerido:** ~40 min.

## De regras para inteligência

Nas Etapas 1 e 2 o sistema decidia tudo por **regras fixas** (palavras-chave,
mapeamentos). Funciona, mas é rígido: não entende sinônimos, contexto ou relatos
ambíguos.

Um **agente** é diferente: ele usa um **modelo de linguagem** para **raciocinar**
sobre o pedido e decidir **quais ações tomar** — chamando **ferramentas (tools)**
quando precisa agir no mundo real.

> Aqui está a virada de chave do workshop:
> **Copilot** ajudou você a *construir* o sistema. O **Foundry** vai dar a ele
> *inteligência em tempo de execução*.

## A arquitetura que vamos montar

```
[ Cidadão fala ]
      │  (linguagem natural)
      ▼
[ Agente Foundry ] ──raciocina──> decide chamar uma ferramenta
      │
      ▼
[ ferramentas.py ]  gerar_bo(), consultar_historico()
      │  (HTTP)
      ▼
[ API do app /api ]  ← o mesmo sistema das Etapas 1 e 2
```

O agente **não substitui** o sistema: ele o **usa** como ferramenta.

## Pré-requisitos

1. Um **projeto no Foundry** com um **modelo implantado** (ex.: `gpt-4o-mini`).
   > O facilitador pode provisionar isso com a skill **microsoft-foundry**.
2. **Azure CLI** autenticada: `az login`.
3. O **app rodando** em um terminal:
   ```bash
   uvicorn app.main:app --reload
   ```

## Passo a passo

Trabalhe na pasta [`agente/`](../agente/).

### 1. Conheça as ferramentas

Abra [`agente/ferramentas.py`](../agente/ferramentas.py). Use o Copilot:

> Explique o que cada função deste arquivo faz e como ela se conecta ao app.

Repare: cada função é um wrapper sobre a API `/api` do app.

### 2. Configure o ambiente

```bash
cd agente
pip install -r requirements.txt
cp ../.env.example ../.env
```

Edite o `.env` e preencha:

```
FOUNDRY_PROJECT_ENDPOINT=https://<seu-projeto>.services.ai.azure.com/api/projects/<projeto>
FOUNDRY_MODEL_DEPLOYMENT=gpt-4o-mini
```

### 3. Complete o esqueleto do agente

Abra [`agente/agente_bo.py`](../agente/agente_bo.py) e procure os `TODO`s.
Refine as **instruções do agente** (`INSTRUCOES_AGENTE`) com a ajuda do Copilot:

> Melhore as instruções do agente para que ele peça os dados que faltarem antes
> de registrar o boletim e confirme o número gerado ao final.

### 4. Rode o agente

```bash
python agente_bo.py
```

O agente deve receber o relato de exemplo, **chamar a ferramenta `gerar_bo`** e
responder com o número e o tipo do boletim. Confira em
<http://localhost:8000/boletins> que o boletim realmente foi criado!

## Critério de conclusão

- [ ] O agente foi criado no Foundry sem erros.
- [ ] Ao receber um relato, o agente chama a ferramenta `gerar_bo`.
- [ ] O boletim aparece no histórico do app.
- [ ] Você consegue explicar a diferença entre "regra fixa" e "agente".

## Gancho para a próxima etapa

Por enquanto o agente roda em um script de demonstração. Na
[Etapa 4](fase4-integracao.md) vamos torná-lo **interativo** e discutir como
integrá-lo de verdade ao sistema.
