import React from "react";
import { useDrag } from "react-dnd";

interface FigureProps {
  type: string;
  color: string;
}

const Figure: React.FC<FigureProps> = ({ type, color }) => {
  const [{isDragging}, drag] = useDrag(() => ({
    type: "FIGURE",
    item: {type, color},
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  const imageSrc = `/figures/${color}_${type}.png`; 

  return (
    <img
      ref={drag}
      src={imageSrc}
      alt={`${color} ${type}`}
      className="figure"
      style={{ opacity: isDragging ? 0.5 : 1, cursor: "grab" }}
    />
  );
};

export default Figure;
