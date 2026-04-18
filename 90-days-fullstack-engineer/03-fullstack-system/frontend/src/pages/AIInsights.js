import { useEffect, useState } from "react";
import { fetchAIInsights } from "../services/api";

export default function AIInsights() {
  const [insights, setInsights] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchAIInsights()
      .then((response) => setInsights(response.data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <section>
      <h2>AI Insights</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {!insights ? (
        <p>Loading AI insight...</p>
      ) : (
        <div>
          <h3>{insights.summary}</h3>
          <p>Confidence: {insights.score}</p>
          <pre>{JSON.stringify(insights.details, null, 2)}</pre>
        </div>
      )}
    </section>
  );
}
