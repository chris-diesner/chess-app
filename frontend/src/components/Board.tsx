import React, { useState, useEffect } from "react";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import Square from "./Square";
import Figure from "./Figure"; // Import für Figuren-Komponente
import "../styles/Board.css"; // Falls Styling vorhanden ist

const API_URL = "http://localhost:5000/api/board"; // API-URL anpassen!

const Board: React.FC = () => {
  const [boardState, setBoardState] = useState<(null | { type: string; color: string; position: string })[][]>([]);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        console.log("DEBUG: API Response", data); // <-- Fügt diese Zeile hinzu
        setBoardState(data);
      })
      .catch((err) => console.error("Fehler beim Laden des Bretts:", err));
  }, []);

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="board-container">
        <div className="chessboard">
          {[...Array(8)].map((_, rowIndex) => (
            <React.Fragment key={rowIndex}>
              {[...Array(8)].map((_, colIndex) => {
                const position = `${String.fromCharCode(97 + colIndex)}${8 - rowIndex}`;
                const isBlack = (rowIndex + colIndex) % 2 === 1;
                const figure = boardState[rowIndex]?.[colIndex] ?? null;

                return (
                  <Square key={position} isBlack={isBlack} position={position}>
                    {figure && <Figure type={figure.type} color={figure.color} />}
                  </Square>
                );
              })}
            </React.Fragment>
          ))}
        </div>
      </div>
    </DndProvider>
  );
};

export default Board;
