
from app.core import database

async def get_films():

    query = "SELECT * FROM filmes;"

    result = await database.pool.fetch(query=query)

    return result

async def delete_films(film_id:int):

    query = "DELETE FROM filmes WHERE filme_id = $1"

    result = await database.pool.execute(query, film_id)

    return result

async def create_film(titulo:str, genero:str, ano:int, diretor: str, duracao_min: int):

    query = "INSERT INTO filmes (titulo, genero, ano, diretor, duracao_min) VALUES ($1, $2, $3, $4, $5) RETURNING * "

    return await database.pool.fetchrow(query, titulo, genero, ano, diretor, duracao_min)


async def update_film(filme_id:int, titulo:str, genero:str, ano:int, diretor: str, duracao_min: int):

    query = "UPDATE filmes SET titulo = $1, genero = $2, ano = $3, diretor = $4, duracao_min = $5 WHERE filme_id = $6 RETURNING *"

    return await database.pool.fetchrow(query, titulo, genero, ano, diretor, duracao_min, filme_id)
