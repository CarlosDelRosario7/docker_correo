from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from correo import Correo
from my_email import MyEmail

from dotenv import load_dotenv
import os 

app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
  correct_username = os.getenv("FAST_ADMIN")
  correct_password = os.getenv("FAST_CLAVE")
  if credentials.username != correct_username or credentials.password != correct_password:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="El usuario o la contraseña son incorrectos",
      headers={"WWW-Authenticate": "Basic"},
    )

@app.get("/")
async def enviar_html():
  return FileResponse("index.html")

@app.post("/")
async def enviar_correo(correo: Correo):
  return MyEmail(correo).enviar()

@app.get("/docs", include_in_schema=False)
async def get_docs(credentials: HTTPBasicCredentials = Depends(authenticate)):
  return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@app.get("/redoc", include_in_schema=False)
async def get_redoc(credentials: HTTPBasicCredentials = Depends(authenticate)):
  return get_redoc_html(openapi_url="/openapi.json", title="redoc")