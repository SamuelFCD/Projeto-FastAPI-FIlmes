from pydantic import BaseModel
from typing import List, Optional

class Actor(BaseModel):
    nome: str
    nacionalidade: str

class ActorResponse(Actor):
    ator_id: int
    filmes_participados: Optional[List[str]] = []
