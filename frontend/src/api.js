import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const fetchHeatmapData = async (params = {}) => {
  const res = await axios.get(`${BASE_URL}/heatmap`, { params });
  return res.data;
};