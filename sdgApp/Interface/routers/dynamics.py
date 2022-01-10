from fastapi import APIRouter, status, Depends
from pydantic.typing import List

from sdgApp.Application.dynamics.CommandDTOs import DynamicsCreateDTO, DynamicsUpdateDTO
from sdgApp.Application.dynamics.RespondsDTOs import DynamicsGetDTO
from sdgApp.Application.dynamics.usercase import DynamicsCommandUsercase, DynamicsQueryUsercase
from sdgApp.Infrastructure.MongoDB.session_maker import get_db

router = APIRouter()



@router.post(
    "/dynamics",
    status_code=status.HTTP_201_CREATED,
    tags=["Dynamics"]
)
async def create_dynamics(dynamics_create_model: DynamicsCreateDTO, db = Depends(get_db)):
    try:
        DynamicsCommandUsercase(db_session=db).create_dynamics(dynamics_create_model)
    except:
        raise


@router.delete(
    "/dynamics/{dynamics_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Dynamics"]
)
async def delete_dynamics(dynamics_id:str, db = Depends(get_db)):
    try:
        DynamicsCommandUsercase(db_session=db).delete_dynamics(dynamics_id)
    except:
        raise


@router.put(
    "/dynamics/{dynamics_id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Dynamics"]
)
async def update_dynamics(dynamics_id:str, dynamics_update_model: DynamicsUpdateDTO, db = Depends(get_db)):
    try:
        DynamicsCommandUsercase(db_session=db).update_dynamics(dynamics_id, dynamics_update_model)
    except:
        raise


@router.get(
    "/dynamics/{dynamics_id}",
    status_code=status.HTTP_200_OK,
    response_model= DynamicsGetDTO,
    tags=["Dynamics"]
)
async def get_dynamics(dynamics_id:str, db = Depends(get_db)):
    try:
        dynamics_dto = DynamicsQueryUsercase(db_session=db).get_dynamics(dynamics_id)
        return dynamics_dto
    except:
        raise


@router.get(
    "/dynamics",
    status_code=status.HTTP_200_OK,
    response_model= List[DynamicsGetDTO],
    tags=["Dynamics"]
)
async def list_dynamics(db = Depends(get_db)):
    try:
        dynamics_dto_lst = DynamicsQueryUsercase(db_session=db).list_dynamics()
        return dynamics_dto_lst
    except:
        raise

