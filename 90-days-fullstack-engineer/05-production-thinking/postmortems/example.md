# Postmortem: API Failure on Listing Search

## Incident summary

- A recent backend deployment caused `GET /api/listings` to return 500 errors.
- The issue occurred on `main` at 11:05 UTC.
- Users could not access listing search or dashboard data.

## Timeline

- 11:05 UTC: error rate alert triggered.
- 11:07 UTC: error confirmed in backend logs.
- 11:10 UTC: rollback decision made.
- 11:17 UTC: rollback executed.
- 11:20 UTC: service recovered.

## Root cause

- A change in query helper did not handle null search filters correctly, causing an exception on the backend.

## Impact

- Search and dashboard requests failed for all signed-in users.
- Business analytics were disrupted during the incident.

## Mitigation and resolution

- Rolled back to the last known good backend image.
- Added defensive handling for empty search filters.
- Deployed a fixed version after validation.

## Prevention

- Add unit tests for search request handling.
- Build a regression test for null filters.
- Introduce synthetic monitoring for search endpoint with empty query cases.

## Lessons learned

- Feature rollouts require stronger input validation coverage.
- The team should maintain a rollback plan for service deployments.
- Faster detection of query helper changes can reduce MTTR.
