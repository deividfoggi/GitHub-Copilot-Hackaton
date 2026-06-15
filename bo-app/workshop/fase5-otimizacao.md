# Etapa 5 — Otimização com o GitHub Copilot

**Objetivo:** elevar a qualidade do sistema — **testes**, **tratamento de erros**
e **documentação** — usando o Copilot para fazer o trabalho pesado.

**Tempo sugerido:** ~30 min.

## Por que otimizar

O sistema funciona, mas está "cru": não tem testes, trata pouco os erros e a
documentação é mínima. O Copilot é excelente para essas tarefas — escolha pelo
menos **duas** das trilhas abaixo.

## Trilha A — Testes automatizados

O projeto **ainda não tem testes**. Vamos criar. Comece pedindo ao Copilot para
localizar a lógica mais importante de testar (a classificação e a geração do
número do boletim) e cobri-la:

> Crie testes com `pytest` para a lógica de classificação deste projeto. Cubra
> cada tipo de ocorrência, o caso em que nenhuma regra casa e o formato do
> número do boletim gerado.

Depois (com o `.venv` ativo — veja a nota abaixo):

```bash
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
pytest -v
```

> Em um terminal novo, ative o `.venv` da raiz (`bo-app/`) antes do `pip
> install`. Sem o venv ativo, o `pip` usa o Python do sistema e falha com
> `externally-managed-environment` (PEP 668) no macOS/Linux.

Desafio extra:

> Gere também testes para as rotas da API usando o `TestClient` do FastAPI.

## Trilha B — Tratamento de erros

Hoje o app assume o "caminho feliz". Vamos torná-lo mais robusto. Use o Copilot
para encontrar os pontos frágeis e protegê-los:

> Onde este projeto lê os dados persistidos? Trate o caso de o arquivo de dados
> não existir ou estar corrompido, retornando uma lista vazia com segurança.

> Garanta que o sistema retorne um erro HTTP 404 adequado quando um boletim não
> for encontrado, tanto na página quanto na API.

## Trilha C — Documentação e qualidade de código

> Adicione docstrings claras (em português) às funções centrais do projeto
> (classificação e persistência), explicando parâmetros e retorno.

> Revise o ponto de entrada da aplicação e sugira melhorias de organização sem
> alterar o comportamento. Explique cada sugestão antes de aplicar.

## Trilha D — Refatorar a classificação (avançado)

Conecte o ciclo completo do workshop:

> Proponha como substituir a classificação por palavras-chave por uma chamada ao
> **agente Foundry**, mantendo a mesma assinatura de função para não quebrar o
> resto do sistema. Apenas o desenho, destacando prós e contras.

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
