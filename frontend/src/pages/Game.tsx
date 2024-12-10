import React from 'react';
import Board from '../components/Board';

const Game: React.FC = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '20px' }}>
      <h1>Schachspiel</h1>
      <Board />
      <div style={{ marginTop: '20px', width: '80%', textAlign: 'center' }}>
        <h2>Spielinformationen</h2>
        <p>Hier können Zughistorie, Spielerinfos oder Status angezeigt werden.</p>
      </div>
    </div>
  );
};

export default Game;
