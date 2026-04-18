import { useEffect, useState } from "react";
import { fetchDashboard } from "../services/api";

export default function Dashboard() {
  const [metrics, setMetrics] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchDashboard()
      .then((response) => setMetrics(response.data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <section>
      <h2>Dashboard</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {!metrics ? (
        <p>Loading metrics...</p>
      ) : (
        <div>
          <div>Active listings: {metrics.activeListings}</div>
          <div>Queued jobs: {metrics.queuedJobs}</div>
          <div>AI insights processed: {metrics.aiReports}</div>
        </div>
      )}
    </section>
  );
}
