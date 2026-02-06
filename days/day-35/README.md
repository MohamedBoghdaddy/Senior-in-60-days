# Day 35 — MongoDB Decision & Setup
![Day](https://img.shields.io/badge/Day-35-blue) ![Area](https://img.shields.io/badge/Area-db-lightgrey) ![Priority](https://img.shields.io/badge/Priority-P0-red)

---
### Focus

Decide on and set up a MongoDB module for activity feeds or analytics.
### Timebox

~3 hours
### Study

- [MongoDB Atlas documentation](https://www.mongodb.com/docs/atlas/)
- [Bucket pattern for time series](https://www.mongodb.com/presentations/data-modeling-time-series-event-bucket-pattern)
### Build

1. Evaluate use cases for MongoDB (activity feed vs analytics) and decide which to implement.
1. Set up a connection to MongoDB (e.g., using Mongoose or the native driver).
1. Define schemas for the chosen use case (e.g., event buckets or aggregated metrics).
1. Plan indexing strategy for efficient queries.
### Assignments

- Commit MongoDB configuration and schema definitions.
- Write an ADR explaining why MongoDB was chosen for this feature.
### DoD Checklist

- [ ] Connection to MongoDB established.
- [ ] Schemas defined for selected use case.
- [ ] ADR capturing decision and trade-offs created.
### Commit Message

`feat(mongo): decide on use case and set up MongoDB with schemas`
### Outcome Artifacts

- Mongo configuration files and models.
- ADR in `/docs/adrs` for MongoDB decision.
### Self‑Review Questions

- Why is MongoDB a better fit than Postgres for this feature?
- What potential challenges might arise with the chosen use case?
