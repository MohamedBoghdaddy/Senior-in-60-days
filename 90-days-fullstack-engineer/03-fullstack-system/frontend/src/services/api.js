import axios from "axios";

const client = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://localhost:5000/api",
});

export const fetchDashboard = () => client.get("/dashboard");
export const fetchListings = (query) =>
  client.get("/listings", { params: query });
export const fetchListing = (id) => client.get(`/listings/${id}`);
export const fetchAIInsights = () => client.get("/ai/insights");
