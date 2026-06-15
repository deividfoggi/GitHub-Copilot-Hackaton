# Etapa 2 — Modificação guiada com o GitHub Copilot

**Objetivo:** evoluir o sistema adicionando um novo campo — o **CPF do
solicitante** — usando o Copilot para propagar a mudança por todas as camadas
com segurança.

**Tempo sugerido:** ~30 min.

## A tarefa

Hoje o boletim identifica o solicitante apenas pelo **nome**, o que não é
suficiente para um registro oficial. Sua missão: adicionar o campo **CPF do
solicitante** ao sistema, de ponta a ponta — da tela em que o cidadão digita
até onde o dado é guardado e exibido.

Diferente do tipo da ocorrência (que é **calculado** pelo sistema), o CPF é um
dado **informado pelo cidadão**: ele entra pela interface e pela API, não é
deduzido pelo sistema.

> Sugestão de regra: valide que o CPF tenha 11 dígitos. A validação completa
> (dígitos verificadores) pode ser um desafio extra para o grupo.

## Como abordar

Essa mudança atravessa **várias camadas** do sistema. O segredo é usar o Copilot
para descobrir **quais** são essas camadas — e alterar uma de cada vez.

### 1. Mapeie o impacto antes de mudar

Comece pedindo ao Copilot um plano, sem alterar nada ainda:

> Quero adicionar um campo "CPF do solicitante" a este sistema, do formulário
> até a persistência e a exibição. Quais arquivos e funções eu preciso alterar?
> Liste em ordem, sem mudar nada ainda.

### 2. Faça a mudança camada por camada

Siga a lista que o Copilot te deu. Em cada ponto, peça a alteração e **revise**
o que ele propõe antes de aplicar. Garanta que você cobriu:

- onde os dados de um boletim são **modelados**;
- onde o cidadão **digita** as informações;
- onde os dados são **recebidos** e o boletim é **montado**;
- onde o boletim é **exibido** (detalhe e histórico).

> Teste a cada camada em vez de mudar tudo de uma vez. Assim fica fácil saber
> onde algo quebrou.

## Testando a mudança

1. Reinicie o servidor (ou confie no `--reload`).
2. Registre um novo boletim informando o CPF → ele deve aparecer no detalhe do
   boletim e no histórico.
3. Confirme que o CPF foi de fato **persistido** junto com o boletim.
4. Teste também pela **API**: descubra com o Copilot qual rota registra um
   boletim e inclua o CPF na requisição.

> Os boletins antigos não têm o campo `cpf`. Discuta com o grupo: como
> o Copilot pode ajudar a lidar com dados antigos (migração / valor padrão)?

## Critério de conclusão

- [ ] O sistema passou a modelar o CPF do solicitante.
- [ ] A interface coleta o CPF do solicitante.
- [ ] O CPF é repassado do recebimento até o boletim montado.
- [ ] O CPF aparece na tela de detalhe e no histórico.
- [ ] Novos boletins persistem o CPF (e a API aceita o campo).

## Gancho para a próxima etapa

Repare: a classificação do tipo ainda é **baseada em regras fixas**. O sistema
não "entende" de fato a ocorrência. Na [Etapa 3](fase3-agente.md) vamos
introduzir um **agente do Microsoft Foundry** que conversa em linguagem natural
e raciocina sobre o relato — a inteligência em tempo de execução.
