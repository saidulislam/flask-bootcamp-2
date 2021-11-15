from typing import Optional
from fastapi import FastAPI

app = FastAPI()

course_items = [{"course_name": "Python"}, {"course_name": "NodeJS"}, {"course_name": "Machine Learning"}]

@app.get("/courses/")
def read_courses(start: int = 0, end: int = 10):
    return course_items[start : start+end]

# http://127.0.0.1:8000/courses/?start=1&end=2
# [{"course_name":"NodeJS"},{"course_name":"Machine Learning"}]

@app.get("/courses/{course_id}")
def read_courses_by_id(course_id: int, q: Optional[str] = None):
    if q is not None:
        return {"course_name": course_items[course_id], "q": q}
    return {"course_name": course_items[course_id]}

# http://127.0.0.1:8000/courses/1?q=1234
# {"course_name":{"course_name":"NodeJS"},"q":"1234"}