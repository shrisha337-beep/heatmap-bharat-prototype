import React, { useEffect, useState } from "react";
import MapView from "./components/MapView";
import Filters from "./components/Filters";
import { fetchHeatmapData } from "./api";

function App() {
  const [data, setData] = useState([]);

  const loadData = async (params = {}) => {
  console.log("Calling API with:", params);

  const res = await fetchHeatmapData(params);

  console.log("Received data:", res);

  setData(res);
};

  useEffect(() => {
    loadData();
  }, []);

  return (
    <div style={{ display: "flex" }}>
      <div style={{ width: "300px", padding: "10px" }}>
        <Filters onApply={loadData} />
      </div>

      <div style={{ flex: 1 }}>
        <MapView data={data} />
      </div>
    </div>
  );
}

export default App;