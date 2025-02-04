# Projektbeschreibung

## Projektname
Chess App

English below

---

## Projektziel
Das Ziel ist die Entwicklung eines Schachspiels mit vollständiger Spiellogik, das sowohl die grundlegenden als auch die komplexeren Regeln des Spiels abbildet. Es soll bewusst auf die Verwendung von bestehenden Bibliotheken verzichtet werden, die Schachregeln und -abläufe bereits vorgeben.

---

## Entwicklungsschritte

### Konzeptionierung 
Auch wenn in diesem Projekt primär die Entwicklung der Programmlogik im Vordergrund steht und wesentliche End-to-End-Funktionalitäten (vorerst) nicht vorgesehen sind, wurden zu Beginn klare Entwicklungsabschnitte nach dem Konzept des **Vertical Slicing** definiert. Diese Strukturierung ermöglicht eine fokussierte und iterative Entwicklung:

1. **Grundlegendes Spielfeld**
    - Aufbau des Schachbretts.
    - Initialisierung der Figurenpositionen.
    - Darstellung des Schachbretts (optionale Konsolenausgabe).

2. **Bewegungslogik**
    - Implementierung der Bewegungsregeln für alle Figuren.
    - Überprüfung der Gültigkeit eines Zugs.
    - Erkennung von Schach, Schachmatt oder Remis.
    - Speicherung und Anzeige der Zughistorie.

3. **Spezialregeln**
    - Implementierung spezieller Regeln wie „Rochade“, "pawnnumwandlung" und „En Passant“.

Da bislang kein Input/Output für die User-Interaktion implementiert wurde, kann die Entwicklung bisher auch nur über die Unit Tests nachvollzogen werden.

Von Beginn an wurde überwiegend **testgetrieben entwickelt**. Dies erleichtert die Implementierung der Methoden gemäß der Schachregeln und stellt sicher, dass jede Erweiterung präzise und robust bleibt. Die Entwicklung wurde auf verschiedene Branches aufgeteilt, um parallele Arbeiten zu ermöglichen. Zusätzlich wurde **Continuous Integration (CI)** eingerichtet, um alle Tests automatisch auszuführen und sicherzustellen, dass nur funktionierende Branches in den Hauptzweig gemergt werden.

Außerdem wurde sich bereits im Vorfeld eines jeden Entwicklungsschritts Gedanken über Struktur und Methodik gemacht und dieses in ERD bzw. UML-Diagrammen skizziert. Es sei dazu gesagt, dass es dabei zu gewisse Inkonsistenzen bei der Benennung von Methoden und Atributen kam. ;) 

**ERD Konzept**

