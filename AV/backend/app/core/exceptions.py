from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse


# ── Excepciones de dominio ─────────────────────────────────────────────────────

class ObrasIAException(Exception):
    """Base para todas las excepciones del sistema."""
    def __init__(self, message: str, code: str = "error_interno"):
        self.message = message
        self.code = code
        super().__init__(message)


class NotFoundError(ObrasIAException):
    """Recurso no encontrado."""
    def __init__(self, resource: str, id: int | str):
        super().__init__(
            message=f"{resource} con id '{id}' no existe",
            code="not_found",
        )


class DuplicateError(ObrasIAException):
    """Registro duplicado — viola unique constraint."""
    def __init__(self, resource: str, field: str, value: str):
        super().__init__(
            message=f"Ya existe un {resource} con {field} '{value}'",
            code="duplicate",
        )


class ValidationError(ObrasIAException):
    """Error de validación de negocio (distinto al de Pydantic)."""
    def __init__(self, message: str):
        super().__init__(message=message, code="validation_error")


class BusinessRuleError(ObrasIAException):
    """Violación de regla de negocio."""
    def __init__(self, message: str):
        super().__init__(message=message, code="business_rule_error")


class OCRError(ObrasIAException):
    """Error durante el procesamiento OCR de una factura."""
    def __init__(self, message: str = "No se pudo procesar la imagen"):
        super().__init__(message=message, code="ocr_error")


# ── Handlers para FastAPI ──────────────────────────────────────────────────────

async def not_found_handler(request: Request, exc: NotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"error": exc.code, "message": exc.message},
    )


async def duplicate_handler(request: Request, exc: DuplicateError) -> JSONResponse:
    return JSONResponse(
        status_code=409,
        content={"error": exc.code, "message": exc.message},
    )


async def validation_handler(request: Request, exc: ValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"error": exc.code, "message": exc.message},
    )


async def business_rule_handler(request: Request, exc: BusinessRuleError) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"error": exc.code, "message": exc.message},
    )


async def ocr_handler(request: Request, exc: OCRError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={"error": exc.code, "message": exc.message},
    )


async def generic_handler(request: Request, exc: ObrasIAException) -> JSONResponse:
    return JSONResponse(
        status_code=500,
        content={"error": exc.code, "message": exc.message},
    )
