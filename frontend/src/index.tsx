import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

// Sicherstellen, dass TypeScript weiß, dass "root" existiert
const rootElement = document.getElementById('root') as HTMLElement;

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  rootElement
);
