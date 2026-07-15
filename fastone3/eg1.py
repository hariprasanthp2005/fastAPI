from fastapi import FastAPI, HTTPException

app = FastAPI()

candidates = [
    {
        "id": 1,
        "name": "Hari",
        "skill": "Python",
        "experience": 0,
        "location": "Bangalore"
    }
]

@app.get("/")
def home():
    return {"message": "Job Portal API"}

@app.get("/candidates")
def get_candidates():
    return candidates

@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int):

    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate

    raise HTTPException(
        status_code=404,
        detail="Candidate not found"
    )

@app.post("/candidates")
def add_candidate(candidate: dict):

    candidates.append(candidate)

    return {
        "message": "Candidate added successfully",
        "candidate": candidate
    }

@app.put("/candidates/{candidate_id}")
def update_candidate(candidate_id: int, updated_data: dict):

    for candidate in candidates:

        if candidate["id"] == candidate_id:

            candidate.update(updated_data)

            return {
                "message": "Candidate updated",
                "candidate": candidate
            }

    raise HTTPException(
        status_code=404,
        detail="Candidate not found"
    )

@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int):

    for candidate in candidates:

        if candidate["id"] == candidate_id:

            candidates.remove(candidate)

            return {
                "message": "Candidate deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Candidate not found"
    )

@app.get("/search/{skill}")
def search_by_skill(skill: str):

    result = []

    for candidate in candidates:
        if candidate["skill"].lower() == skill.lower():
            result.append(candidate)

    return result