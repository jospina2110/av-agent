from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import trabajadores, asistencia, nomina, gastos, chat
from app.core.config import settings
from app.core.logger import get_logger
from app.core.exceptions import (
    ObrasIAException,
    NotFoundError,
    DuplicateError,
    ValidationError,
    BusinessRuleError,
    OCRError,
    not_found_handler,
    duplicate_handler,
    validation_handler,
    business_rule_handler,
    ocr_handler,
    generic_handler,
)

logger = get_logger(__name__)

app = FastAPI(
    title="ObrasIA API",
    description="Backend para el sistema de gestión de obras con arquitectura de agentes IA.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ───────────────────────────────────────────────────────────────────────
# En producción reemplaza ["*"] por la URL real del frontend
origins = ["*"] if settings.debug else [
    "https://tu-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Exception handlers ─────────────────────────────────────────────────────────
app.add_exception_handler(NotFoundError, not_found_handler)
app.add_exception_handler(DuplicateError, duplicate_handler)
app.add_exception_handler(ValidationError, validation_handler)
app.add_exception_handler(BusinessRuleError, business_rule_handler)
app.add_exception_handler(OCRError, ocr_handler)
app.add_exception_handler(ObrasIAException, generic_handler)

# ── Routers ────────────────────────────────────────────────────────────────────
app.include_router(trabajadores.router, prefix="/api/trabajadores", tags=["trabajadores"])
app.include_router(asistencia.router,   prefix="/api/asistencia",   tags=["asistencia"])
app.include_router(nomina.router,       prefix="/api/nomina",        tags=["nomina"])
app.include_router(gastos.router,       prefix="/api/gastos",        tags=["gastos"])
app.include_router(chat.router,         prefix="/api/chat",          tags=["chat"])

# ── Eventos de ciclo de vida ───────────────────────────────────────────────────
@app.on_event("startup")
async def on_startup():
    logger.info("ObrasIA API iniciando — env=%s", settings.app_env)


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("ObrasIA API apagándose")


# ── Endpoints base ─────────────────────────────────────────────────────────────
@app.get("/", tags=["root"])
async def root():
    return {"message": "Bienvenido a la API de ObrasIA"}


@app.get("/health", tags=["root"])
async def health():
    return {
        "status": "ok",
        "version": "0.1.0",
        "env": settings.app_env,
    }


# ── Entrypoint local ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
