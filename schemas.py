from pydantic import BaseModel

class Employee(BaseModel):
    emp_name: str
    emp_id: int
