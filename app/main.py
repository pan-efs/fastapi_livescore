from app.schemas.schemas import (Goal, Score)
from app.models.db import DequeDB

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import (FastAPI, HTTPException)

#Initialize fastapi instance
app = FastAPI()

#Initialize DequeDB and the score as 0-0.
score = Score()
db = DequeDB()
db.appendleft(score)

#REST Operations
@app.post(
    '/goal',
    response_model=Score,
    status_code=200,
    description='Update the score. Set 0-0 providing "-1" value to "player" key.',
    tags = ['Live Score']
)
def post_goal(goal: Goal):
    if goal:
        if goal.player=='-1':
            score.away = 0
            score.home = 0
            
            db.clear_db() #length==0
            return db.update_score(score)
        
        if goal.team=='home':
            score.home = score.home + 1
            return db.update_score(score)
        
        elif goal.team=='away':
            score.away = score.away + 1
            return db.update_score(score)
    
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