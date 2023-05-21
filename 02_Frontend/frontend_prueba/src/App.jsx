import { useEffect, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [data, setData] = useState([]);
  const [consulta, setConsulta] = useState("");

  useEffect(() => {
    fetch(`http://localhost:5000/api/noticias/${consulta}`)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, [consulta]);

  const handleConsultaChange = (event) => {
    setConsulta(event.target.value);
  };

  return (
    <div>
      <input type="text" value={consulta} onChange={handleConsultaChange} />
      <button onClick={() => setConsulta("")}>Limpiar</button>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Rank</th>
          </tr>
        </thead>
        <tbody>
          {data.map((noticia) => (
            <tr key={noticia.id}>
              <td>{noticia.id}</td>
              <td>{noticia.title}</td>
              <td>{noticia.rank}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
