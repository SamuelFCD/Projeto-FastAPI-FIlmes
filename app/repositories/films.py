from app.core import database


class FilmRepository:
    def __init__(self):
        self.db = database.pool
        
    async def exists_by_name(self, titulo: str) -> bool:
        query = "SELECT EXISTS(SELECT 1 FROM filmes WHERE titulo = $1);"

        result = await self.db.fetchval(query, titulo)

        return result
    
    async def exists_by_id(self, film_id: int) -> bool:
        print("validador")
        query = "SELECT 1 FROM filmes WHERE filme_id = $1;"

        result = await self.db.fetchval(query, film_id)
        
    

        return result is not None
    
    
    async def get_films(self):

        query = "SELECT * FROM filmes;"

        result = await self.db.fetch(query=query)

        return result

    async def delete_films(self, film_id:int):

        query = "DELETE FROM filmes WHERE filme_id = $1"

        result = await self.db.execute(query, film_id)

        return result

    async def create_film(self, titulo:str, genero:str, ano:int, diretor: str, duracao_min: int):

        query = "INSERT INTO filmes (titulo, genero, ano, diretor, duracao_min) VALUES ($1, $2, $3, $4, $5) RETURNING * "

        return await self.db.fetchrow(query, titulo, genero, ano, diretor, duracao_min)


    async def update_film(self, filme_id:int, titulo:str, genero:str, ano:int, diretor: str, duracao_min: int):

        query = "UPDATE filmes SET titulo = $1, genero = $2, ano = $3, diretor = $4, duracao_min = $5 WHERE filme_id = $6 RETURNING *"

        return await self.db.fetchrow(query, titulo, genero, ano, diretor, duracao_min, filme_id)
