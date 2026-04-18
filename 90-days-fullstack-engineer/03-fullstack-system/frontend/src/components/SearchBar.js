export default function SearchBar({ query, onChange, onSearch }) {
  return (
    <div style={{ marginBottom: 16 }}>
      <input
        value={query}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Search listings..."
        style={{ width: 300, marginRight: 8, padding: 8 }}
      />
      <button onClick={onSearch}>Search</button>
    </div>
  );
}
