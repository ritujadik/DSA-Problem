
def crud_operation(json_var,operation,emp_id=None,emp_name=None,emp_dept=None,emp_design=None):
    if operation == "create":
        if emp_id and emp_name:
            new_emp={
                "emp_id":emp_id,
                "emp_name":emp_name,
                "emp_dept":emp_dept,
                "emp_design":emp_design
            }
            json_var.append(new_emp)
            return f"employee {emp_name} added successfully"

    elif operation == "read":
            if emp_id:
                for emp in json_var:
                    if emp["emp_id"] == emp_id:
                        return emp
                return f"Employee with {emp_id} not found"


    elif operation == "update":
            if emp_id:
                for emp in json_var:
                    if emp["emp_id"] == emp_id:
                        if emp_name:
                            emp["emp_name"] = emp_name
                        if emp_dept:
                            emp["emp_dept"] = emp_dept
                        if emp_design:
                            emp["emp_design"] = emp_design

                        return f"Employee with ID {emp_id} updated successfully"

                return f"Employee with ID {emp_id} not found"

    elif operation == "delete":
        if emp_id:
            for emp in json_var:
                if emp["emp_id"] == emp_id:
                    json_var.remove(emp)
                    return f"Employee with ID {emp_id} deleted successfully"
            return f"Employee with ID {emp_id} does not exist"

    return "Invalid Operation"


json_var = [{
    "emp_id":2,
    "emp_name":"Ritu",
    "emp_dept": "IT",
    "emp_design":"Executive"
}]

print(crud_operation(json_var,"create",emp_id=3,emp_name="rahul",emp_dept="IT",emp_design="Executive"))
print(crud_operation(json_var,"read",emp_id=2))
print(crud_operation(json_var, "update", emp_id=3, emp_name="John Doe", emp_dept="Finance", emp_design="Senior Analyst"))
print(crud_operation(json_var,"delete",emp_id=3))



class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def make_sound(self):
        return "some generic animal sound"

    def display_animal(self):
        return f"This is {self.name}, a {self.type}."

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,"Dog")

    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name,"Cat")

    def make_sound(self):
        return "Meow"


animals = [Dog("Jennie"),Cat("Jimmie")]
for animal in animals:
    print(animal.display_animal())
    print("Sound:",animal.make_sound())

#simple api for signup
from fastapi import FastAPI,Request,http
from pydantic import BaseModel,EmailStr
from fastapi.responses import JSONResponse

App = FastAPI()

class registerRequest(BaseModel):
    mobile:str
    email:EmailStr
    password:str


@app.post('/register')
def signup(user:registerRequest):
    if len(mobile) !=10 or not user.mobile.isdigit():
        return JSONResponse(
            status_code=400,
            content={
                "status":"error",
                "message":"please enter a valid mobile number"
        }
        )
    if len(user.password)<8:
        return JSONResponse(
            status_code=400,
            content={
                "status":"error",
                "message":"password should be 8 digit atleast"
            }
        )

    return {
        "status_code":200,
        "status":"success"
        
    }

