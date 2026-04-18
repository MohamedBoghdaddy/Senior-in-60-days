# Incident: API Failure

## Timeline

- 11:05 UTC: Alerts triggered for elevated 500 responses on `/api/listings`.
- 11:07 UTC: Engineers confirmed backend service returning `500` on search calls.
- 11:15 UTC: Traffic was rerouted to healthy replicas and cache fallback behavior was verified.
- 11:30 UTC: root cause identified and temporary rollback completed.

## Root cause

- A recent dependency update caused a database query helper to throw when a null filter was passed.

## Impact

- `GET /api/listings` failed for 100% of user requests.
- Dashboard and listing search were unavailable.

## Mitigation and resolution

- Rolled back the deployment to the previous stable backend image.
- Added a validation guard for search parameters.
- Recovered service by 11:40 UTC.

## Prevention

- Add a regression test for empty search filters.
- Introduce a minor feature flag for query helper changes.
- Expand synthetic monitoring to include search endpoint payload variants.
