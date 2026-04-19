# System Design Framework

This is your personal framework for answering any system design question.
Fill it in as you practice. Refine it after each drill. By Day 90 this should be instinct.

---

## The 45-minute structure

| Time | Step | What you do |
|------|------|-------------|
| 0–5 min | Requirements | Ask clarifying questions. Write functional + non-functional requirements. |
| 5–10 min | Scale estimation | Calculate DAU → QPS → storage. Back of envelope. |
| 10–15 min | API design | Define the core API endpoints. |
| 15–20 min | Data model | Define the key tables/collections and their relationships. |
| 20–35 min | Architecture | Draw and explain the high-level components. |
| 35–42 min | Deep dive | Go deep on one critical component (caching, queue, DB, etc.). |
| 42–45 min | Tradeoffs + bottlenecks | What are the known limitations? What would you change at 10x scale? |

---

## Requirements questions I always ask

**Scope:**
1. What is the expected number of users? (DAU, monthly active?)
2. Is this read-heavy or write-heavy?
3. What is the acceptable latency? (p99 under 200ms? 1 second?)
4. What is the availability requirement? (99.9%? 99.99%?)
5. Is this global (multi-region) or single region?

**Features:**
6. Which features are MVP vs nice-to-have?
7. Do we need real-time updates or is eventual consistency acceptable?
8. Is there a mobile client? What network conditions?
9. Any compliance requirements (GDPR, HIPAA, PCI)?
10. Do we handle payments or other high-stakes operations?

---

## Scale estimation formula sheet

**Users → Requests:**
- DAU × average requests/user/day = daily requests
- daily requests / 86,400 = average QPS
- average QPS × 3–5 = peak QPS (rule of thumb)

**Storage:**
- (bytes per record) × (records per day) × (retention days) = total storage
- Add 20% overhead for indexes, metadata, replication

**Bandwidth:**
- QPS × average request size = read bandwidth
- Writes/sec × average write size = write bandwidth

**Quick benchmarks to remember:**
| Component | Approximate capacity |
|-----------|---------------------|
| Single relational DB (PostgreSQL) | 10K–30K reads/sec, 5K–10K writes/sec |
| Redis (single node) | 100K+ ops/sec |
| Kafka (single partition) | ~100 MB/s throughput |
| CDN | Virtually unlimited reads (cached) |
| Single App server | ~10K requests/sec |

---

## Architecture component decision tree

| Need | Component |
|------|-----------|
| High-read traffic, repeated queries | Cache (Redis) |
| Offload heavy work from request path | Message queue (Kafka, BullMQ) |
| Store relational business data | PostgreSQL |
| Store unstructured/flexible documents | MongoDB |
| Serve static assets, reduce latency globally | CDN |
| Route traffic to multiple app servers | Load balancer |
| Centralize logs from all services | Log aggregation (ELK, Loki) |
| Track metrics and alert | Prometheus + Grafana |
| Search with text scoring | Elasticsearch |
| Real-time bidirectional communication | WebSockets |
| Rate limiting, auth at the edge | API Gateway |
| Decouple services, fan out to multiple consumers | Event bus |

---

## Failure modes to always consider

For any system, ask these questions:
1. What happens if the database goes down?
2. What happens if the cache goes down? Does the system degrade gracefully?
3. What happens if an external dependency (email, payment, AI) goes down?
4. What happens if a message in the queue is processed twice?
5. What happens if a node in the cluster fails mid-request?
6. What happens when traffic spikes 10x?
7. What is the worst-case read latency under full load?
8. What happens if a migration runs on a table with 100M rows?

---

## Tradeoff pairs — know both sides

| Tradeoff | Left | Right |
|----------|------|-------|
| Consistency vs availability | Strong consistency (PostgreSQL, transactions) | Eventual consistency (Redis, MongoDB with default settings) |
| SQL vs NoSQL | ACID, joins, schema enforcement | Flexible schema, horizontal scaling, schema-less |
| Synchronous vs async | Simpler client, immediate response | Decoupled, more reliable for heavy work, worse UX for immediate feedback |
| Monolith vs microservices | Simpler to build and debug | Independent scaling, independent deployment, more complexity |
| Cache-aside vs write-through | App controls cache, stale on miss | Always fresh cache, writes slower |
| Fanout on write vs read | Feed is prebuilt, fast reads | No storage overhead, celeb problem avoided |
| Normalization vs denormalization | No duplication, harder to query | Duplicated data, fast reads |
| Replication vs sharding | High availability, all data on all replicas | Horizontal scale, data partitioned |

---

## My personal weaknesses (update after each drill)

| After system design | What I consistently underdesign | What I got right |
|--------------------|---------------------------------|------------------|
| URL Shortener (Day 29) | | |
| Notification System (Day 43) | | |
| Distributed Cache (Day 44) | | |
| Chat System (Day 45) | | |
| News Feed (Day 46) | | |
| Video Streaming (Day 47) | | |
| Ride-Hailing (Day 86) | | |

---

## Template for writing a design doc (all components in order)

```
## Requirements
### Functional
- [List what the system does]

### Non-functional
- Availability: [X%]
- Latency: [p99 < Xms]
- Scale: [X DAU, X QPS]
- Consistency: [strong/eventual]

## Scale Estimation
- DAU: X million
- Requests/user/day: X
- Peak QPS: X
- Storage per day: X GB
- Total storage (3 years): X TB

## API Design
POST   /resource         - Create
GET    /resource/{id}    - Read by ID
GET    /resources        - List (paginated)
PUT    /resource/{id}    - Update
DELETE /resource/{id}    - Delete

## Data Model
Table/Collection: [name]
- id: UUID
- field: type (constraints)
- created_at: timestamp

## High-Level Architecture
[Text diagram or description of components]

## Core Algorithm / Critical Component
[Deep dive on the hardest or most interesting part]

## Bottlenecks
- [Bottleneck 1]: [Impact and mitigation]
- [Bottleneck 2]: [Impact and mitigation]

## Tradeoffs
- [Choice A vs Choice B]: [Why you chose A]
```
