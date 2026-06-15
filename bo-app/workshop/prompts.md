# Biblioteca de Prompts

Uma coleção de prompts em português para usar com o **GitHub Copilot Chat**
durante o workshop. Adapte-os ao seu contexto — e crie os seus!

> Dica geral: dê **contexto** ao Copilot. Abra o arquivo relevante, selecione o
> trecho de código e use `#file` ou `#selection` para apontar exatamente do que
> você está falando.

## Descoberta de código (Etapa 1)

- `Explique a arquitetura deste projeto e a responsabilidade de cada arquivo.`
- `Como a função classificar_tipo decide o tipo de uma ocorrência? Explique passo a passo.`
- `Qual é o caminho completo de um dado, do formulário até ser salvo no JSON?`
- `Quais campos um boletim possui e quais NÃO são preenchidos pelo usuário?`
- `Existe algum risco ou limitação na forma atual de classificação? Liste-os.`
- `Desenhe um diagrama (mermaid) do fluxo de registro de um boletim.`

## Modificação de código (Etapa 2)

- `Adicione um campo cpf (string) aos modelos Ocorrencia e BoletimOcorrencia.`
- `Adicione um campo "CPF do solicitante" ao formulario.html, obrigatório, com name="cpf".`
- `Em registrar_boletim, adicione o parâmetro cpf: str = Form(...) e repasse para a Ocorrencia.`
- `Atualize montar_boletim para preencher o cpf do boletim a partir da ocorrência.`
- `Exiba o CPF do solicitante em boletim.html e adicione uma coluna CPF em lista.html.`
- `Valide que o CPF informado tenha 11 dígitos.`
- `Como lidar com boletins antigos que não têm o campo cpf? Sugira opções.`

## Agente e Foundry (Etapas 3 e 4)

- `Explique o que cada função de ferramentas.py faz e como se conecta ao app.`
- `Melhore as instruções do agente para pedir dados que faltarem antes de registrar.`
- `Refatore a função conversar separando "criar thread" de "enviar mensagem".`
- `Transforme o main() em um loop de conversa interativo que encerra com "sair".`
- `Esboce uma rota POST /api/chat no main.py que repassa a mensagem ao agente.`
- `Quais boas práticas de segurança devo seguir ao guardar o endpoint e segredos do Foundry?`

## Otimização (Etapa 5)

- `Crie testes pytest para app/classificacao.py cobrindo todos os tipos e o caso "Outros".`
- `Gere testes para as rotas /api usando o TestClient do FastAPI.`
- `Trate em repositorio.py o caso de boletins.json inexistente ou corrompido.`
- `Retorne HTTP 404 quando um boletim não for encontrado, no HTML e na API.`
- `Adicione docstrings em português às funções de classificacao.py e repositorio.py.`
- `Revise main.py e sugira melhorias de organização sem mudar o comportamento.`

## Prompts "meta" (úteis em qualquer etapa)

- `Não escreva o código ainda. Primeiro me explique seu plano em passos.`
- `Mostre apenas o diff das mudanças necessárias neste arquivo.`
- `Esse código tem algum bug ou caso não tratado? Aponte antes de corrigir.`
- `Explique este erro e proponha a correção mais simples.`
- `Há uma forma mais idiomática de escrever isto em Python? Mostre lado a lado.`
