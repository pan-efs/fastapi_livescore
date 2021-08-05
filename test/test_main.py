from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_score():
    """
    Score is 0-0 at initial step.
    """
    response = client.get(
        '/score',
    )
    assert response.status_code == 200
    assert response.json() == {
                            "away": 0,
                            "home": 0
                        }

def test_post_goal_home():
    """
    Messinho scores for home team.
    """
    response = client.post(
        '/goal',
        json={'player': 'messinho', 'team': 'home'}
    )
    assert response.status_code == 200
    assert response.json() == {
                            "away": 0,
                            "home": 1
                        }

def test_post_goal_away():
    """
    Ibrahimovic scores for away team.
    """
    response = client.post(
        '/goal',
        json={'player': 'ibrahimovic', 'team': 'away'}
    )
    assert response.status_code == 200
    assert response.json() == {
                            "away": 1,
                            "home": 1
                        }

def test_invalid_team_value():
    """
    Invalid team name.
    """
    response = client.post(
        '/goal',
        json={'player': 'matthieu', 'team': 'whoami'}
    )
    assert response.status_code == 422

def test_extra_optional_keys():
    """
    Provide more info related to goal but it returns only the score again.
    """
    response = client.post(
        '/goal',
        json={'player': 'panos', 'team': 'away', 'how_scored': 'penalty'}
    )
    assert response.status_code == 200
    assert response.json() == {
                            "away": 2,
                            "home": 1
                        }

def test_get_history():
    response = client.get(
        '/history'
    )
    assert response.status_code == 200
    assert response.json() == [
            {
            "away": 2,
            "home": 1
            },
            {
            "away": 1,
            "home": 1
            },
            {
            "away": 0,
            "home": 1
            },
            {
            "away": 0,
            "home": 0
            }
        ]

def test_reset_score():
    response = client.delete(
        '/reset'
    )
    assert response.status_code == 200
    assert response.json() == {
                            "away": 0,
                            "home": 0
                        }