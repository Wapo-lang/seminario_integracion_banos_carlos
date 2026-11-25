# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Curso FastAPI + uv")


class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@app.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv",
            "autor": "Carlos Baños",
            "version": "0.13.7"}

@app.get("/carlos")
def endpoint_carlos() -> Mensaje:
    return Mensaje(texto="Hola")

@app.get("/banos", response_model=Mensaje)
def endpoint_banos():
    return {"texto": "Hola", "prioridad": 5, "campo_interno": "no debería salir"}

@app.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Carlos",
             "prioridad": 5, 
             "campo_interno": "si debe salir incluido el modelo",
             "campo_externo": "no debería salir"}