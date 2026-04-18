const { pool } = require("../config/db");

exports.searchListings = async (query, offset, limit) => {
  const sql = `
    SELECT id, title, owner_id, status, created_at
    FROM listings
    WHERE title ILIKE $1 OR description ILIKE $1
    ORDER BY created_at DESC
    LIMIT $2 OFFSET $3
  `;
  const values = [`%${query}%`, limit, offset];
  const result = await pool.query(sql, values);
  return { items: result.rows, pagination: { offset, limit } };
};

exports.getListingById = async (id) => {
  const result = await pool.query(
    "SELECT id, title, description, owner_id, status FROM listings WHERE id = $1",
    [id],
  );
  return result.rows[0];
};

exports.saveListingMetadata = async ({ title, description, ownerId }) => {
  const sql =
    "INSERT INTO listings (title, description, owner_id, status) VALUES ($1, $2, $3, $4) RETURNING id";
  const result = await pool.query(sql, [title, description, ownerId, "active"]);
  return result.rows[0];
};
