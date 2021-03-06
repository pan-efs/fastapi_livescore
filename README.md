# `Live Score` :sunglasses:

### Info & Prep
The project is built with python=3.9.6 version.

Initialize the project using your desired IDE if you wish.

Get docker from [here.](https://docs.docker.com/get-docker/)

### Run web server and develop simultaneously
Navigate to the root project directory and provide the command `uvicorn app.main:app --reload`.
Modifications take place automatically at the same time.
### Build and run docker
Open your terminal at the root of the project directory. Following the below commands you can build and run the project.

Build & Run: `docker-compose up -d`

Existence: `docker images`, [optional]

Check status: `docker ps`, [optional]

Stop: `docker stop {container id}`

If you want to rebuild docker container at any time, type: `docker-compose up -d --no-deps --build`.

### Interact with Live Score API
`Option 1:` Open your desired browser (e.g. Google Chrome) and write `http://localhost:8000/docs`.
An interactive version of REST API will render on your screen.

`Option 2:` Via terminal write the command `python`, then you should see the symbol `>>>`.
Then, you can provide a virtual scenario line by line as below, in order to perceive the philosophy of Live Score API.

```diff
# import requests
! requests.get('http://localhost:8000/score').text, GET SCORE!
! requests.post('http://localhost:8000/goal', json={'player':'rhodinho', 'team':'away'}).text, POST GOAL!
  requests.post('http://localhost:8000/goal', json={'player':'berginho', 'team':'home'}).text
! requests.get('http://localhost:8000/history').text, GET HISTORY!
! requests.delete('http://localhost:8000/reset').text, RESET SCORE!
- requests.post('http://localhost:8000/goal', json={'team':'sweden'}).text, ERROR!
```

### Run tests
Navigate to the root project directory and provide the command `pytest`.