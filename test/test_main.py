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

def test_get_first_score():
    """
    Score should be 0-1.
    """
    response = client.get(
        '/score',
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

def test_get_score_again():
    """
    Score should be 1-1.
    """
    response = client.get(
        '/score',
    )
    assert response.status_code == 200
    assert response.json() == {
                            "away": 1,
                            "home": 1
                        }

def test_score_is_zero_again():
    """
    User set 0-0 the score table providing '-1' to 'player' key.
    """
    response = client.post(
        '/goal',
        json={'player': '-1', 'team': 'away'}
    )
    assert response.status_code == 200
    assert response.json() == {
                            "away": 0,
                            "home": 0
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
                            "away": 1,
                            "home": 0
                        }

def test_a_sequence_of_events():
    """
    Set 0-0 -> Away scores -> Get score -> Set 0-0 -> Invalid team name -> Home scores.
    """
    initial = client.post(
        '/goal',
        json={'player': '-1', 'team': 'away'}
    )
    assert initial.status_code == 200
    assert initial.json() == {
                            "away": 0,
                            "home": 0,
    }
    response = client.post(
        '/goal',
        json={'player': 'panos', 'team': 'away'}
    )
    assert response.json() == {
                            "away": 1,
                            "home": 0
                        }
    response_one = client.get(
        '/score',
    )
    assert  response_one.json() == {
                            "away": 1,
                            "home": 0
    }
    response_two = client.post(
        '/goal',
        json={'player': '-1', 'team': 'away'}
    )
    assert  response_two.json() == {
                            "away": 0,
                            "home": 0
    }
    response_three = client.post(
        '/goal',
        json={'player': 'panagiotis', 'team': 'dontknow'}
    )
    assert response_three.status_code == 422
    response_four = client.post(
        '/goal',
        json={'player': 'berg', 'team': 'home'}
    )
    assert  response_four.json() == {
                            "away": 0,
                            "home": 1
    }