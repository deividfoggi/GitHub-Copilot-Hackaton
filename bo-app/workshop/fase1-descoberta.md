# Etapa 1 — Descoberta do código com o GitHub Copilot

**Objetivo:** entender, em poucos minutos, como o sistema funciona — sem ler
linha por linha. Você vai usar o Copilot Chat como um guia que explica o código.

**Tempo sugerido:** ~30 min (depois do setup).

## Contexto

Você acabou de "herdar" este projeto. Ele registra Boletins de Ocorrência e
classifica o tipo automaticamente. Mas como? Vamos descobrir com o Copilot.

## Passo a passo

> Não tente ler os arquivos um por um. Deixe o Copilot ser seu guia: faça
> perguntas e deixe que ele aponte os arquivos e a lógica relevantes para você.

### 1. Tenha uma visão geral

Abra o Copilot Chat e peça uma explicação do projeto inteiro. Por exemplo:

> Explique a arquitetura deste projeto. Quais são os principais arquivos e qual
> a responsabilidade de cada um?

A partir da resposta, deixe que o Copilot indique por onde vale a pena começar.

### 2. Encontre o "coração" do sistema

O sistema decide sozinho o tipo de cada ocorrência. **Onde** e **como** isso
acontece? Use o Copilot para localizar e explicar essa lógica:

> Onde e como este sistema decide o tipo de uma ocorrência? Mostre o arquivo
> responsável e explique a lógica passo a passo.

**Pergunta para refletir:** o que acontece quando o relato não se encaixa em
nenhuma das regras conhecidas?

### 3. Siga o fluxo de uma requisição

Descubra, com o Copilot, o caminho completo de um dado quando o usuário envia
o formulário:

> Quando o usuário envia o formulário, qual é o caminho completo do dado até ele
> ser salvo? Cite as funções e arquivos envolvidos, na ordem.

Peça ao Copilot para desenhar esse fluxo (por exemplo, em um diagrama mermaid).

### 4. Entenda os dados

Investigue, com a ajuda do Copilot, como um boletim é estruturado:

> Quais campos um boletim possui? Há algum campo que NÃO é preenchido pelo
> usuário diretamente? De onde ele vem?

## Critério de conclusão

Você consegue responder, sem olhar o código:

- [ ] Onde fica a lógica que decide o tipo da ocorrência.
- [ ] Como o tipo é decidido.
- [ ] O que acontece quando o relato não casa com nenhuma regra.
- [ ] O caminho do dado, do formulário até onde ele é persistido.

## Gancho para a próxima etapa

O boletim identifica o solicitante apenas pelo **nome** — o que não basta para
um registro oficial. E se quiséssemos registrar também o **CPF** de quem abre a
ocorrência? Na [Etapa 2](fase2-modificacao.md) vamos evoluir o sistema com a
ajuda do Copilot.
