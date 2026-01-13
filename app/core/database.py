import asyncpg

pool: asyncpg.Pool | None = None

async def connect_db():
    global pool

    try:
        pool = await asyncpg.create_pool(
            user="postgres",
            password="123",
            database="Filmes",
            host="localhost",
            port="5432",
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