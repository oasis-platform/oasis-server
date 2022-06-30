from datetime import datetime
from typing import Union, Any, Optional
from sdgApp.Application.scenarios.CommandDTOs import ScenarioCreateDTO
from pydantic import BaseModel
from pydantic.typing import List


class ScenariosReadDTO(ScenarioCreateDTO):
   id: str
   create_time: Union[None, datetime]
   last_modified: Union[None, datetime]
   types: str
   parent_id: Any


class ScenariosResponse(BaseModel):
   total_num: int
   total_page_num: int
   datas: List[ScenariosReadDTO]

class ScenarioGroupReadMapDTO(BaseModel):
   map_name: Optional[str]

class ScenarioGroupReadDTO(BaseModel):
   id: str
   name: str
   tags: List
   types: str
   scenario_param: Optional[ScenarioGroupReadMapDTO]
   last_modified: Union[None, datetime]

