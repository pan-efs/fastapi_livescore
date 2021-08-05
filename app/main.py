from app.schemas.schemas import (Goal, Score)
from app.models.db import DequeDB

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import (FastAPI, HTTPException)

#Initialize fastapi instance
app = FastAPI()

#Initialize DequeDB and the score as 0-0.
db = DequeDB()
db.appendleft(Score())

#REST Operations
@app.post(
    '/goal',
    response_model=Score,
    status_code=200,
    description='Update the score.',
    tags = ['Live Score']
)
def post_goal(goal: Goal):
    if goal.team=='home':
        return db.update_home_score()
    
    elif goal.team=='away':
        return db.update_away_score()
    
    else:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY)

@app.get(
    '/score',
    response_model=Score,
    status_code=200,
    description='Get current score.',
    tags = ['Live Score']
)
def get_score():
    return db.get_current_score()

@app.get(
    '/history',
    response_model=list,
    status_code=200,
    description='Get score history of the game.',
    tags = ['Live Score']
)
def get_history():
    return list(db)

@app.delete(
    '/reset',
    response_model=Score,
    status_code=200,
    description='Reset score as 0-0.',
    tags = ['Live Score']
)
def reset_score():
    return db.reset_score()