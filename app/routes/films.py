
from fastapi import (
    APIRouter, 
    Depends, 
    status,
    HTTPException
)


from app.models.film import Film, FilmResponse
from app.repositories.films import FilmRepository

from typing import Annotated, List

router = APIRouter( 
    prefix="/films", # todos desse rota vão ter esse prefixo 
    tags=["Films"]
)

def get_film_repository() -> FilmRepository:
    return FilmRepository()

film_repository_dependency = Annotated[FilmRepository, Depends(get_film_repository)]


@router.get(
    "/",
    response_model= List[FilmResponse],
    status_code=status.HTTP_200_OK
)
async def get_films(service: film_repository_dependency):
    films = await service.get_films()
    
    return [FilmResponse(**dict(film)) for film in films]


@router.get(
    "/{film_id}",
    response_model=FilmResponse,
    status_code=status.HTTP_200_OK
)
async def get_film_by_id(
    service: film_repository_dependency, 
    film_id: int
):
    film = await service.get_film_by_id(film_id)
    
    if not film:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O Filme com o ID {film_id} não foi encontrado."
        )
    
    return FilmResponse(**dict(film))


@router.delete(
    "/{film_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_films(service: film_repository_dependency, film_id: int):
    if not await service.exists_by_id(film_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O Filme com o ID {film_id} não foi encontrado."
        )
    

    await service.delete_films(film_id)

    return {"message": f"O Filme {film_id} foi deletado com sucesso "}



@router.post("/", status_code=status.HTTP_201_CREATED) # verifica se algo foi criado no servidor 
async def create_film(
    service: film_repository_dependency,
    film: Film
):
    if await service.exists_by_name(film.titulo):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"O Filme com o título '{film.titulo}' já existe."
    )
        
    novo_filme = novo_filme = await service.create_film(
    titulo=film.titulo,
    ano=film.ano,
    genero=film.genero,
    diretor=film.diretor,
    duracao_min=film.duracao_min)

    return novo_filme

@router.put("/{film_id}")
async def update_film(
    service: film_repository_dependency,
    film_id:int, 
    film:Film
):
    if not await service.exists_by_id(film_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O Filme com o ID {film_id} não foi encontrado."
        )

    filme_atualizado = await service.update_film(film_id, *film.model_dump().values())

    return filme_atualizado

