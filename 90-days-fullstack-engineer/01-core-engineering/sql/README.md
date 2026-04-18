# Core Engineering: Practical SQL

This folder collects SQL patterns that matter for production platforms.

## 1. Joins
Use joins to connect relational entities while preserving performance.

Example: query a platform listing with owner and tags.

```sql
SELECT
  l.id,
  l.title,
  u.name AS owner_name,
  t.label AS tag
FROM listings l
JOIN users u ON u.id = l.owner_id
LEFT JOIN listing_tags lt ON lt.listing_id = l.id
LEFT JOIN tags t ON t.id = lt.tag_id
WHERE l.status = 'active';
```

## 2. Indexing
Choose indexes for read-heavy queries and composite key access patterns.

Example: add a compound index for filter and sort.

```sql
CREATE INDEX idx_listings_status_created_at
ON listings (status, created_at DESC);
```

## 3. Query optimization
Avoid `SELECT *`, prefer predicate pushdown, and use explain plans.

Example: limit returned columns and filter early.

```sql
EXPLAIN ANALYZE
SELECT id, title, price
FROM listings
WHERE status = 'active' AND price > 50
ORDER BY created_at DESC
LIMIT 20;
```

## 4. Transactions
Use transactions for multi-step consistency boundaries.

Example: create a user and initial profile in one atomic flow.

```sql
BEGIN;
INSERT INTO users (email, hashed_password) VALUES ('alex@example.com', '...');
INSERT INTO profiles (user_id, display_name) VALUES (currval(pg_get_serial_sequence('users','id')), 'Alex');
COMMIT;
```

## 5. Normalization vs denormalization
When to normalize:
- reduce update anomalies
- enforce strong relational integrity
- support complex joins across entities

When to denormalize:
- improve read performance for dashboards
- reduce join latency in high-traffic queries
- cache derived state in a separate table

Example schema for a production platform:

- `users`: identity and role data
- `listings`: business entity with owner and status
- `organizations`: multi-tenant metadata
- `events`: audit trail and activity
- `documents`: unstructured attachments stored in MongoDB by reference

## 6. Example schema

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  role TEXT NOT NULL DEFAULT 'member',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE listings (
  id SERIAL PRIMARY KEY,
  owner_id INT NOT NULL REFERENCES users(id),
  title TEXT NOT NULL,
  description TEXT,
  status TEXT NOT NULL DEFAULT 'draft',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## 7. Practical takeaways
- Validate data structures before persisting.
- Use indexes aligned to filters and sorts.
- Model immutable history in append-only tables when audit is required.
- Keep heavy unstructured text in document stores when relational joins are unnecessary.
