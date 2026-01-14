from fastapi import (
    APIRouter, 
    Depends, 
    status,
    HTTPException
)
from typing import Annotated, List
from app.models.actors import Actor, ActorResponse
from app.repositories.actors import ActorRepository

router = APIRouter( 
    prefix="/actors", 
    tags=["Actors"]
)

def get_actor_repository() -> ActorRepository:
    return ActorRepository()

actor_repository_dependency = Annotated[ActorRepository, Depends(get_actor_repository)]

@router.get(
    "/",
    response_model=List[ActorResponse],
    status_code=status.HTTP_200_OK
)
async def get_actors(service: actor_repository_dependency):
    actors = await service.get_actors()
    return [ActorResponse(**dict(actor)) for actor in actors]

@router.get(
    "/{actor_id}",
    response_model=ActorResponse,
    status_code=status.HTTP_200_OK
)
async def get_actor_by_id(
    service: actor_repository_dependency, 
    actor_id: int
):
    actor = await service.get_actor_by_id(actor_id)
    
    if not actor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O Ator com o ID {actor_id} não foi encontrado."
        )
    
    return ActorResponse(**dict(actor))

@router.post(
    "/", 
    status_code=status.HTTP_201_CREATED,
    response_model=ActorResponse
) 
async def create_actor(
    service: actor_repository_dependency,
    actor: Actor
):        
    novo_ator = await service.create_actor(**actor.model_dump())
    return ActorResponse(**dict(novo_ator))

@router.put(
    "/{actor_id}",
    response_model=ActorResponse
)
async def update_actor(
    service: actor_repository_dependency,
    actor_id: int, 
    actor: Actor
):
    if not await service.exists_by_id(actor_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O Ator com o ID {actor_id} não foi encontrado."
        )

    ator_atualizado = await service.update_actor(actor_id, **actor.model_dump())
    return ActorResponse(**dict(ator_atualizado))

@router.delete(
    "/{actor_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_actor(
    service: actor_repository_dependency, 
    actor_id: int
):
    if not await service.exists_by_id(actor_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"O Ator com o ID {actor_id} não foi encontrado."
        )
    
    await service.delete_actor(actor_id)







