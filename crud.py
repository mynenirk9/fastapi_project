from sqlalchemy.orm import Session

import models, schemas


def get_employee_id(db: Session, emp_id=int):
    return db.query(models.EmployeeModel).filter(models.EmployeeModel.emp_id == emp_id).first()


def get_employees(db: Session):
    return db.query(models.EmployeeModel).all()


def add_employee(db: Session, item: schemas.Employee):
    db_item = models.EmployeeModel(**item.dict())
    db.add(db_item)
    db.commit()
    return db_item
