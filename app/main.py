import collections

from app.schemas import (Goal, Score)

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import (FastAPI, HTTPException)

#Initialize fastapi instance
app = FastAPI()

#Initialize deque data structure and the score as 0-0.
score = Score()
db = collections.deque['Score']()
db.appendleft(score)

#REST Operations
@app.post(
    '/goal',
    response_model=Score,
    status_code=200,
    description='Update the score. If you want 0-0, give "-1" value to "player" key.',
    tags = ['Live Score']
)
def post_goal(goal: Goal):
    if goal and goal.player=='-1':
        score.away = 0
        score.home = 0
        
        db.clear() #length==0
        db.appendleft(score)
        return db[0]
    
    if goal and goal.team=='home':
        score.home = score.home + 1
        
        db.appendleft(score)
        return db[0]
    
    elif goal and goal.team=='away':
        score.away = score.away + 1
        
        db.appendleft(score)
        return db[0]
    
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
    return db[0]