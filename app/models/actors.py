from pydantic import BaseModel
from typing import List, Optional

class Actor(BaseModel):
    nome: str
    nacionalidade: str

class ActorResponse(Actor):
    actor_id: int
    actor_filmes: Optional[List[str]] = []
