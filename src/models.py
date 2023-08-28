import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float , DATE
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250),nullable=False)
    email = Column(String(250),nullable=False)

class StarShips(Base):
    __tablename__ = 'starShips'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    model =  Column(String(250), nullable=False)
    manufacturer =  Column(String(250) )
    cost_in_credits =  Column(Float,nullable=False)
    length =  Column(Float,nullable=False )
    max_atmosphering_speed = Column(Integer,nullable=False)
    crew =  Column(String(250),nullable=False )
    passengers =  Column(Integer,nullable=False )
    cargo_capacity =  Column(Float,nullable=False)
    consumables =  Column(Integer,nullable=False)
    hyperdrive_rating =  Column(Float)
    MGLT =  Column(Integer,nullable=False)
    starship_class =  Column(String(200))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    model =  Column(String(250), nullable=False)
    manufacturer =  Column(String(250) )
    cost_in_credits =  Column(Float,nullable=False)
    length =  Column(Float,nullable=False )
    max_atmosphering_speed = Column(Integer,nullable=False)
    crew =  Column(String(250),nullable=False )
    passengers =  Column(Integer,nullable=False )
    cargo_capacity =  Column(Float,nullable=False)
    consumables =  Column(Integer,nullable=False)
    vehicle_class =  Column(String(200))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer,nullable=False)
    orbital_period = Column(Integer,nullable=False)
    diameter = Column(Float,nullable=False)
    climate = Column(String(50))
    gravity = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    population = Column(Integer,nullable=False)

class Colors(Base):
    __tablename__ = 'colors'
    id= Column(Integer, primary_key=True, autoincrement=True)
    color_Name = Column(String(50),unique=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    height = Column( nullable=False)
    colors = relationship(Colors)
    hair_color = Column(Integer, ForeignKey("colors.id"), nullable=False)
    skin_color = Column(Integer, ForeignKey("colors.id"), nullable=False)
    eye_color = Column(Integer, ForeignKey("colors.id"), nullable=False)
    birth_year = Column(DATE ,nullable=False)
    gender = Column(String(50), nullable=False)
    homeworld = Column(String(100), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer,ForeignKey("user.id"))
    user = relationship(User)

    id_characters = Column(Integer,ForeignKey("characters.id"))
    characters = relationship(Characters)

    id_starships = Column(Integer,ForeignKey("starShips.id"))
    starShips = relationship(StarShips)

    id_vehicles = Column(Integer,ForeignKey("vehicles.id"))
    vehicles = relationship(Vehicles)

    id_planets = Column(Integer,ForeignKey("planets.id"))
    planets = relationship(Planets)

    def to_dict(self):
        return {}
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
