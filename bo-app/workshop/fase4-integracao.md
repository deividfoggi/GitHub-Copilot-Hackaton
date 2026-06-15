# Etapa 4 — Integração

**Objetivo:** transformar o agente de demonstração em uma **conversa
interativa** e conectá-lo de forma mais natural ao sistema, fechando o ciclo
*Copilot constrói → Foundry dá inteligência*.

**Tempo sugerido:** ~30 min.

## O que vamos fazer

Na Etapa 3 o agente rodou com um relato fixo. Agora vamos:

1. Tornar a conversa **interativa** (o usuário digita e o agente responde).
2. Permitir que o agente **consulte o histórico**, não só registre.
3. Discutir como esse agente poderia viver **dentro do app**.

## Passo a passo

Continue na pasta [`agente/`](../agente/).

### 1. Loop de conversa interativo

Volte ao agente que **você criou na Etapa 3**. Use o Copilot para evoluir o
ponto de entrada do programa:

> Substitua o relato fixo por um loop interativo: leia a mensagem do usuário com
> `input()`, envie ao agente e imprima a resposta. Encerre quando o usuário
> digitar "sair". Reaproveite a mesma thread durante toda a conversa.

> **Dica importante:** para manter o contexto da conversa, crie a *thread* uma
> única vez (fora do loop) e apenas adicione novas mensagens a cada rodada.
> Peça ao Copilot para separar "criar a thread" de "enviar a mensagem".

### 2. Teste um diálogo real

Rode novamente o agente e experimente conversas como:

- "Quero registrar uma ocorrência."  → o agente deve **perguntar** os dados que faltam.
- "Quantos boletins de furto já existem?" → o agente deve **consultar o histórico**.
- "Me mostra os detalhes de um boletim específico." → o agente deve **consultar** o boletim.

### 3. Pense na integração de verdade

Discussão em grupo (com apoio do Copilot para prototipar):

- Como seria expor o agente como um **endpoint dentro do app** (uma rota de chat)?
- O que muda em termos de **autenticação** e **segredos** quando o agente sai do
  seu notebook e vai para produção?
- Onde guardar o `FOUNDRY_PROJECT_ENDPOINT` com segurança?

Prompt sugerido para prototipar (opcional):

> Mostre como eu poderia criar uma rota de chat no app que recebe uma mensagem
> e a repassa para o agente Foundry, retornando a resposta. Apenas um esboço,
> sem quebrar as rotas existentes.

## Critério de conclusão

- [ ] O agente conversa de forma interativa, mantendo o contexto.
- [ ] O agente consegue tanto **registrar** quanto **consultar** boletins.
- [ ] O grupo discutiu como integrar o agente ao app em produção.

## Gancho para a próxima etapa

O sistema cresceu: app + agente. Mas falta **qualidade** — testes, tratamento de
erros e documentação. Na [Etapa 5](fase5-otimizacao.md) o Copilot volta ao palco
para nos ajudar a deixar tudo mais robusto.
