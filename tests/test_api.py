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
    print(f"DEBUG: result = {response}")

    
    assert len(data) == 8
    assert len(data[0]) == 8
    
    assert data[0][0]['type'] == 'rook'
    assert data[0][0]['color'] == 'black'
    assert data[0][0]['position'] == 'a8'
    
    assert data[6][4]["type"] == "pawn"
    assert data[6][4]["color"] == "white"
    assert data[6][4]["position"] == "e2"
    
def test_move_figure_should_return_200OK_and_update_board(client):
    # Schritt 1: Neues Spiel initialisieren
    response = client.post("/api/new_game")
    assert response.status_code == 200
    game_id = response.get_json()["gameId"]

    # Schritt 2: Bewegung vorbereiten (z. B. Bauer von e2 nach e4)
    move_payload = {
        "gameId": game_id,
        "figureId": None,  # Wird dynamisch gefunden
        "toPosition": "e4"
    }

    # Schritt 3: Aktuelle Board-Daten abrufen & die `figureId` von e2 holen
    response = client.get(f"/api/board?gameId={game_id}")
    assert response.status_code == 200
    board = response.get_json()

    # Finde den Bauern auf e2
    for row in board:
        for piece in row:
            if piece and piece["position"] == "e2" and piece["type"] == "pawn" and piece["color"] == "white":
                move_payload["figureId"] = piece["id"]

    assert move_payload["figureId"] is not None, "Kein gültiger Bauer auf e2 gefunden!"

    # Schritt 4: Bewegung testen
    response = client.post("/api/move", data=json.dumps(move_payload), content_type="application/json")
    assert response.status_code == 200, response.get_json()

    # Schritt 5: Neues Board abrufen & validieren
    response = client.get(f"/api/board?gameId={game_id}")
    assert response.status_code == 200
    new_board = response.get_json()

    # Prüfen, ob der Bauer jetzt auf e4 ist
    pawn_found = False
    for row in new_board:
        for piece in row:
            if piece and piece["position"] == "e4" and piece["type"] == "pawn" and piece["color"] == "white":
                pawn_found = True

    assert pawn_found, "Bauer wurde nicht erfolgreich nach e4 bewegt!"