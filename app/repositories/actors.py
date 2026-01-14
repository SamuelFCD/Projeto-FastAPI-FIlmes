from app.core import database


class ActorRepository:
    def __init__(self):
        self.db = database.pool
    
    async def get_actors(self):
        query = """
        SELECT 
            a.ator_id, 
            a.nome, 
            a.nacionalidade,
            ARRAY_REMOVE(ARRAY_AGG(f.titulo), NULL) as filmes_participados
        FROM atores a
        LEFT JOIN filme_ator fa ON a.ator_id = fa.ator_id
        LEFT JOIN filmes f ON fa.filme_id = f.filme_id
        GROUP BY a.ator_id, a.nome, a.nacionalidade
        ORDER BY a.nome;
        """
        conn = await self.get_connection()
        try:
            records = await conn.fetch(query)
            return records
        finally:
            await conn.close()

    async def create_actor(self, nome: str, nacionalidade: str):
        query = """
        INSERT INTO atores (nome, nacionalidade)
        VALUES ($1, $2)
        RETURNING ator_id, nome, nacionalidade
        """
        conn = await self.get_connection()
        try:
            record = await conn.fetchrow(query, nome, nacionalidade)
            return dict(record)
        finally:
            await conn.close()

    async def add_actor_to_film(self, ator_id: int, filme_id: int):
        """ if already exists, then return false """
        query = """
        INSERT INTO filme_ator (ator_id, filme_id)
        VALUES ($1, $2)
        """
        conn = await self.get_connection()
        try:
            await conn.execute(query, ator_id, filme_id)
            return True
        except asyncpg.UniqueViolationError:
            return False 
        finally:
            await conn.close()
