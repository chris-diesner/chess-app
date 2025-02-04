import React, { ReactNode } from "react";
import { useDrop } from "react-dnd";

interface SquareProps {
  isBlack: boolean;
  position: string;
  children?: ReactNode;
  onMoveFigure: (from: string, to: string) => void;
}

const Square: React.FC<SquareProps> = ({ isBlack, position, children, onMoveFigure }) => {
  const [{ isOver }, drop] = useDrop(() => ({
    accept: "FIGURE",
    drop: (item: { type: string; color: string }) => {
      onMoveFigure(item.color + "_" + item.type, position);
    },
    collect: (monitor) => ({
      isOver: !!monitor.isOver(),
    }),
  }));

  return (
    <div
      ref={drop}
      className={`square ${isBlack ? "black" : "white"} ${isOver ? "hover" : ""}`}
      data-position={position}
    >
      {children}
    </div>
  );
};

export default Square;