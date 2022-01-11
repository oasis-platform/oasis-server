from sdgApp.Application.dynamic_scenes.CommandDTOs import ScenarioCreateDTO
from datetime import datetime
from typing import Union


class ScenarioReadDTO(ScenarioCreateDTO):
    id: str
    create_time: datetime
    last_modified: Union[None, datetime]
