# Etapa 5 — Otimização com o GitHub Copilot

**Objetivo:** elevar a qualidade do sistema — **testes**, **tratamento de erros**
e **documentação** — usando o Copilot para fazer o trabalho pesado.

**Tempo sugerido:** ~30 min.

## Por que otimizar

O sistema funciona, mas está "cru": não tem testes, trata pouco os erros e a
documentação é mínima. O Copilot é excelente para essas tarefas — escolha pelo
menos **duas** das trilhas abaixo.

## Trilha A — Testes automatizados

O projeto **ainda não tem testes**. Vamos criar.

> Crie testes com `pytest` para o arquivo `app/classificacao.py`. Cubra:
> classificação de cada tipo, o caso "Outros" quando nenhuma palavra-chave casa,
> e o formato do número do BO gerado por `gerar_numero_bo`.

Depois:

```bash
pip install pytest
pytest -v
```

Desafio extra:

> Gere também testes para as rotas `/api` usando o `TestClient` do FastAPI.

## Trilha B — Tratamento de erros

Hoje o app assume o "caminho feliz". Vamos torná-lo mais robusto.

> Em `app/repositorio.py`, trate o caso de o arquivo `boletins.json` não existir
> ou estar corrompido (JSON inválido), retornando uma lista vazia com segurança.

> Em `app/main.py`, retorne um erro HTTP 404 adequado quando um boletim não for
> encontrado nas rotas de detalhe (HTML e API).

## Trilha C — Documentação e qualidade de código

> Adicione docstrings claras (em português) às funções de `app/classificacao.py`
> e `app/repositorio.py`, explicando parâmetros e retorno.

> Revise o `app/main.py` e sugira melhorias de organização sem alterar o
> comportamento. Explique cada sugestão antes de aplicar.

## Trilha D — Refatorar a classificação (avançado)

Conecte o ciclo completo do workshop:

> Proponha como substituir a classificação por palavras-chave de
> `classificacao.py` por uma chamada ao **agente Foundry**, mantendo a mesma
> assinatura de função para não quebrar o resto do sistema. Apenas o desenho,
> destacando prós e contras.

Essa é a síntese da mensagem do dia: **a regra fixa (build com Copilot) pode dar
lugar à inteligência em tempo de execução (Foundry)** — sem reescrever o sistema
inteiro.

## Critério de conclusão

- [ ] Pelo menos duas trilhas concluídas.
- [ ] Se fez a Trilha A: `pytest` roda e passa.
- [ ] O grupo consegue resumir, em uma frase, a diferença entre **Copilot
      (build)** e **Foundry (run intelligence)**.

## Encerramento

Parabéns! Em 3 horas você:

1. **Entendeu** um sistema desconhecido com o Copilot.
2. **Evoluiu** o código com segurança.
3. **Criou** um agente inteligente no Foundry.
4. **Integrou** agente e sistema.
5. **Otimizou** com testes, robustez e documentação.

> **GitHub Copilot constrói. Microsoft Foundry pensa em tempo de execução.**
> Juntos, levam você do código à inteligência.
