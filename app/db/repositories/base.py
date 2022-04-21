from typing import Any, Dict, Generic, Optional, Type, TypeVar, Union, List

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from db.session import SessionLocal


ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepo(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def get(self, id_in: Any) -> Optional[ModelType]:
        with SessionLocal() as db:
            domain_obj = db.query(self.model).filter(self.model.id == id_in).first()
        return domain_obj

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        domain_obj = self.model(**obj_in_data)
        with SessionLocal() as db:
            db.add(domain_obj)
            db.commit()
            db.refresh(domain_obj)
        return domain_obj

    def update(self, domain_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        obj_data = jsonable_encoder(domain_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(domain_obj, field, update_data[field])
        with SessionLocal() as db:
            db.add(domain_obj)
            db.commit()
            db.refresh(domain_obj)
        return domain_obj

    def delete(self, id_in: int) -> ModelType:
        with SessionLocal() as db:
            obj = db.query(self.model).get(id_in)
            db.delete(obj)
            db.commit()
        return obj
