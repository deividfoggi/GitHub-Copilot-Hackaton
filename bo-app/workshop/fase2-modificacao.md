# Etapa 2 — Modificação guiada com o GitHub Copilot

**Objetivo:** evoluir o sistema adicionando um novo campo — o **CPF do
solicitante** — usando o Copilot para propagar a mudança por todas as camadas
com segurança.

**Tempo sugerido:** ~30 min.

## A tarefa

Hoje o boletim identifica o solicitante apenas pelo **nome**, o que não é
suficiente para um registro oficial. Vamos adicionar o campo **`cpf`** ao
solicitante, capturando-o no formulário e propagando-o pelo modelo de dados,
pela persistência em JSON e pela API.

Diferente do `tipo` (que é **calculado** a partir da descrição), o CPF é um
dado **informado pelo cidadão** — ele entra pelo formulário e pela API, não é
deduzido pelo sistema.

> Sugestão de regra: valide que o CPF tenha 11 dígitos. A validação completa
> (dígitos verificadores) pode ser um desafio extra para o grupo.

## Passo a passo

A mudança atravessa várias camadas. Use o Copilot em cada uma.

### 1. Modelo de dados

Em [`app/models.py`](../app/models.py), adicione o campo `cpf` aos modelos
`Ocorrencia` (entrada) e `BoletimOcorrencia` (saída). Prompt sugerido:

> Adicione um campo `cpf` (string) aos modelos `Ocorrencia` e
> `BoletimOcorrencia`, com uma descrição indicando que é o CPF de quem
> registra a ocorrência.

### 2. Formulário

Em [`app/templates/formulario.html`](../app/templates/formulario.html),
adicione o campo de CPF. Prompt sugerido:

> Adicione um campo de entrada "CPF do solicitante" ao formulário, logo abaixo
> do nome do solicitante, com `name="cpf"`, obrigatório e um placeholder de
> exemplo.

### 3. Rota e montagem do boletim

Em [`app/main.py`](../app/main.py), receba o novo campo do formulário e repasse
para a `Ocorrencia`. Prompt sugerido:

> Em `registrar_boletim`, adicione o parâmetro `cpf: str = Form(...)` e inclua
> `cpf=cpf` ao criar a `Ocorrencia`.

Em [`app/classificacao.py`](../app/classificacao.py), faça `montar_boletim`
copiar o CPF para o boletim:

> Atualize `montar_boletim` para também preencher o campo `cpf` do
> `BoletimOcorrencia` a partir da `Ocorrencia`.

### 4. Exibição

Mostre o CPF nas telas. Prompts sugeridos:

> Em `boletim.html`, exiba o CPF do solicitante junto com o nome.

> Em `lista.html`, adicione uma coluna "CPF" na tabela de boletins.

## Testando a mudança

1. Reinicie o servidor (ou confie no `--reload`).
2. Registre um novo boletim informando o CPF → ele deve aparecer no detalhe do
   boletim e no histórico.
3. Confira que o CPF foi salvo no arquivo
   [`dados/boletins.json`](../dados/boletins.json).
4. Teste também via API (`POST /api/boletins`) incluindo o campo `cpf` no JSON.

> Os boletins antigos do seed não têm o campo `cpf`. Discuta com o grupo: como
> o Copilot pode ajudar a lidar com dados antigos (migração / valor padrão)?

## Critério de conclusão

- [ ] O campo `cpf` existe nos modelos `Ocorrencia` e `BoletimOcorrencia`.
- [ ] O formulário coleta o CPF do solicitante.
- [ ] O CPF é repassado da rota até o boletim montado.
- [ ] O CPF aparece na tela de detalhe e no histórico.
- [ ] Novos boletins salvam o CPF no JSON (e a API aceita o campo).

## Gancho para a próxima etapa

Repare: a classificação do tipo ainda é **baseada em regras fixas**. O sistema
não "entende" de fato a ocorrência. Na [Etapa 3](fase3-agente.md) vamos
introduzir um **agente do Microsoft Foundry** que conversa em linguagem natural
e raciocina sobre o relato — a inteligência em tempo de execução.
