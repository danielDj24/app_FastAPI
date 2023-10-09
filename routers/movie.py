from fastapi import APIRouter
from fastapi import  Body, Path, Query, Depends
from fastapi.responses import JSONResponse #permite enviar contenido al cliente
from typing import   List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder #pass model to object
from middlewares.jwt_bearer import JWTbearer
from services.movie import MovieService
from schemas.movie import Movies


movie_router = APIRouter()

@movie_router.get("/movies",tags=['movies'], response_model= List[Movies], status_code= 200, dependencies=[Depends(JWTbearer())])
#.json movies
def get_movies() -> List[Movies]:
    """return list movies of the database  """
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200,content= jsonable_encoder(result))

@movie_router.get('/movies/{id}',tags=['movies'], response_model=Movies,status_code=200) #url id movie
def get_movie(id: int  = Path(ge=1, le=2000)) -> Movies:
    """return movie with id"""
    db= Session()
    result= MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message":"movie not found" })
    return JSONResponse(status_code= 200, content= jsonable_encoder(result))


@movie_router.get('/movies/', tags=["movies"], response_model= List[Movies],status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=20))-> List[Movies] :
    """return movies by a category"""
    db= Session()
    category_result=MovieService(db).get_movies_by_category(category)
    if not category_result:
        return JSONResponse(status_code=404, content={'message':'category not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(category_result))

    
@movie_router.post('/movies', tags=['movies'], response_model= dict, status_code= 201)
def create_movie(movie: Movies) -> dict:
    """create the movies with a parameters and save a database"""
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201,content= {"message": "movie register in the database"})


@movie_router.put('/movies/{id}', tags=['movies'], response_model= dict, status_code=200)
def update_movie(id: int, movie: Movies) -> dict:
    """update de movie with a parameters in the database"""
    db = Session()
    result_update= MovieService(db).get_movie(id)
    if not result_update:
        return JSONResponse(status_code=404, content= {'message':'movie not update'})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200,content={"message": "modified movie"})


@movie_router.delete('/movies/{id}', tags=['movies'], response_model= dict, status_code= 200)
def delete_movie(id: int) -> dict:
    """remove movie with a database with id """
    db = Session()
    result_delete = MovieService(db).get_movie(id)
    if not result_delete:
        return JSONResponse(status_code=404, content= {'message': 'movie not found'})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={'message': 'movie eliminate'})
    