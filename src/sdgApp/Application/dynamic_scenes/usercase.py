import shortuuid

from sdgApp.Application.car.usercase import split_page
from sdgApp.Application.dynamic_scenes.CommandDTOs import DynamicSceneCreateDTO, DynamicSceneUpdateDTO
from sdgApp.Application.dynamic_scenes.RespondsDTOs import DynamicSceneReadDTO
from sdgApp.Domain.dynamic_scenes.dynamic_scenes import DynamicScenesAggregate
from sdgApp.Infrastructure.MongoDB.dynamic_scene.dynamic_scene_repoImpl import DynamicSceneRepoImpl


class DynamicSceneCommandUsercase(object):

    def __init__(self, db_session, user, repo=DynamicSceneRepoImpl):
        self.repo = repo
        self.repo = self.repo(db_session, user)

    async def create_scenario(self, dynamic_scene_create_model: DynamicSceneCreateDTO):
        try:
            uuid = shortuuid.uuid()
            scenario = DynamicScenesAggregate(
                uuid,
                name=dynamic_scene_create_model.name,
                desc=dynamic_scene_create_model.desc,
                scene_script=dynamic_scene_create_model.scene_script,
                type=dynamic_scene_create_model.type)
            await self.repo.create_scenario(scenario)
        except:
            raise

    async def delete_scenario(self, dynamic_scene_id: str):
        try:
            await self.repo.delete_scenario_by_id(dynamic_scene_id)
        except:
            raise

    async def update_scenario(self, dynamic_scene_id: str, dynamic_scene_update_model: DynamicSceneUpdateDTO):
        try:
            scenario_retrieved = self.repo.get(dynamic_scene_id)
            scenario_retrieved.name = dynamic_scene_update_model.name
            scenario_retrieved.desc = dynamic_scene_update_model.desc
            scenario_retrieved.scene_script = dynamic_scene_update_model.scene_script
            scenario_retrieved.type = dynamic_scene_update_model.type
            await self.repo.update_scenario(dynamic_scene_id, scenario_retrieved)
        except:
            raise


class DynamicSceneQueryUsercase(object):

    def __init__(self, db_session, user):
        self.user = user
        self.db_session = db_session
        self.scenarios_collection = self.db_session['dynamic_scenes']

    async def find_specified_scenario(self, dynamic_scene_id: str):
        try:
            filter = {'id': dynamic_scene_id}
            filter.update({"usr_id": self.user.id})
            result_dict = await self.scenarios_collection.find_one(filter, {'_id': 0})
            response_dto = DynamicSceneReadDTO(**result_dict)
            return response_dto
        except:
            raise

    async def find_all_scenarios(self, p_num):
        try:
            response_dto_lst = []
            filter = {}
            filter.update({"usr_id": self.user.id})
            results_dict = self.scenarios_collection.find(filter, {'_id': 0}).sort([('last_modified', -1)])
            if results_dict:
                async for one_result in results_dict:
                    response_dto_lst.append(DynamicSceneReadDTO(**one_result))

                response_dto_lst = split_page(p_num, response_dto_lst)
                return response_dto_lst
        except:
            raise

