# Stage 0 Backend Assessment - Genderize Proxy API

## 🚀 Live Demo
**Base URL:** ``

## 📌 Project Overview
Built with FastAPI. It acts as a proxy and data transformation layer for the public Genderize API. It evaluates incoming names, enforces strict input validation, makes asynchronous network calls to the external API, processes the raw data according to specific business logic, and returns a strictly formatted JSON contract.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Server:** Uvicorn (ASGI)
* **HTTP Client:** httpx (Asynchronous I/O)
* **Validation:** Pydantic

## 🧠 Architectural Decisions
 modular architecture separated by concern:
* `main.py`: The orchestrator. Handles routing, CORS configuration, and global exception handling to guarantee strict JSON error formatting.
* `schemas.py`: Pydantic models that enforce the exact input and output data contracts.
* `clients.py`: The isolated network layer. Handles outbound asynchronous requests and protects the server with strict timeout policies.
* `services.py`: The core business logic. Evaluates data edge cases, calculates the `is_confident` metric, and generates the dynamic UTC `processed_at` timestamps.

## 💻 Local Setup & Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/carl-yom/Genderize_proxy_server.git](https://github.com/carl-yom/Genderize_proxy_server.git)
