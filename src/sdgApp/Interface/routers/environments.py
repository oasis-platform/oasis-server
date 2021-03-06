from sdgApp.Application.environments.RespondsDTOs import EnvReadDTO, EnvsResponse
from sdgApp.Application.environments.CommandDTOs import EnvCreateDTO, EnvUpdateDTO
from sdgApp.Application.environments.usercase import EnvCommandUsercase, EnvQueryUsercase
from sdgApp.Infrastructure.MongoDB.session_maker import get_db
from fastapi import APIRouter, status, Depends
from sdgApp.Interface.FastapiUsers.users_model import UserDB
from sdgApp.Interface.FastapiUsers.manager import current_active_user
from typing import List
from sdgApp.Application.log.usercase import except_logger
router = APIRouter()


@router.post(
    "/environments",
    status_code=status.HTTP_201_CREATED,
    response_model=EnvReadDTO,
    tags=["Envs"]
)
@except_logger("creat_env failed .....................")
async def creat_env(env_create_model: EnvCreateDTO, db=Depends(get_db),
                    user: UserDB = Depends(current_active_user)):
    try:
        await EnvCommandUsercase(db_session=db, user=user).create_env(env_create_model)
    except:
        raise


@router.delete("/environments/{env_ids}",
               status_code=status.HTTP_202_ACCEPTED,
               tags=["Envs"])
@except_logger("delete_env failed .....................")
async def delete_env(env_ids: str, db=Depends(get_db), user: UserDB = Depends(current_active_user)):
    try:
        await EnvCommandUsercase(db_session=db, user=user).delete_env(env_ids)
    except:
        raise


@router.put(
    "/environments/{env_id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=EnvReadDTO,
    tags=["Envs"]
)
@except_logger("update_env failed .....................")
async def update_env(env_id: str, env_update_model: EnvUpdateDTO, db=Depends(get_db),
                     user: UserDB = Depends(current_active_user)):
    try:
        await EnvCommandUsercase(db_session=db, user=user).update_env(env_id, env_update_model)
    except:
        raise

@router.get(
    "/environments/{env_id}",
    status_code=status.HTTP_200_OK,
    response_model=EnvReadDTO,
    tags=["Envs"]
)
@except_logger("find_specified_env failed .....................")
async def find_specified_env(env_id: str, db=Depends(get_db),
                             user: UserDB = Depends(current_active_user)):
    try:
        return await EnvQueryUsercase(db_session=db, user=user).find_specified_env(env_id)
    except:
        raise


@router.get(
    "/environments",
    status_code=status.HTTP_200_OK,
    response_model=EnvsResponse,
    tags=["Envs"]
)
@except_logger("find_all_envs failed .....................")
async def find_all_envs(content: str = '', p_size: int = 15, p_num: int = 1, db=Depends(get_db), user: UserDB = Depends(current_active_user)):
    try:
        return await EnvQueryUsercase(db_session=db, user=user).find_all_envs(p_num, p_size, content)
    except:
        raise



