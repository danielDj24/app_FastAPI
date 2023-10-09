import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""generate database with sqlalchemy and rute in the proyect"""
sqlite_file_name = "../database.sqlite" #databse name
base_dir = os.path.dirname(os.path.realpath(__file__)) #generate database

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" #url database

"""create engine for a database"""
engine = create_engine(database_url, echo =True)

"""generate sesion for the login database """
Session = sessionmaker(bind=engine)

Base= declarative_base()
