import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchListing } from "../services/api";

export default function Details() {
  const { id } = useParams();
  const [listing, setListing] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchListing(id)
      .then((response) => setListing(response.data))
      .catch((err) => setError(err.message));
  }, [id]);

  return (
    <section>
      <h2>Listing Details</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {!listing ? (
        <p>Loading item...</p>
      ) : (
        <article>
          <h3>{listing.title}</h3>
          <p>{listing.description}</p>
          <pre>{JSON.stringify(listing.document, null, 2)}</pre>
        </article>
      )}
    </section>
  );
}