![{0DA5029C-E033-4E30-90E0-975E136EBE3D}](https://github.com/user-attachments/assets/c3316a1d-befe-4233-bc3b-a5b2a3787108)

---

### Implementierungsschritte

#### **1. Grundlegendes Spielfeld**
Der erste Entwicklungsabschnitt konzentrierte sich auf die grundlegende Logik des Schachbretts:
- **Modellierung des Spielfelds:** 
    - Das Schachbrett wurde als 2-dimensionales Array implementiert, in dem jedes Feld durch seine Koordinaten (`[Zeile][Spalte]`) referenziert wird.
    - Jedes Feld kann entweder leer sein oder eine Schachfigur enthalten.
- **Initialisierung der Startaufstellung:**
    - Figuren wie pawnn, bishop und Türme wurden als Objekte erstellt und auf den entsprechenden Startfeldern des Bretts positioniert.
    - Jedes Figurenobjekt enthält Attribute wie Farbe (weiß oder schwarz), aktuelle Position und spezifische Bewegungslogik.
- **Konsolenausgabe:**
    - Eine einfache Darstellung des Schachbretts wurde in der Konsole implementiert, um die Platzierung der Figuren zu überprüfen und den aktuellen Spielstatus darzustellen.
 
- **vereinfachte UML-Darstellung**

![grafik](https://github.com/user-attachments/assets/9106faac-a809-4a1d-8851-d888122ded15)


#### **2. Bewegungslogik**
Die zweite Phase umfasste die Implementierung der Bewegungsregeln und die Validierung von Zügen:
- **Figurenbewegungen:**
    - Jede Figur erhielt ihre spezifischen Bewegungsregeln:
        - Der **pawn** kann sich nach vorne bewegen und diagonal schlagen.
        - Der **bishop** bewegt sich nur diagonal, ohne Figuren zu überspringen.
        - Der **rook** bewegt sich orthogonal, ebenfalls ohne Hindernisse zu überspringen.
        - Die **queen** kombiniert die Bewegungsregeln von rook und bishop.
        - Der **king** kann sich nur ein Feld in jede Richtung bewegen.
    - Die Bewegungsregeln wurden durch eigene Methoden wie `is_move_valid` in den jeweiligen Figurenklassen umgesetzt.
- **Validierung der Züge:**
    - Vor jedem Zug wird überprüft:
        - **Spielfeldgrenzen:** Der Zug darf das Schachbrett nicht verlassen.
        - **Blockaden:** Figuren dürfen keine anderen Figuren überspringen (außer knight).
        - **Zielposition:** Das Zielfeld muss entweder leer sein oder eine gegnerische Figur enthalten.
     
          ![grafik](https://github.com/user-attachments/assets/b3764f78-09a1-4ca8-bb3b-67c3a5931607)


- **Schach- und Schachmatt-Erkennung:**
    - Die Spiellogik wurde erweitert, um Situationen zu erkennen, in denen der king bedroht ist.
    - „Schachmatt“ wird erkannt, wenn keine gültigen Züge mehr verfügbar sind, um die Bedrohung zu beseitigen.
 
        ![grafik](https://github.com/user-attachments/assets/6d9e58d9-9c55-491e-8b3c-4919603a9539)

- **Testszenarien:**
    - Für jede Figur wurden Unit Tests erstellt, die typische und komplexe Spielsituationen abdecken, um die Einhaltung der Bewegungsregeln sicherzustellen.


#### **3. Spezialregeln**
Die dritte Phase konzentrierte sich auf die Implementierung und Validierung von Spezialregeln:
- **Rochade:**
    - Die Rochade wurde implementiert, sodass der king und ein rook gleichzeitig bewegt werden können, wenn:
        - Weder der king noch der rook zuvor bewegt wurden.
        - Keine Figuren zwischen ihnen stehen.
        - Der king nicht im Schach steht oder durch die Rochade ins Schach gerät.
- **pawnnumwandlung:**
    - Wenn ein pawn die letzte Reihe erreicht, wird der Spieler aufgefordert, ihn in eine beliebige andere Figur umzuwandeln (standardmäßig in eine queen).
- **En Passant:**
    - Diese Regel erlaubt es einem pawnn, einen gegnerischen pawnn zu schlagen, der im vorherigen Zug zwei Felder vorgerückt ist. Um dies umzusetzen:
        - Die Zughistorie wurde erweitert, um den letzten Zug eines pawnn zu speichern.
        - Vor jedem Zug wird überprüft, ob „En Passant“ möglich ist.
     
          ![grafik](https://github.com/user-attachments/assets/45971df2-1b95-4320-8210-13b627c4e519)


- **Testszenarien:**
    - Jedes Szenario, einschließlich gültiger und ungültiger Anwendungen dieser Regeln, wurde durch Tests abgesichert.

---

### Bekannte Fehler:

- Im jetzigem Entwicklungsstand sind momentan alle Bedingungen **ohne** Error Handling geschrieben worden, was bei z.B. fehlerhaften Spielzügen zu einem vorzeitigen Abbruch des Programms führen würde. Sobald sich damit beschäftigt wurde, wird dies jedoch entsprechend überarbeitet.
- Bei der Spezialregel "pawnnumwandlung" wird der pawn momentan noch standartmäßig in eine queen umgewandelt. Dies ist mit der (noch) fehlenden Benutzereingabe zu begründen.

----


## Project goal
The aim is to develop a chess game with complete game logic that maps both the basic and the more complex rules of the game. The aim is to deliberately avoid using existing libraries that already contain chess rules and sequences.

---

## Development steps

### Conceptualization 
Even though the development of the program logic is the primary focus of this project and essential end-to-end functionalities are not planned (for the time being), clear development stages were defined at the beginning according to the concept of **vertical slicing**. This structure enables focused and iterative development:

1. **Basic playing field**
    - Construction of the chessboard.
    - Initialization of the piece positions.
    - Display of the chessboard (optional console output).

2. **Movement logic**
    - Implementation of the movement rules for all pieces.
    - Checking the validity of a move.
    - Recognition of check, checkmate or draw.
    - Storage and display of the move history.

3 **Special rules**
    - Implementation of special rules such as “castling”, “pawn conversion” and “en passant”.

As no input/output for user interaction has been implemented to date, the development can only be traced via the unit tests.

Right from the start, development was predominantly **test-driven**. This facilitates the implementation of the methods according to the chess rules and ensures that each extension remains precise and robust. The development was split across different branches to enable parallel work. In addition, **Continuous Integration (CI)** was set up to run all tests automatically and ensure that only working branches are merged into the main branch.

Furthermore, the structure and methodology of each development step was considered in advance and outlined in ERD and UML diagrams. It should be noted that there were certain inconsistencies in the naming of methods and attributes ;) 

---

### Implementation steps

#### **1. Basic board**
The first stage of development focused on the basic logic of the chessboard:
- **Modeling the board:** 
    - The chessboard was implemented as a 2-dimensional array in which each square is referenced by its coordinates (`[row][column]`).
    - Each field can either be empty or contain a chess piece.
- **Initialization of the starting position:**
    - Pieces such as pawns, bishops and rooks have been created as objects and positioned on the corresponding starting squares of the board.
    - Each piece object contains attributes such as color (white or black), current position and specific movement logic.
- Console output:**
    - A simple representation of the chessboard has been implemented in the console to check the placement of the pieces and display the current game status.
 
#### **2. Movement logic**
The second phase comprised the implementation of the movement rules and the validation of moves:
- **Figure movements:**
    - Each piece was given its specific movement rules:
        - The **pawn** can move forward and capture diagonally.
        - The **Bishop** only moves diagonally without skipping pieces.
        - The **tower** moves orthogonally, also without jumping over obstacles.
        - The **queen** combines the movement rules of the rook and bishop.
        - The **king** can only move one square in each direction.
    - The movement rules have been implemented using special methods such as `is_move_valid` in the respective piece classes.
- **Move validation:**
    - A check is made before each move:
        - **Pitch boundaries:** The move must not leave the chessboard.
        - **Blockades:** Pieces may not jump over other pieces (except knights).
        - **Target position:** The target square must either be empty or contain an opponent's piece.

- **Check and checkmate detection:**
    - The game logic has been extended to recognize situations in which the king is threatened.
    - “Checkmate” is recognized when there are no more valid moves available to eliminate the threat.

- **Test scenarios:**
    - Unit tests have been created for each character, covering typical and complex game situations to ensure compliance with the movement rules.


#### **3. Special rules**
The third phase focused on the implementation and validation of special rules:
- **Rochade:**
    - Castling was implemented so that the king and a rook can be moved simultaneously if:
        - Neither the king nor the rook have been moved before.
        - There are no pieces between them.
        - The king is not in check or is put in check by castling.
- **Pawn conversion:**
    - When a pawn reaches the last rank, the player is asked to convert it to any other piece (by default to a queen).
- **En Passant:**
    - This rule allows a pawn to capture an opponent's pawn that has advanced two squares in the previous move. To implement this:
        - The move history has been extended to store the last move of a pawn.
        - Before each move, a check is made to see whether “En Passant” is possible.

- **Test scenarios:**
    - Each scenario, including valid and invalid applications of these rules, has been validated by testing.
