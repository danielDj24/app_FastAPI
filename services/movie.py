from models.movie import Movie as MovieModel
from schemas.movie import Movies
class MovieService():
    """Constructor service and access a db"""
    def __init__(self,db) -> None:
        self.db = db
        
    def get_movies(self):
        """get the all movies"""
        result=self.db.query(MovieModel).all()
        return result
    
    def get_movie(self,id):
        """get movie with id"""
        result=self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self, category):
        """get movies by category"""
        result= self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self,movie: Movies):
        """create a new movie"""
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self,id:int, data:Movies):
        """modified movie by id """
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating =data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self,id):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return