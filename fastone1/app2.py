from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Hari", "age": 21},
    2: {"name": "Ravi", "age": 22}
}

@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students[student_id]


@app.post("/students/{student_id}")
def add_student(student_id: int, name: str, age: int):
    students[student_id] = {
        "name": name,
        "age": age
    }
    return {"message": "Student added"}


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int):
    students[student_id] = {
        "name": name,
        "age": age
    }
    return {"message": "Student updated"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    del students[student_id]
    return {"message": "Student deleted"}