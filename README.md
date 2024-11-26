# Projektdokumentation

## Projektname
Chess App

## Projektziel
Das Ziel ist die Entwicklung eines Schachspiels mit vollständiger Spiellogik, das sowohl die grundlegenden als auch die komplexeren Regeln des Spiels abbildet. 

---

## Entwicklungsschritte

### Initialisierung und Grundgerüst
Das Projekt wurde mit einer grundlegenden Spielfeldstruktur und den ersten Schachfiguren gestartet. Das Spielfeld repräsentiert die Schachbrettlogik und ermöglicht es, Figuren auf bestimmte Felder zu setzen. Figuren wie Bauern, Läufer und Türme wurden implementiert, jeweils mit ihren grundlegenden Bewegungsregeln. Von Anfang an wurde größtenteils testgetrieben entwickelt: Für jede neue Funktion wurde zunächst ein Testfall definiert, um die Anforderungen präzise zu formulieren.

Parallel dazu wurde Continuous Integration (CI) eingerichtet, um sicherzustellen, dass alle Tests automatisch ausgeführt werden, sobald Änderungen vorgenommen werden. So konnte jede Funktionalität kontinuierlich überprüft werden.

---

### Implementierung der Bewegungsregeln
Die Bewegungslogik der Figuren wurde weiter verfeinert. Figuren wie der König und die Dame wurden hinzugefügt, und ihre speziellen Bewegungsmöglichkeiten wurden implementiert. Zusätzlich wurden grundlegende Einschränkungen wie das Verlassen des Spielfelds oder das Blockieren durch andere Figuren berücksichtigt.

---

### Einführung der Spiellogik für Schach und Schachmatt
Die Spiellogik wurde erweitert, um die Spielsituationen „Schach“ und „Schachmatt“ korrekt zu erkennen. Für „Schach“ wurde überprüft, ob der König durch eine gegnerische Figur bedroht wird. „Schachmatt“ tritt ein, wenn keine gültigen Züge mehr existieren, um den König zu retten.

Zunächst wurden Tests für einfache Situationen erstellt, bevor komplexere Spielszenarien wie Kombinationen aus mehreren Bedrohungen umgesetzt wurden.

---

### Spezialregel: En passant
Die Regel „en passant“ wurde hinzugefügt, eine der komplexeren Regeln im Schach. Hierbei darf ein Bauer geschlagen werden, der im vorherigen Zug zwei Felder vorgerückt ist, wenn der schlagende Bauer neben ihm steht.

Um die Regel korrekt umzusetzen, wurde die Zughistorie erweitert. Jeder Zug eines Bauern wird gespeichert, damit überprüft werden kann, ob „en passant“ anwendbar ist. Die Funktionalität wurde durch Tests abgesichert, die alle möglichen Fälle der Regel abdecken, einschließlich unzulässiger Situationen.

---

### Zughistorie und UUID-Validierung
Die Zughistorie wurde eingeführt, um den Spielverlauf zu dokumentieren und die Gültigkeit von Zügen besser überprüfen zu können. Jede Figur wurde mit einer eindeutigen UUID versehen. Dies ermöglicht eine zuverlässige Zuordnung von Figuren, selbst in komplexen Spielsituationen wie beim Schlagen oder bei der Promotion eines Bauern.

Diese Erweiterung wurde von Tests begleitet, die sicherstellen, dass die Zughistorie korrekt geführt wird und die UUID-Validierung fehlerfrei funktioniert.

---

Diese Projektdokumentation beschreibt den aktuellen Stand der Entwicklung und fasst die bisher umgesetzten Schritte zusammen. 
