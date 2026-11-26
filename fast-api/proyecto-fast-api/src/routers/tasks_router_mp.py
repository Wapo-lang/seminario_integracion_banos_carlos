from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

flights_router = APIRouter()


class FlightCreate(BaseModel):
    codigo: str
    origen: str
    destino: str
    estado: Literal["programado", "abordando", "en vuelo", "aterrizado", "cancelado"] = "programado"


class FlightStatusUpdate(BaseModel):
    estado: Literal["programado", "abordando", "en vuelo", "aterrizado", "cancelado"]


FLIGHTS: list[FlightCreate] = [
    FlightCreate(codigo="AB123", origen="Quito", destino="Guayaquil"),
    FlightCreate(codigo="CD456", origen="Guayaquil", destino="Cuenca", estado="abordando"),
]


@flights_router.get("/vuelos", response_model=list[FlightCreate])
def list_flights() -> list[FlightCreate]:
    return FLIGHTS


@flights_router.post("/vuelos", response_model=FlightCreate)
def create_flight(flight: FlightCreate) -> FlightCreate:
    if any(existing.codigo == flight.codigo for existing in FLIGHTS):
        raise HTTPException(status_code=409, detail="Ya existe un vuelo con ese codigo")
    FLIGHTS.append(flight)
    return flight


@flights_router.patch("/vuelos/{codigo}/estado", response_model=FlightCreate)
def update_flight_status(codigo: str, update: FlightStatusUpdate) -> FlightCreate:
    for flight in FLIGHTS:
        if flight.codigo == codigo:
            flight.estado = update.estado
            return flight
    raise HTTPException(status_code=404, detail="Vuelo no encontrado")
