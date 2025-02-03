import React from 'react';
import '../styles/Board.css';

// Startpositionen für das Schachspiel (FEN-ähnlich)
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
  const boardSquares = generateBoard(); // Koordinaten generieren

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
          <React.Fragment key={rowIndex}>
            {/* Zeilennummer links */}
            <div className="row-label">{8 - rowIndex}</div>

            {[...Array(8)].map((_, colIndex) => {
              const square = boardSquares[rowIndex * 8 + colIndex];
              const isBlack = (rowIndex + colIndex) % 2 === 1;
              const piece = initialBoard[rowIndex][colIndex]; // Figur an dieser Position

              return (
                <div key={square.square} className={`square ${isBlack ? 'black' : 'white'}`}>
                  {piece && (
                    <img src={`/figures/${piece}.png`} alt={piece} className="chess-piece" />
                  )}
                </div>
              );
            })}

            {/* Zeilennummer rechts */}
            <div className="row-label">{8 - rowIndex}</div>
          </React.Fragment>
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
