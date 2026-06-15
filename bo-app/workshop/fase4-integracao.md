# Etapa 4 — Integração

**Objetivo:** transformar o agente de demonstração em uma **conversa
interativa** e **integrá-lo ao app**, de modo que o sistema clássico de BO
passe a **permitir o registro do boletim por meio do agente**, fechando o ciclo
*Copilot constrói → Foundry dá inteligência*.

**Tempo sugerido:** ~30 min.

## O que vamos fazer

Na Etapa 3 o agente rodou com um relato fixo. Agora vamos:

1. Tornar a conversa **interativa** (o usuário digita e o agente responde).
2. Permitir que o agente **consulte o histórico**, não só registre.
3. **Integrar o agente ao app** com uma rota de chat, para que o BO possa ser
   criado conversando com o agente a partir do próprio sistema.

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

### 3. Integre o agente ao app (obrigatório)

Até aqui o agente vive em um script à parte. Agora ele precisa virar parte do
sistema: o app clássico de BO deve **permitir criar o boletim conversando com o
agente**. Faça a integração com a ajuda do Copilot.

Primeiro, torne a conversa reutilizável fora do loop de terminal:

> Extraia a lógica de conversa do `agente_bo.py` para uma função reutilizável
> que receba uma mensagem do cidadão e um identificador de conversa, e devolva a
> resposta do agente, reaproveitando a mesma thread por conversa.

Depois, exponha o agente como uma rota de chat no app, sem quebrar o que já
existe:

> Adicione ao app FastAPI uma rota de chat (página e/ou endpoint) que recebe uma
> mensagem, repassa para o agente Foundry e retorna a resposta. O agente deve
> usar as ferramentas que já chamam a API `/api/boletins`, permitindo registrar
> o BO pela conversa. Mantenha o formulário clássico funcionando em paralelo mas adicione uma opção na interface para acessar o chat do agente e permitir a criação do boletim de ocorrencia com o agente.

Por fim, valide o fluxo de ponta a ponta:

> Com o app rodando, registre um boletim pela rota de chat do agente e confirme
> que ele aparece em `/boletins`, com tipo classificado e número gerado.

> **Atenção a segurança:** ao mover o agente para dentro do app, não exponha o
> `FOUNDRY_PROJECT_ENDPOINT` nem credenciais no código ou no front-end. Mantenha
> esses valores no `.env`/variáveis de ambiente e use `DefaultAzureCredential`.

## Critério de conclusão

- [ ] O agente conversa de forma interativa, mantendo o contexto.
- [ ] O agente consegue tanto **registrar** quanto **consultar** boletins.
- [ ] **O agente está integrado ao app:** o sistema clássico permite criar um BO
      pela conversa com o agente, e o boletim aparece no histórico (`/boletins`).

## Gancho para a próxima etapa

O sistema cresceu: app + agente integrados. Mas falta **qualidade** — testes,
tratamento de erros e documentação. Na [Etapa 5](fase5-otimizacao.md) o Copilot
volta ao palco para nos ajudar a deixar tudo mais robusto.
