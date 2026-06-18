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

1. **Python 3.11+** instalado.
2. **VS Code** com a extensão **GitHub Copilot** ativa.
3. Suba o app uma vez para garantir que está tudo certo:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
   Acesse <http://localhost:8000> e registre um boletim de teste.

Pronto? Vá para a [Etapa 1](fase1-descoberta.md).
