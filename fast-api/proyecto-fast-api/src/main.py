from fastapi import FastAPI
from src.routers.hello_world_mp import router
from src.routers.tasks_router_mp import flights_router

app = FastAPI(title="Control de vuelos del aeropuerto")


app.include_router(router)
app.include_router(flights_router)