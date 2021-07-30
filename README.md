# `Signality Assignment` :sunglasses:

### Info & Prep
The project is built with python=3.9.6 version on Windows 10 OS.

You can clone the project from GitHub using your desired IDE.
### Build and run docker
Build: `docker-compose up -d`

Existence: `docker images`, [optional]

Check status: `docker ps`, [optional]

Stop: `docker stop {container id}`

### Interact with FastAPI
`Option 1:` Open your desired browser (e.g. Google Chrome) and write `http://localhost:8000/docs`.
An interactive version of REST API will render on your screen.

`Option 2:` Via terminal write the command `python`, then you should see the symbol `>>>`.
Then, you can provide a virtual scenario as below, in order to perceive the philoshopy of REST API.

```diff
# import requests
! requests.get('http://localhost:8000/score').text, get score!
! requests.post('http://localhost:8000/goal', json={'player':'rhodinho', 'team':'away'}).text, post goal!
requests.post('http://localhost:8000/goal', json={'player':'berginho', 'team':'home'}).text
! requests.post('http://localhost:8000/goal', json={'player':'-1', 'team':'home'}).text, set score as 0-0!
requests.get('http://localhost:8000/score').text
requests.post('http://localhost:8000/goal', json={'team':'home'}).text
requests.post('http://localhost:8000/goal', json={'team':'home'}).text
requests.post('http://localhost:8000/goal', json={'team':'home'}).text
requests.post('http://localhost:8000/goal', json={'team':'home'}).text
requests.get('http://localhost:8000/score').text
- requests.post('http://localhost:8000/goal', json={'team':'sweden'}).text, error!
```
