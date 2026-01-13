
from fastapi import APIRouter

from app.repositories import films as films_repository

from pydantic import BaseModel

router = APIRouter(
    prefix="/films", # todos desse rota vão ter esse prefixo 
    tags=["films"]
)

@router.get("/")

async def get_films():

    return await films_repository.get_films()

@router.delete("/{film_id}")
async def delete_films(film_id: int):

    await films_repository.delete_films(film_id)

    return {"message": f"O Filme {film_id} foi deletado com sucesso "}

class CreateFilm(BaseModel):
    titulo:str
    genero:str
    ano:int
    diretor:str
    duracao_min:int

@router.post("/", status_code=201) # verifica se algo foi criado no servidor 
async def create_film(film: CreateFilm):

    novo_filme = await films_repository.create_film(film.titulo, film.genero, film.ano, film.diretor, film.duracao_min)

    return novo_filme

@router.put("/{film_id}")

async def update_film(film_id:int, film:CreateFilm):

    filme_atualizado = await films_repository.update_film(film_id, film.titulo, film.genero, film.ano, film.diretor, film.duracao_min)

    return filme_atualizado