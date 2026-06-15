# Sistema de Boletim de Ocorrência (BO)

Aplicação base do workshop **GitHub Copilot + Microsoft Foundry**.

É um sistema simples de registro de Boletins de Ocorrência: o cidadão preenche
um formulário descrevendo o que aconteceu, e o sistema **classifica
automaticamente o tipo da ocorrência** (furto, roubo, acidente de trânsito,
etc.) e gera um boletim estruturado.

> A classificação atual é feita por **regras e palavras-chave** — sem nenhuma
> inteligência artificial. Essa é justamente a oportunidade que vamos explorar
> no workshop: entender o sistema com o Copilot, evoluí-lo e depois adicionar
> inteligência real com um **agente do Microsoft Foundry**.

## Roadmap de evolução

A evolução do sistema acontece em duas etapas bem definidas:

- **Fase 1 — Adicionar o campo de CPF do solicitante (GitHub Copilot):**
  evoluímos o sistema para capturar e armazenar o **CPF de quem registra o
  boletim**. Isso envolve incluir o campo no formulário HTML, no modelo de
  dados (`Ocorrência`/`Boletim`), na persistência em JSON e na API. É um
  exercício de modificação guiada de ponta a ponta, com o Copilot ajudando a
  propagar a mudança por todas as camadas do código.

- **Fase 2 — Adicionar um agente do AI Foundry para triagem inicial do BO
  (Microsoft Foundry):** substituímos a classificação por regras por um
  **agente inteligente do Microsoft Foundry** que faz a **triagem inicial do
  boletim de ocorrência** — analisando a descrição em linguagem natural para
  sugerir o tipo, a gravidade e o encaminhamento adequado. O agente usa a API
  do sistema como ferramenta, trazendo inteligência em tempo de execução.

## O que você vai fazer no workshop

O workshop está dividido em **5 etapas**. As **Fases 1 e 2** do roadmap de
evolução acima são construídas ao longo dessas etapas (CPF na Etapa 2; agente
de triagem nas Etapas 3 e 4).

| Etapa | Foco | Ferramenta |
|-------|------|-----------|
| 1 | Entender o sistema existente | GitHub Copilot |
| 2 | Modificar e evoluir o código (campo CPF) | GitHub Copilot |
| 3 | Criar um agente inteligente | Microsoft Foundry |
| 4 | Integrar o agente ao sistema | Foundry + API |
| 5 | Otimizar (testes, docs, qualidade) | GitHub Copilot |

Os guias de cada etapa estão na pasta [`workshop/`](workshop/).

## Estrutura do projeto

```
bo-app/
├── app/                  # Aplicação web (FastAPI)
│   ├── main.py           # Rotas HTML (formulário) e rotas /api (JSON)
│   ├── models.py         # Modelos de dados (Ocorrência e Boletim)
│   ├── classificacao.py  # Lógica de negócio: classificação do tipo
│   ├── repositorio.py    # Persistência dos boletins em JSON
│   ├── templates/        # Páginas HTML (Jinja2)
│   └── static/           # Estilos (CSS)
├── dados/
│   └── boletins.json     # Boletins registrados (com exemplos)
├── agente/               # Esqueleto do agente Foundry (Etapa 3+)
└── workshop/             # Guias e prompts de cada etapa
```

## Como executar (local)

Pré-requisitos: **Python 3.11+**.

```bash
# 1. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Inicie a aplicação
uvicorn app.main:app --reload
```

Acesse no navegador:

- Formulário de registro: <http://localhost:8000>
- Histórico de boletins: <http://localhost:8000/boletins>
- Documentação da API (Swagger): <http://localhost:8000/docs>

## API

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/api/boletins` | Registra um boletim a partir de JSON |
| `GET` | `/api/boletins` | Lista todos os boletins |
| `GET` | `/api/boletins/{numero_bo}` | Detalha um boletim específico |

Exemplo de registro via API:

```bash
curl -X POST http://localhost:8000/api/boletins \
  -H "Content-Type: application/json" \
  -d '{
    "solicitante": "Ana Pereira",
    "data_hora": "14/06/2026 22:30",
    "local": "Praça Central, 10",
    "descricao": "Fui vítima de um assalto à mão armada."
  }'
```

A API é a porta de entrada que o **agente Foundry** vai usar como ferramenta
na Etapa 3 do workshop.

## Passos macro das 5 etapas (com GitHub Copilot)

Um roteiro de alto nível de cada etapa, com sugestões de como usar o
**GitHub Copilot** (Chat, `#file`, `#selection` e autocompletar) para cumpri-las.
Os guias detalhados estão em [`workshop/`](workshop/).

### Etapa 1 — Entender o sistema existente

1. Peça ao Copilot uma visão geral da arquitetura e da responsabilidade de cada arquivo.
2. Investigue a lógica de classificação em [`app/classificacao.py`](app/classificacao.py).
3. Siga o fluxo do dado, do formulário até o `boletins.json`.

> 💡 *Copilot:* `Explique a arquitetura deste projeto e o que cada arquivo faz.`
> e `Como a função classificar_tipo decide o tipo de uma ocorrência?`

### Etapa 2 — Modificar e evoluir o código (campo CPF)

1. Adicione o campo `cpf` aos modelos em [`app/models.py`](app/models.py).
2. Inclua o campo no formulário e propague pela rota e pela montagem do boletim.
3. Exiba o CPF nas telas de detalhe e de listagem; teste pelo formulário e pela API.

> 💡 *Copilot:* selecione o modelo e peça `Adicione um campo cpf (string) a este modelo`;
> use o autocompletar ao replicar o padrão no template e na rota.

### Etapa 3 — Criar um agente inteligente (Microsoft Foundry)

1. Configure o acesso ao Foundry (`.env`, `az login`, modelo implantado).
2. Entenda as ferramentas em [`agente/ferramentas.py`](agente/ferramentas.py) e o esqueleto em [`agente/agente_bo.py`](agente/agente_bo.py).
3. Refine as instruções do agente para conversar e registrar boletins via API.

> 💡 *Copilot:* `Explique o que cada função de ferramentas.py faz e como chama a API.`
> e `Melhore as instruções do agente para pedir os dados que faltarem antes de registrar.`

### Etapa 4 — Integrar o agente ao sistema (Foundry + API)

1. Transforme a demonstração em um **loop de conversa interativo**.
2. Permita que o agente também **consulte o histórico**, não só registre.
3. Discuta como o agente viveria dentro do app (ex.: rota `POST /api/chat`).

> 💡 *Copilot:* `Transforme o main() em um loop de conversa que encerra com "sair".`
> e `Esboce uma rota POST /api/chat no main.py que repassa a mensagem ao agente.`

### Etapa 5 — Otimizar (testes, docs, qualidade)

1. Gere **testes** para a classificação e para as rotas `/api`.
2. Melhore o **tratamento de erros** (JSON ausente/corrompido, boletim não encontrado).
3. Adicione **docstrings** e revise a organização do código.

> 💡 *Copilot:* `Crie testes pytest para app/classificacao.py cobrindo todos os tipos.`
> e `Trate em repositorio.py o caso de boletins.json inexistente ou corrompido.`
