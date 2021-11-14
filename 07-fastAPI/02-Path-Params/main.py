from fastapi import FastAPI

app = FastAPI()

@app.get("/coursename/{course_name}")
def read_course(course_name):
    return {"course_name": course_name}

@app.get("/courseid/{course_id}")
def read_course_id(course_id: int):
    return {"course_id": course_id}