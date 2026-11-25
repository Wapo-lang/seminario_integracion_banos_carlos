from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Sistema de control de vuelos del aeropuerto"}
