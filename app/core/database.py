import asyncpg
import os

pool: asyncpg.Pool | None = None

async def connect_db():
    global pool

    try:
        pool = await asyncpg.create_pool(
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "123"),
            database=os.getenv("DB_NAME", "Filmes"),
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "5432")),
            min_size=1
        )

        print("Conexão com o banco de dados estabelecida com sucesso.")

    except Exception as Error:
        print("Erro ao conectar ao banco de dados:", Error)

async def desconnect_db():

    global pool

    if pool:

        await pool.close()
        
        print("Conexão com o banco de dados encerrada com sucesso.")