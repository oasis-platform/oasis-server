from pydantic import BaseModel
from pydantic.typing import Any, List
from sdgApp.Domain.job.job import JobAggregate, TaskEntity


class TaskDO(BaseModel):
    id: str
    name: str
    desc: str
    car_id: str
    car_name: str
    scenario_id: str
    scenario_name: str
    result: str
    job_id: str
    status: str
    replay_url: str = None
    retry_id: str = None
    cam_url: str = None
    scenario_param: dict = None
    car_snap: dict = None
    sensors_snap: dict = None
    start_time: str = None
    end_time: str = None


class JobDO(BaseModel):
    id: str
    name: str
    desc: str
    status: str = None
    start_time: str = None
    end_time: str = None
    usr_id: Any
    create_time: str = None
    last_modified: str
    task_list: List[TaskDO]

    def to_entity(self) -> JobAggregate:
        job_aggregate = JobAggregate(id=self.id,
                                     name=self.name,
                                     desc=self.desc,
                                     status=self.status,
                                     start_time=self.start_time,
                                     end_time=self.end_time)
        for task_DO in self.task_list:
            task = TaskEntity(id=task_DO.id,
                              name=task_DO.name,
                              desc=task_DO.desc,
                              car_id=task_DO.car_id,
                              car_name=task_DO.car_name ,
                              scenario_id=task_DO.scenario_id,
                              scenario_name=task_DO.scenario_name,
                              job_id=task_DO.job_id,
                              result=task_DO.result,
                              status=task_DO.status,
                              replay_url=task_DO.replay_url,
                              start_time=task_DO.start_time,
                              end_time=task_DO.end_time)
            job_aggregate.add_task(task)
        return job_aggregate

