import { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [bericht, setBericht] = useState('');

  const senden = async () => {
    const res = await axios.post('http://localhost:8000/bericht', {
      stichpunkte: input,
    });
    setBericht(res.data.bericht);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Pflegebericht-Agent</h1>
      <textarea rows="6" value={input} onChange={(e) => setInput(e.target.value)} />
      <br />
      <button onClick={senden}>Bericht generieren</button>
      <pre>{bericht}</pre>
    </div>
  );
}

export default App;
