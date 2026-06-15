# Etapa 1 — Descoberta do código com o GitHub Copilot

**Objetivo:** entender, em poucos minutos, como o sistema funciona — sem ler
linha por linha. Você vai usar o Copilot Chat como um guia que explica o código.

**Tempo sugerido:** ~30 min (depois do setup).

## Contexto

Você acabou de "herdar" este projeto. Ele registra Boletins de Ocorrência e
classifica o tipo automaticamente. Mas como? Vamos descobrir com o Copilot.

## Passo a passo

### 1. Tenha uma visão geral

Abra o Copilot Chat e peça uma explicação do projeto inteiro. Use o prompt:

> Explique a arquitetura deste projeto. Quais são os principais arquivos e qual
> a responsabilidade de cada um?

Compare a resposta com a estrutura em [`README.md`](../README.md).

### 2. Encontre o "coração" do sistema

A lógica mais interessante está em [`app/classificacao.py`](../app/classificacao.py).
Abra o arquivo e pergunte:

> Como este arquivo decide o tipo de uma ocorrência? Explique passo a passo a
> função `classificar_tipo`.

**Pergunta para refletir:** o que acontece se a descrição não contém nenhuma
palavra-chave conhecida?

### 3. Siga o fluxo de uma requisição

Abra [`app/main.py`](../app/main.py) e pergunte:

> Quando o usuário envia o formulário, qual é o caminho completo do dado até ele
> ser salvo? Cite as funções e arquivos envolvidos na ordem.

Desenhe (ou peça ao Copilot para desenhar) o fluxo da transação na aplicação.

### 4. Entenda os dados

Abra [`app/models.py`](../app/models.py) e [`dados/boletins.json`](../dados/boletins.json).
Pergunte:

> Quais campos um boletim possui? Há algum campo que NÃO é preenchido pelo
> usuário diretamente? De onde ele vem?

## Critério de conclusão

Você consegue responder, sem olhar o código:

- [ ] Onde fica a lógica de classificação do tipo.
- [ ] Como o tipo é decidido (regras por palavra-chave).
- [ ] O que acontece quando nenhuma palavra-chave casa.
- [ ] O caminho do dado, do formulário até o arquivo JSON.

## Gancho para a próxima etapa

O boletim identifica o solicitante apenas pelo **nome** — o que não basta para
um registro oficial. E se quiséssemos registrar também o **CPF** de quem abre a
ocorrência? Na [Etapa 2](fase2-modificacao.md) vamos evoluir o sistema com a
ajuda do Copilot.
