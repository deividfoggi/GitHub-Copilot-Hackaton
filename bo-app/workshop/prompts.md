# Biblioteca de Prompts

Uma coleção de prompts em português para usar com o **GitHub Copilot Chat**
durante o workshop. Adapte-os ao seu contexto — e crie os seus!

> Dica geral: dê **contexto** ao Copilot. Abra o arquivo relevante, selecione o
> trecho de código e use `#file` ou `#selection` para apontar exatamente do que
> você está falando.

## Descoberta de código (Etapa 1)

- `Explique a arquitetura deste projeto e a responsabilidade de cada arquivo.`
- `Onde e como este sistema decide o tipo de uma ocorrência? Explique passo a passo.`
- `Qual é o caminho completo de um dado, do formulário até ser persistido?`
- `Quais campos um boletim possui e quais NÃO são preenchidos pelo usuário?`
- `Existe algum risco ou limitação na forma atual de classificação? Liste-os.`
- `Desenhe um diagrama (mermaid) do fluxo de registro de um boletim.`

## Modificação de código (Etapa 2)

- `Quero adicionar um campo "CPF do solicitante". Quais arquivos e funções preciso alterar? Liste em ordem, sem mudar nada ainda.`
- `Faça a primeira camada dessa mudança e me explique o que vai alterar antes de aplicar.`
- `Adicione o campo de CPF na interface onde o cidadão registra a ocorrência.`
- `Garanta que o CPF seja repassado do recebimento até o boletim montado e persistido.`
- `Exiba o CPF do solicitante nas telas de detalhe e de histórico.`
- `Valide que o CPF informado tenha 11 dígitos.`
- `Como lidar com boletins antigos que não têm o campo cpf? Sugira opções.`

## Agente e Foundry (Etapas 3 e 4)

- `Quais rotas de API este app expõe? Mostre método, caminho e o que cada uma espera.`
- `Explique o que cada ferramenta do agente faz e como ela se conecta ao app.`
- `Melhore as instruções do agente para pedir dados que faltarem antes de registrar.`
- `Separe "criar a thread" de "enviar a mensagem" para manter o contexto da conversa.`
- `Transforme o ponto de entrada em um loop de conversa interativo que encerra com "sair".`
- `Esboce uma rota de chat no app que repassa a mensagem ao agente.`
- `Quais boas práticas de segurança devo seguir ao guardar o endpoint e segredos do Foundry?`

## Otimização (Etapa 5)

- `Crie testes pytest para a lógica de classificação, cobrindo todos os tipos e o caso sem correspondência.`
- `Gere testes para as rotas da API usando o TestClient do FastAPI.`
- `Trate o caso do arquivo de dados inexistente ou corrompido, com segurança.`
- `Retorne HTTP 404 quando um boletim não for encontrado, na página e na API.`
- `Adicione docstrings em português às funções centrais do projeto.`
- `Revise o ponto de entrada da aplicação e sugira melhorias de organização sem mudar o comportamento.`

## Prompts "meta" (úteis em qualquer etapa)

- `Não escreva o código ainda. Primeiro me explique seu plano em passos.`
- `Mostre apenas o diff das mudanças necessárias neste arquivo.`
- `Esse código tem algum bug ou caso não tratado? Aponte antes de corrigir.`
- `Explique este erro e proponha a correção mais simples.`
- `Há uma forma mais idiomática de escrever isto em Python? Mostre lado a lado.`
