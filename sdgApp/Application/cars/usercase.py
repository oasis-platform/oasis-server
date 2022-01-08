from sdgApp.Application.cars.CommandDTOs import CarCreateDTO, CarUpdateDTO
from sdgApp.Domain.cars.cars import CarsAggregate
from sdgApp.Infrastructure.MongoDB.car.car_repoImpl import CarRepoImpl
import shortuuid
from fastapi import Depends
from collections import OrderedDict

def DTO_assembler(car: CarsAggregate):
    return car.shortcut_DO

class CarCommandUsercase(object):

    def __init__(self, db_session, repo=CarRepoImpl):
        self.repo = repo
        self.repo = self.repo(db_session)

    def create_car(self, dto: CarCreateDTO):
        try:
            uuid = shortuuid.uuid()
            car_dict = dto.dict()
            car = CarsAggregate(uuid,
                                name=car_dict["name"],
                                desc=car_dict["desc"],
                                autosys=car_dict["autosys"],
                                model=car_dict["model"],
                                physics=car_dict["physics"],
                                wheels=car_dict["wheels"],
                                sensors=car_dict["sensors"])
            self.repo.create(car)
        except:
            raise

    def delete_car(self, car_id: str):
        try:
            self.repo.delete(car_id)
        except:
            raise

    def update_car(self, car_id:str, dto: CarUpdateDTO):
        try:
            car_update_dict = dto.dict()
            update_car = CarsAggregate(car_id,
                                       name=car_update_dict["name"],
                                       desc=car_update_dict["desc"],
                                       autosys=car_update_dict["autosys"],
                                       model=car_update_dict["model"],
                                       physics=car_update_dict["physics"],
                                       wheels=car_update_dict["wheels"],
                                       sensors=car_update_dict["sensors"])
            self.repo.update(update_car)
        except:
            raise


class CarQueryUsercase(object):

    def __init__(self, db_session, repo=CarRepoImpl):
        self.repo = repo
        self.repo = self.repo(db_session)

    def get_car(self, car_id:str):
        try:
            car = self.repo.get(car_id)
            response_dto = DTO_assembler(car)
            return response_dto
        except:
            raise

    def list_car(self):
        try:
            response_dto_lst = []
            car_lst = self.repo.list()
            for car in car_lst:
                response_dto = DTO_assembler(car)
                response_dto_lst.append(response_dto)
            return response_dto_lst
        except:
            raise

