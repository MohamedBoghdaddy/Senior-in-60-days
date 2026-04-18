# Scaling Plan

## Initial scale
- Single backend instance behind a load balancer.
- One Redis instance, one PostgreSQL replica, one MongoDB replica.
- Focus on correctness and observability.

## Medium scale
- Add Redis cluster and separate cache roles.
- Scale backend horizontally with stateless API servers.
- Add read replicas for PostgreSQL and MongoDB.

## High scale
- Use partitioning for hot tables and workload-specific MongoDB collections.
- Move AI service to separate autoscaling deployment.
- Introduce rate limiting at the gateway and request-level throttling.
- Add metrics dashboards for latency, queue depth, and cache hit rate.

## Failure mitigation
- Use circuit breakers for external AI service calls.
- Use dead-letter queues for failed background jobs.
- Use monitoring alerts for DB slow queries and cache saturation.
