import React from 'react';
import '../styles/Board.css';

// Hilfsfunktion: Koordinaten generieren
const generateBoard = () => {
  const rows = 'abcdefgh';
  const board = [];

  for (let row = 8; row >= 1; row--) {
    for (let col = 0; col < rows.length; col++) {
      board.push({ square: `${rows[col]}${row}`, row, col });
    }
  }

  return board;
};

const Board: React.FC = () => {
  const boardSquares = generateBoard(); // Koordinaten und Felder erstellen

  return (
    <div className="board-container">
      <div className="chessboard">
        {/* Spaltennamen oben */}
        <div className="board-margin"></div>
        {[...'abcdefgh'].map((col) => (
          <div key={`col-top-${col}`} className="column-label">
            {col}
          </div>
        ))}
        <div className="board-margin"></div>

        {/* Zeilen + Schachfelder */}
        {[...Array(8)].map((_, rowIndex) => (
          <>
            {/* Zeilennummer links */}
            <div key={`row-left-${8 - rowIndex}`} className="row-label">
              {8 - rowIndex}
            </div>

            {[...Array(8)].map((_, colIndex) => {
              const square = boardSquares[rowIndex * 8 + colIndex];
              const isBlack = (rowIndex + colIndex) % 2 === 1;

              return (
                <div
                  key={square.square}
                  className={`square ${isBlack ? 'black' : 'white'}`}
                >
                  {/* {square.square} (optional für Debugging) */}
                </div>
              );
            })}

            {/* Zeilennummer rechts */}
            <div key={`row-right-${8 - rowIndex}`} className="row-label">
              {8 - rowIndex}
            </div>
          </>
        ))}

        {/* Spaltennamen unten */}
        <div className="board-margin"></div>
        {[...'abcdefgh'].map((col) => (
          <div key={`col-bottom-${col}`} className="column-label">
            {col}
          </div>
        ))}
        <div className="board-margin"></div>
      </div>
    </div>
  );
};

export default Board;
