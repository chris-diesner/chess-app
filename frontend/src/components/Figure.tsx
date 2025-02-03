import React from 'react';
import { useDrag } from 'react-dnd';

const Figure: React.FC<{ figure: string; position: string }> = ({ figure, position }) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: 'FIGURE',
    item: { figure, position },
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  return (
    <img
      ref={drag}
      src={`/figures/${figure}.png`}
      alt={figure}
      className="chess-piece"
      style={{ opacity: isDragging ? 0.5 : 1, cursor: 'grab' }}
    />
  );
};

export default Figure;