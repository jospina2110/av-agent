# 🏗️ Sistema Inteligente de Gestión de Obras con IA

## 🚀 Descripción

Este proyecto es una plataforma inteligente para la gestión de obras de construcción que combina:

* 📊 Gestión de trabajadores
* 📅 Control de asistencia
* 💰 Cálculo de nómina
* 🧾 Registro de gastos con OCR + IA
* 🤖 Sistema multi-agente
* 🧠 Orquestador inteligente
* 🗣️ Interfaz conversacional (chat + voz)

El objetivo es automatizar procesos operativos en obra y convertirlos en decisiones inteligentes basadas en datos.

---

## 🧠 Arquitectura

```plaintext
Frontend / Chat / Voz
        ↓
Chat Agent
        ↓
Orchestrator (cerebro)
        ↓
Agentes especializados
        ↓
Servicios (lógica)
        ↓
Repositorios (DB)
        ↓
Base de datos
```

---

## 🧩 Módulos principales

### 👷 Trabajadores

* CRUD completo
* Información:

  * nombre
  * cédula
  * teléfono
  * cargo
  * especialidad
  * valor por día

---

### 📅 Asistencia

* Registro diario
* Estados:

  * presente
  * ausente
  * incapacidad
* Registro masivo
* Auditoría

---

### 💰 Nómina

* Cálculo automático
* Basado en asistencia
* Reportes:

  * semanal
  * quincenal
  * mensual

---

### 🧾 Gastos (OCR + IA) 🔥

* Subida de facturas
* Extracción automática de datos:

  * proveedor
  * NIT
  * fecha
  * total
* Clasificación automática
* Validación inteligente

---

### 🤖 Sistema Multi-Agente

* registro_agent
* asistencia_agent
* nomina_agent
* gastos_agent
* chat_agent

---

### 🧠 Orchestrator

* Router de intenciones (reglas + IA)
* Context Manager
* Workflow Engine
* Event Bus
* Manejo de errores
* Logging

---

### 🧠 Memoria híbrida

* Short-term (Redis)
* State (PostgreSQL)
* Long-term (histórico)
* Limpieza automática (TTL + resumen IA)

---

## ⚙️ Tecnologías

### Backend

* Python
* FastAPI

### Base de datos

* PostgreSQL

### Cache / memoria

* Redis

### IA

* OpenAI API (LLM)

### OCR

* EasyOCR (MVP)
* Google Vision API (producción)

### ORM

* SQLAlchemy

---

## 📁 Estructura del proyecto

```plaintext
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── agents/
│   ├── orchestrator/
│   ├── memory/
│   ├── ai/
│   └── utils/
```

---

## 🔄 Flujo de ejecución

```plaintext
Usuario → Chat → Orchestrator → Agente → Servicio → DB → Respuesta
```

---

## 🧠 Flujo de gastos (ejemplo)

```plaintext
Factura
 ↓
OCR
 ↓
Texto
 ↓
Reglas (regex)
 ↓
IA (parser)
 ↓
Validación
 ↓
Base de datos
```

---

## 🔐 Seguridad (pendiente / roadmap)

* Autenticación JWT
* Roles y permisos
* Control de acceso por obra

---

## 🚀 Roadmap

### 🟢 Fase 1 (MVP)

* CRUD trabajadores
* Asistencia
* Nómina básica

### 🟡 Fase 2

* Gastos + OCR + IA

### 🔴 Fase 3

* Chat inteligente
* Voz
* Recomendaciones automáticas

---

## 💡 Diferencial

Este sistema no solo gestiona datos, sino que:

* 🧠 entiende la operación de obra
* 🤖 automatiza decisiones
* 📊 genera inteligencia operativa

---

## 🏆 Estado del proyecto

* Arquitectura: ✅ definida
* Backend: 🟡 en desarrollo
* IA: 🟡 en integración
* MVP: 🔜 en construcción

---

## 🤝 Contribución

1. Fork del proyecto
2. Crear rama (`feature/nueva-funcionalidad`)
3. Commit
4. Push
5. Pull Request

---

## 📄 Licencia

MIT License

---

## 👨‍💻 Autor

Proyecto desarrollado como base para una plataforma SaaS de construcción inteligente con IA.

---
