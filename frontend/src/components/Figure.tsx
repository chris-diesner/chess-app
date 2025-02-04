import React from "react";

interface FigureProps {
  type: string;
  color: string;
}

const Figure: React.FC<FigureProps> = ({ type, color }) => {
  const imageSrc = `/figures/${color}_${type}.png`; 

  return <img src={imageSrc} alt={`${color} ${type}`} className="figure" />;
};

export default Figure;
