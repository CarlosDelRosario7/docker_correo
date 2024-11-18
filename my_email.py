import smtplib
import ssl
from correo import Correo

class MyEmail:
    def __init__(self, correo: Correo):
        self.correo = correo

    def enviar(self):
        mensaje = f"Subject: {self.correo.asunto}\n\n{self.correo.cuerpo}"
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL(self.correo.smtp_server, self.correo.smtp_port, context=context) as server:
                server.login(self.correo.email, self.correo.clave)
                server.sendmail(self.correo.email, self.correo.destinatario, mensaje.encode('utf-8'))
                return "Correo enviado exitosamente!"
        except Exception as e:
            return f"Ocurrió un error: {e}"
