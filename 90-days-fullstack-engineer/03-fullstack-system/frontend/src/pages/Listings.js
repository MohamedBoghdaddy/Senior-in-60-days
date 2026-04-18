import { useEffect, useState } from "react";
import { fetchListings } from "../services/api";
import SearchBar from "../components/SearchBar";

export default function Listings() {
  const [listings, setListings] = useState([]);
  const [query, setQuery] = useState("");
  const [error, setError] = useState(null);

  useEffect(() => {
    loadListings();
  }, []);

  const loadListings = (search = "") => {
    fetchListings({ search, page: 1 })
      .then((response) => setListings(response.data.items || []))
      .catch((err) => setError(err.message));
  };

  return (
    <section>
      <h2>Listings</h2>
      <SearchBar
        query={query}
        onChange={setQuery}
        onSearch={() => loadListings(query)}
      />
      {error && <p style={{ color: "red" }}>{error}</p>}
      <ul>
        {listings.map((item) => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </section>
  );
}
