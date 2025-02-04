import React, { useState, useEffect } from "react";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import Square from "./Square";
import Figure from "./Figure";
import "../styles/Board.css";

const API_URL = "http://localhost:5000/api/board";
const MOVE_API_URL = "http://localhost:5000/api/move";

const Board: React.FC = () => {
  const [boardState, setBoardState] = useState<(null | { type: string; color: string; position: string })[][]>([]);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        console.log("DEBUG: API Response", data);
        setBoardState(data);
      })
      .catch((err) => console.error("Fehler beim Laden des Bretts:", err));
  }, []);

  const handleMoveFigure = (figureId: string, toPosition: string) => {
    console.log(`Moving ${figureId} to ${toPosition}`);

    fetch(MOVE_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ figureId, toPosition }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("DEBUG: Move Response", data);
        setBoardState(data);
      })
      .catch((err) => console.error("Fehler beim Bewegen der Figur:", err));
  };

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
                  <Square key={position} isBlack={isBlack} position={position} onMoveFigure={handleMoveFigure}>
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
