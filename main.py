from fastapi import FastAPI

from contextlib import asynccontextmanager # o que fazer quando a api inicia/finaliza,Sem isso, não teria como garantir que o banco conecta antes das rotas rodarem.

from app.core import database
from app.routes.films import router as films_router

@asynccontextmanager
async def lifespan(app: FastAPI): # controlar o ciclo de vida da aplicação 

    await database.connect_db()
    print("Aplicação iniciada.")

    yield # Antes - quando a API liga ; Depois - quando a API Desliga | Quando para o servidor (Ctrl + C), ele volta pro código depois do yield e executa o disconnect | Sem isso, a conexão pode não fechar 

    await database.desconnect_db()
    print("Aplicação finalizada.")

app = FastAPI(lifespan=lifespan) # gerenciadora da vida da aplicação.

@app.get("/")
async def test_connection():
    return {"message": "A aplicação está rodando!"}


app.include_router(prefix="/api",
                   router=films_router
                ) # prefixo + junta as rotas no app principal

