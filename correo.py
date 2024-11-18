from pydantic import BaseModel
from dotenv import load_dotenv
import os

class Correo(BaseModel):
  email: str = os.getenv("EMAIL")
  clave: str = os.getenv("PASSWORD")
  destinatario: str
  asunto: str
  cuerpo: str
  smtp_server: str = os.getenv("SMTP_SERVER")
  smtp_port: str = os.getenv("SMTP_PORT")