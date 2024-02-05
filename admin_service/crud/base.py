from typing import Generic, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

from admin_service.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


# TODO: REFACTOR THIS TO SQLALCHEMY 2.0
class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: str) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).one_or_none()

    def get_all(self, db: Session) -> list[ModelType]:
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, id: str, obj_in: UpdateSchemaType
    ) -> ModelType | None:
        db_obj = self.get(db=db, id=id)
        if not db_obj:
            return None

        for attr, value in obj_in.model_dump().items():
            setattr(db_obj, attr, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: str) -> ModelType:
        db_obj = self.get(db, id)
        db.delete(db_obj)
        db.commit()
        return db_obj
