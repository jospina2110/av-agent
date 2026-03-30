from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import trabajadores, asistencia, nomina, gastos, chat

app = FastAPI(
    title="AV Backend API",
    description="Backend para el sistema de gestión AV con arquitectura de agentes IA.",
    version="0.1.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(trabajadores.router, prefix="/api/trabajadores", tags=["trabajadores"])
app.include_router(asistencia.router, prefix="/api/asistencia", tags=["asistencia"])
app.include_router(nomina.router, prefix="/api/nomina", tags=["nomina"])
app.include_router(gastos.router, prefix="/api/gastos", tags=["gastos"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de AV"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)