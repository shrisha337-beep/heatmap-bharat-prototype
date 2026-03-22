import React, { useEffect, useRef } from "react";
import mapboxgl from "mapbox-gl";

mapboxgl.accessToken = "YOUR_MAPBOX_TOKEN";

const MapView = ({ data }) => {
  const mapContainer = useRef(null);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: mapContainer.current,
      style: "mapbox://styles/mapbox/dark-v10",
      center: [77.23, 28.61],
      zoom: 5,
    });

    map.on("load", () => {
      const features = data.map((d) => ({
        type: "Feature",
        geometry: {
          type: "Point",
          coordinates: [d.lon, d.lat],
        },
        properties: {
          intensity: d.intensity,
        },
      }));

      map.addSource("heat", {
        type: "geojson",
        data: {
          type: "FeatureCollection",
          features,
        },
      });

      map.addLayer({
        id: "heatmap",
        type: "heatmap",
        source: "heat",
        paint: {
          "heatmap-weight": ["get", "intensity"],
          "heatmap-radius": 25,
        },
      });
    });

    return () => map.remove();
  }, [data]);

  return <div ref={mapContainer} style={{ height: "100vh" }} />;
};

export default MapView;