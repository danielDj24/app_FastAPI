from fastapi import FastAPI
from fastapi.responses import HTMLResponse #permite enviar contenido al cliente
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()#creamos la app
app.title= "aplicacion con FASTAPI" #cambia el titulo dentro de la doc
app.version = "0.0.1"

"""middleware for manage errors"""
app.add_middleware(ErrorHandler)#llamamos el midleware creado

"""routes for a website"""
app.include_router(user_router)
app.include_router(movie_router)


"""Generate the data_base"""
Base.metadata.create_all(bind= engine)





