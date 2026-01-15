import asyncpg
import os

from dotenv import load_dotenv
load_dotenv()

pool: asyncpg.Pool | None = None

async def connect_db():
    global pool

    try:
        # Get port with error handling
        try:
            port = int(os.getenv("DB_PORT", "5432"))
        except ValueError:
            port = 5432
        
        pool = await asyncpg.create_pool(
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "filmes"),
            host=os.getenv("DB_HOST", "localhost"),
            port=port,
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