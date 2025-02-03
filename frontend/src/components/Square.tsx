import React from 'react';
import { useDrop } from 'react-dnd';
import Figure from './Figure';

const Square: React.FC<{ isBlack: boolean; position: string; figure: string | null; moveFigure: (from: string, to: string) => void }> = ({
  isBlack,
  position,
  figure,
  moveFigure,
}) => {
    const [, drop] = useDrop(() => ({
        accept: 'FIGURE',
        drop: (item: { figure: string; position: string }) => {
          console.log(`Figur ${item.figure} von ${item.position} nach ${position} gezogen`);
          moveFigure(item.position, position);
        },
      }));
      

  return (
    <div ref={drop} className={`square ${isBlack ? 'black' : 'white'}`}>
      {figure && <Figure figure={figure} position={position} />}
    </div>
  );
};

export default Square;
