# Projektdokumentation

## Projektname
Chess App

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
    - Implementierung spezieller Regeln wie „Rochade“, "Bauernumwandlung" und „En Passant“.

Da bislang kein Input/Output für die User-Interaktion implementiert wurde, kann die Entwicklung bisher auch nur über die Unit Tests nachvollzogen werden.

Von Beginn an wurde überwiegend **testgetrieben entwickelt**. Dies erleichtert die Implementierung der Methoden gemäß der Schachregeln und stellt sicher, dass jede Erweiterung präzise und robust bleibt. Die Entwicklung wurde auf verschiedene Branches aufgeteilt, um parallele Arbeiten zu ermöglichen. Zusätzlich wurde **Continuous Integration (CI)** eingerichtet, um alle Tests automatisch auszuführen und sicherzustellen, dass nur funktionierende Branches in den Hauptzweig gemergt werden.

---

### Implementierungsschritte

#### **1. Grundlegendes Spielfeld**
Der erste Entwicklungsabschnitt konzentrierte sich auf die grundlegende Logik des Schachbretts:
- **Modellierung des Spielfelds:** 
    - Das Schachbrett wurde als 2-dimensionales Array implementiert, in dem jedes Feld durch seine Koordinaten (`[Zeile][Spalte]`) referenziert wird.
    - Jedes Feld kann entweder leer sein oder eine Schachfigur enthalten.
- **Initialisierung der Startaufstellung:**
    - Figuren wie Bauern, Läufer und Türme wurden als Objekte erstellt und auf den entsprechenden Startfeldern des Bretts positioniert.
    - Jedes Figurenobjekt enthält Attribute wie Farbe (weiß oder schwarz), aktuelle Position und spezifische Bewegungslogik.
- **Konsolenausgabe:**
    - Eine einfache Darstellung des Schachbretts wurde in der Konsole implementiert, um die Platzierung der Figuren zu überprüfen und den aktuellen Spielstatus darzustellen.

#### **2. Bewegungslogik**
Die zweite Phase umfasste die Implementierung der Bewegungsregeln und die Validierung von Zügen:
- **Figurenbewegungen:**
    - Jede Figur erhielt ihre spezifischen Bewegungsregeln:
        - Der **Bauer** kann sich nach vorne bewegen und diagonal schlagen.
        - Der **Läufer** bewegt sich nur diagonal, ohne Figuren zu überspringen.
        - Der **Turm** bewegt sich orthogonal, ebenfalls ohne Hindernisse zu überspringen.
        - Die **Dame** kombiniert die Bewegungsregeln von Turm und Läufer.
        - Der **König** kann sich nur ein Feld in jede Richtung bewegen.
    - Die Bewegungsregeln wurden durch eigene Methoden wie `is_move_valid` in den jeweiligen Figurenklassen umgesetzt.
- **Validierung der Züge:**
    - Vor jedem Zug wird überprüft:
        - **Spielfeldgrenzen:** Der Zug darf das Schachbrett nicht verlassen.
        - **Blockaden:** Figuren dürfen keine anderen Figuren überspringen (außer Springer).
        - **Zielposition:** Das Zielfeld muss entweder leer sein oder eine gegnerische Figur enthalten.
- **Schach- und Schachmatt-Erkennung:**
    - Die Spiellogik wurde erweitert, um Situationen zu erkennen, in denen der König bedroht ist.
    - „Schachmatt“ wird erkannt, wenn keine gültigen Züge mehr verfügbar sind, um die Bedrohung zu beseitigen.
- **Testszenarien:**
    - Für jede Figur wurden Unit Tests erstellt, die typische und komplexe Spielsituationen abdecken, um die Einhaltung der Bewegungsregeln sicherzustellen.

#### **3. Spezialregeln**
Die dritte Phase konzentrierte sich auf die Implementierung und Validierung von Spezialregeln:
- **Rochade:**
    - Die Rochade wurde implementiert, sodass der König und ein Turm gleichzeitig bewegt werden können, wenn:
        - Weder der König noch der Turm zuvor bewegt wurden.
        - Keine Figuren zwischen ihnen stehen.
        - Der König nicht im Schach steht oder durch die Rochade ins Schach gerät.
- **Bauernumwandlung:**
    - Wenn ein Bauer die letzte Reihe erreicht, wird der Spieler aufgefordert, ihn in eine beliebige andere Figur umzuwandeln (standardmäßig in eine Dame).
- **En Passant:**
    - Diese Regel erlaubt es einem Bauern, einen gegnerischen Bauern zu schlagen, der im vorherigen Zug zwei Felder vorgerückt ist. Um dies umzusetzen:
        - Die Zughistorie wurde erweitert, um den letzten Zug eines Bauern zu speichern.
        - Vor jedem Zug wird überprüft, ob „En Passant“ möglich ist.
- **Testszenarien:**
    - Jedes Szenario, einschließlich gültiger und ungültiger Anwendungen dieser Regeln, wurde durch Tests abgesichert.

---

