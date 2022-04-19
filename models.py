from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class EmployeeModel(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer)
    emp_name = Column(String)

    def to_json(self):
        return {
            "emp_id": self.emp_id,
            "emp_name": self.emp_name
        }