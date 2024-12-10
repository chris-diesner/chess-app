import React from 'react';

// Hilfsfunktion: Koordinaten generieren
const generateBoard = () => {
  const rows = 'abcdefgh'; // Schachspalten
  const board = [];

  for (let row = 8; row >= 1; row--) {
    for (let col = 0; col < rows.length; col++) {
      board.push(`${rows[col]}${row}`);
    }
  }
  return board;
};

const Board: React.FC = () => {
  const boardSquares = generateBoard(); // Koordinaten generieren

  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(8, 50px)',
        gridTemplateRows: 'repeat(8, 50px)',
        border: '2px solid black',
      }}
    >
      {boardSquares.map((square, index) => {
        // Abwechselnde Farben
        const isBlack = (Math.floor(index / 8) + index) % 2 === 1;

        return (
          <div
            key={square}
            style={{
              backgroundColor: isBlack ? '#769656' : '#eeeed2',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              width: '50px',
              height: '50px',
              fontSize: '12px',
              color: isBlack ? '#fff' : '#000',
            }}
          >
            {square} {/* Label anzeigen */}
          </div>
        );
      })}
    </div>
  );
};

export default Board;
