from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import List
import schemas
from models import EmployeeModel
from schemas import Employee
from database import SessionLocal, engine
from crud import get_employees, add_employee, get_employee_id

app = FastAPI(
    title="HSBC Interview Test Swagger API",
    description="""
        Create employee and get all employees through restfull request
    """,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employee", response_model=schemas.Employee)
def create_employee(
        employee: Employee,
        db: Session = Depends(get_db)
):
    employee = add_employee(db, employee)
    return employee.to_json()


@app.get("/employees", response_model=List[
    schemas.Employee])
def get_all_employees(
        db: Session = Depends(get_db)
):
    employees = get_employees(db)
    return [employee.to_json() for employee in employees]


@app.get("/employee/{emp_id}", response_model=schemas.Employee)
def get_employee(
        emp_id: int,
        db: Session = Depends(get_db)
):
    employee = get_employee_id(db, emp_id)
    if employee:
        return employee.to_json()
    else:
        raise HTTPException(status_code=404, detail="No Employee Record Found.")
