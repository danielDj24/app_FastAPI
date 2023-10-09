from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Movie(Base):
    """Model with the structure of the database """
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)