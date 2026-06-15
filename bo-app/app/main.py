"""Aplicação web do sistema de Boletim de Ocorrência (BO).

Expõe duas interfaces:
- Rotas HTML: formulário para registrar e visualizar boletins (uso humano).
- Rotas /api: endpoints JSON usados por integrações, como o agente Foundry.
"""

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.classificacao import montar_boletim
from app.models import BoletimOcorrencia, Ocorrencia
from app.repositorio import (
    buscar_por_numero,
    carregar_boletins,
    contar_boletins,
    salvar_boletim,
)

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Sistema de Boletim de Ocorrência")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# -------------------- Rotas HTML (interface do cidadão) --------------------


@app.get("/", response_class=HTMLResponse)
def exibir_formulario(request: Request):
    """Exibe o formulário de registro de ocorrência."""
    return templates.TemplateResponse("formulario.html", {"request": request})


@app.post("/boletins", response_class=HTMLResponse)
def registrar_boletim(
    request: Request,
    solicitante: str = Form(...),
    data_hora: str = Form(...),
    local: str = Form(...),
    descricao: str = Form(...),
):
    """Recebe os dados do formulário, gera e salva o boletim."""
    ocorrencia = Ocorrencia(
        solicitante=solicitante,
        data_hora=data_hora,
        local=local,
        descricao=descricao,
    )
    boletim = montar_boletim(ocorrencia, contar_boletins())
    salvar_boletim(boletim)
    return templates.TemplateResponse(
        "boletim.html", {"request": request, "boletim": boletim.model_dump()}
    )


@app.get("/boletins", response_class=HTMLResponse)
def listar_boletins(request: Request):
    """Exibe o histórico de boletins registrados."""
    boletins = carregar_boletins()
    return templates.TemplateResponse(
        "lista.html", {"request": request, "boletins": boletins}
    )


@app.get("/boletins/{numero_bo}", response_class=HTMLResponse)
def detalhar_boletim(request: Request, numero_bo: str):
    """Exibe os detalhes de um boletim específico."""
    boletim = buscar_por_numero(numero_bo)
    return templates.TemplateResponse(
        "boletim.html", {"request": request, "boletim": boletim}
    )


# -------------------- Rotas /api (integrações e agente) --------------------


@app.post("/api/boletins", response_model=BoletimOcorrencia)
def api_registrar_boletim(ocorrencia: Ocorrencia):
    """Registra um boletim a partir de um JSON e retorna o boletim gerado."""
    boletim = montar_boletim(ocorrencia, contar_boletins())
    salvar_boletim(boletim)
    return boletim


@app.get("/api/boletins")
def api_listar_boletins():
    """Retorna o histórico de boletins em JSON."""
    return carregar_boletins()


@app.get("/api/boletins/{numero_bo}")
def api_detalhar_boletim(numero_bo: str):
    """Retorna um boletim específico em JSON."""
    return buscar_por_numero(numero_bo)
