# Workshop: GitHub Copilot + Microsoft Foundry

Bem-vindo! Neste workshop de **3 horas** você vai partir de um sistema real e
simples — um cadastro de **Boletins de Ocorrência** — e percorrer toda a
jornada: **entender → evoluir → dar inteligência → integrar → otimizar**.

> **A grande mensagem:** o **GitHub Copilot** é seu copiloto para **construir**
> (entender e escrever código rápido). O **Microsoft Foundry** dá a
> **inteligência em tempo de execução** (um agente que raciocina e age).
> Copilot = *build*. Foundry = *run intelligence*.

## As 5 etapas

| Etapa | Tema | Ferramenta principal | Guia |
|-------|------|----------------------|------|
| 1 | Descoberta do código | GitHub Copilot | [fase1-descoberta.md](fase1-descoberta.md) |
| 2 | Modificação guiada | GitHub Copilot | [fase2-modificacao.md](fase2-modificacao.md) |
| 3 | Introdução ao agente | Microsoft Foundry | [fase3-agente.md](fase3-agente.md) |
| 4 | Integração | Foundry + API | [fase4-integracao.md](fase4-integracao.md) |
| 5 | Otimização | GitHub Copilot | [fase5-otimizacao.md](fase5-otimizacao.md) |

A biblioteca de prompts úteis está em [prompts.md](prompts.md).

## Antes de começar

### Pré-requisitos

> VS Code e a extensão GitHub Copilot já estão instalados na máquina do workshop.

Abra o VSCode, abra o terminal integrado (`Ctrl + ``) e instale os requisitos usando os comandos abaixo:

```powershell
winget install -e --id Python.Python.3.11
winget install -e --id Git.Git
winget install -e --id Microsoft.AzureCLI
```

Adicione ao PATH do usuário:

```powershell
$gitPath = "C:\Program Files\Git\cmd"
$azPath = "C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin"
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ((Test-Path $gitPath) -and ($userPath -notlike "*$gitPath*")) {
	$userPath = "$userPath;$gitPath"
}

if ((Test-Path $azPath) -and ($userPath -notlike "*$azPath*")) {
	$userPath = "$userPath;$azPath"
}

[Environment]::SetEnvironmentVariable("Path", $userPath, "User")
```

**Feche e reabra o VS Code** antes de seguir.

### Verifique o ambiente

Confirme no terminal que tudo está acessível:

```powershell
py --version       # deve mostrar 3.11 ou superior
git --version
az --version
```

### Clone o repositório

Clone o repositório e entre na pasta:

```powershell
git clone https://github.com/deividfoggi/GitHub-Copilot-Hackaton.git
cd GitHub-Copilot-Hackaton
```

### Abra a pasta no VS Code

Com a pasta clonada aberta no terminal, execute:

```powershell
code .
```

Se o comando `code` não funcionar, abra manualmente pelo VS Code:
`File` -> `Open Folder...` -> selecione `GitHub-Copilot-Hackaton`.

### Confira os arquivos e abra o README da raiz

No painel **Explorer** do VS Code, expanda a pasta bo-app/workshop e selecione `README.md` para abri-lo e continue os passos abaixo.

### Suba o app uma vez


**Windows (PowerShell ou Prompt de Comando):**

```powershell
cd bo-app
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Abra o navegador, <http://localhost:8000> e registre um boletim de teste.

### Autentique no GitHub Copilot

Como último passo de preparação, autentique no GitHub Copilot com a credencial
fornecida para o workshop:

1. No VS Code, clique no ícone do GitHub Copilot na barra de status, logo acima do relógio do Windows. ![alt text](media/copilot-icon.png)
2. Clique no botão **Use AI Features**.
3. Clique em **Continue with GitHub** e siga o processo de login usando a credencial fornecida pela organização do workshop.
4. Quando solicitado, clique em Continue e Authorize para conceder as permissões necessárias.
5. Quando colicitado abrir o Visual Studio Code, clique em Open.
6. Para confirmar de que o Copilot esta realmente autenticado, clique novamente no ícone do GitHub Copilot na barra de status. Ele deve mostrar Informações sobre o uso (Copilot Business Usage) e o botão **Use AI Features** não deve ser mais exibido.

Pronto? Vá para a [Etapa 1](fase1-descoberta.md).
