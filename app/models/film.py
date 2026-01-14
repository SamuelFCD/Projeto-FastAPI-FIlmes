from datetime import datetime
from pydantic import (
    BaseModel, 
    Field,
    field_validator 
)
from typing import Optional, List

class Film(BaseModel):
    titulo: str = Field(min_length=1)
    genero: str = Field(min_length=1)
    ano: int
    diretor: str = Field(min_length=1)
    duracao_min: int
    
    @field_validator("titulo", "diretor", "genero")
    @classmethod
    def capitaliza_str(cls, value: str) -> str:
        return value.capitalize()
    
    @field_validator("ano", "duracao_min")
    @classmethod
    def validate_int_filds(cls, value: int) -> int:
        if value <= 0:
            raise ValueError(f"O Titulo e Duração têm que ser maior que 0")
        
        return value
    

class FilmResponse(Film):
    filme_id: int
    autor_nome: Optional[str] = None
    generos: Optional[str] = None
    elenco: Optional[List[str]] = []
