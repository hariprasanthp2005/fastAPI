from fastapi import APIRouter
from models.emp import Employee
from pymongo import MongoClient
from fastapi import HTTPException

#create employee router
router=APIRouter(prefix='/emp')

#establish the db connection
client=MongoClient('mongodb://localhost:27017/')
db=client['dbtwo']
emp_col=db['employees']

'''
Usage:create new employee
Rest API URL: http://127.0.0.1:8000/emp/create
Method Type:POST
Required Fields:eid ename esal gender
Access Type:public
'''
@router.post('/create')
def create_emp(emp:Employee):
    emp_col.insert_one(emp.dict())
    return{"msg":"employee data created successfully"}

'''
Usage:create new employee
Rest API URL: http://127.0.0.1:8000/emp/read
Method Type:GET
Required Fields:None
Access Type:public
'''    
@router.get('/read')
def read_emp():
    employees = list (emp_col.find({},{'_id':0}))
    return employees

'''
Usage:create new employee
Rest API URL: http://127.0.0.1:8000/emp/read
Method Type:GET
Required Fields:None
Access Type:public
'''    
@router.get('/read/{eid}')
def read_emp_by_id(eid:int):
    employee=emp_col.find_one({'eid':eid},{'_id':0})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee
    



       