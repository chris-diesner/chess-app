import React, { ReactNode } from "react";

interface SquareProps {
  isBlack: boolean;
  position: string;
  children?: ReactNode;
}

const Square: React.FC<SquareProps> = ({ isBlack, position, children }) => {
  return (
    <div className={`square ${isBlack ? "black" : "white"}`} data-position={position}>
      {children}
    </div>
  );
};

export default Square;
