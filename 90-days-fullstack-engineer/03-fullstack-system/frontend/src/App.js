import { Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Listings from "./pages/Listings";
import Details from "./pages/Details";
import AIInsights from "./pages/AIInsights";

function App() {
  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: 24 }}>
      <header>
        <h1>Senior Platform Dashboard</h1>
        <nav>
          <Link to="/" style={{ marginRight: 16 }}>
            Dashboard
          </Link>
          <Link to="/listings" style={{ marginRight: 16 }}>
            Listings
          </Link>
          <Link to="/ai-insights">AI Insights</Link>
        </nav>
      </header>
      <main style={{ marginTop: 24 }}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/listings" element={<Listings />} />
          <Route path="/listings/:id" element={<Details />} />
          <Route path="/ai-insights" element={<AIInsights />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
