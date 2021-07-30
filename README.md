# `Signality Assignment` :sunglasses:

### Info & Prep
The project is built with python=3.9.6 version on Windows 10 OS.

You can clone the project from GitHub using your desired IDE.

Get docker from [here.](https://docs.docker.com/get-docker/)
### Build and run docker
Open your terminal at the root of project directory. Following the below commands you can build and run the project.

Build: `docker-compose up -d`

Existence: `docker images`, [optional]

Check status: `docker ps`, [optional]

Stop: `docker stop {container id}`

### Interact with Live Score API
`Option 1:` Open your desired browser (e.g. Google Chrome) and write `http://localhost:8000/docs`.
An interactive version of REST API will render on your screen.

`Option 2:` Via terminal write the command `python`, then you should see the symbol `>>>`.
Then, you can provide a virtual scenario as below, in order to perceive the philoshopy of Live Score API.

```diff
# import requests
! requests.get('http://localhost:8000/score').text, GET SCORE!
! requests.post('http://localhost:8000/goal', json={'player':'rhodinho', 'team':'away'}).text, POST GOAL!
  requests.post('http://localhost:8000/goal', json={'player':'berginho', 'team':'home'}).text
! requests.post('http://localhost:8000/goal', json={'player':'-1', 'team':'home'}).text, SET SCORE AS 0-0!
  requests.get('http://localhost:8000/score').text
  requests.post('http://localhost:8000/goal', json={'team':'home'}).text
  requests.post('http://localhost:8000/goal', json={'team':'home'}).text
  requests.post('http://localhost:8000/goal', json={'team':'home'}).text
  requests.post('http://localhost:8000/goal', json={'team':'home'}).text
  requests.get('http://localhost:8000/score').text
- requests.post('http://localhost:8000/goal', json={'team':'sweden'}).text, ERROR!
```

### Run tests
Navigate to root project directory and provide the command `pytest`.