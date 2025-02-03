import React, { useState } from 'react';
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import '../styles/Board.css';
import Square from './Square';

const initialBoard: (string | null)[][] = [
  ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
  ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  [null, null, null, null, null, null, null, null],
  ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
  ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
];

const Board: React.FC = () => {
  const [boardState, setBoardState] = useState(initialBoard);

  const moveFigure = (from: string, to: string) => {
    console.log(`Zug von ${from} nach ${to}`);

    const fromRow = 8 - parseInt(from[1]);
    const fromCol = from.charCodeAt(0) - 'a'.charCodeAt(0);
    const toRow = 8 - parseInt(to[1]);
    const toCol = to.charCodeAt(0) - 'a'.charCodeAt(0);

    const newBoard = boardState.map((row) => [...row]);
    newBoard[toRow][toCol] = newBoard[fromRow][fromCol];
    newBoard[fromRow][fromCol] = null;

    setBoardState(newBoard);
  };

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="board-container">
        <div className="chessboard">
          {/* Spaltennamen oben */}
          <div className="board-margin"></div>
          {[...'abcdefgh'].map((col, index) => (
            <div key={`col-top-${col}`} className="column-label" style={{ gridColumn: index + 2, gridRow: 10 }}>
              {col}
            </div>
          ))}

          {/* Zeilen + Schachfelder */}
          {[...Array(8)].map((_, rowIndex) => (
            <React.Fragment key={rowIndex}>
              {/* Zeilennummer links */}
              <div className="row-label" style={{ gridRow: rowIndex + 1 }}>
                {8 - rowIndex}
              </div>

              {[...Array(8)].map((_, colIndex) => {
                const position = `${String.fromCharCode(97 + colIndex)}${8 - rowIndex}`;
                const isBlack = (rowIndex + colIndex) % 2 === 1;
                const figure = boardState[rowIndex][colIndex];

                return <Square key={position} isBlack={isBlack} position={position} figure={figure} moveFigure={moveFigure} />;
              })}
            </React.Fragment>
          ))}
        </div>
      </div>
    </DndProvider>
  );
};

export default Board;
