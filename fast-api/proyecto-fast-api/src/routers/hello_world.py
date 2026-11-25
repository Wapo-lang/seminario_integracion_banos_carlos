from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str 

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "autor":"Carlos Baños",
            "version" : "0.1.0"}

@router.get("/carlos")
def endpoint_carlos() -> Mensaje:
    return Mensaje(texto="Hola Carlos", campo_interno= "desde Carlos link")

@router.get("/banos", response_model=Mensaje)
def endpoint_banos():
    return {"texto": "Hola Baños", 
            "prioridad": 5, 
            "campo_interno": "imprime desde endpoint canar"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Baños", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo", 
            "campo_extra":"no deberia salir"}