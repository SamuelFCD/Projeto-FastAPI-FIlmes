from pydantic import BaseModel

class Film(BaseModel):
    titulo: str
    genero: str
    diretor: str
    
    duracao_min: int
    ano: int
    