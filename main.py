from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

import schemas
import clients
import services

app = FastAPI(title="Genderize Classification API")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request : Request, exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status" : "error", "message": exc.detail}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request:Request, exc : RequestValidationError):
    error_msg = exc.errors()[0].get("msg", "Invalid input")
    return JSONResponse(
        status_code = 422,
        content = {
            "status" : "error",
            "message":f"Validation Error: {error_msg}"
        }
    )


@app.get("/api/classify", response_model = schemas.SuccessResponse)
async def classify_name(name: str | None = None):
    if not name or not name.strip():
        raise HTTPException(
            status_code = 400,
            detail="Name query parameter is missing or empty"
        )
    # 422 automatically handled by fastapi and requestvalidation error handler

    raw_data = await clients.fetch_gender_prediction(name)
    processed_dict = services.process_classification(raw_data)

    return schemas.SuccessResponse(data = processed_dict)
