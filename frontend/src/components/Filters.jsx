import React, { useState } from "react";

const Filters = ({ onApply }) => {
  const [minAQI, setMinAQI] = useState("");
  const [maxAQI, setMaxAQI] = useState("");

  const applyFilters = () => {
  const params = {
    min_aqi: minAQI,
    max_aqi: maxAQI,
  };

  console.log("Sending params:", params);
  onApply(params);
};

  return (
    <div>
      <h3>Filters</h3>

      <input
        placeholder="Min AQI"
        onChange={(e) => setMinAQI(e.target.value)}
      />

      <input
        placeholder="Max AQI"
        onChange={(e) => setMaxAQI(e.target.value)}
      />

      <button onClick={() => {
  console.log("Apply clicked");
  applyFilters();
}}>
  Apply
</button>
    </div>
  );
};

export default Filters;