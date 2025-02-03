import pytest
from chess_game import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
def test_get_board_should_return_200OK_and_true_for_some_figures(client):
    response = client.get('api/board')
    
    assert response.status_code == 200
    data = response.get_json()
    
    assert len(data) == 8
    assert len(data[0]) == 8
    
    assert data[0][0]['type'] == 'Turm'
    assert data[0][0]['color'] == 'black'
    assert data[0][0]['position'] == 'a8'
    
    assert data[6][4]["type"] == "Bauer"
    assert data[6][4]["color"] == "white"
    assert data[6][4]["position"] == "e2"