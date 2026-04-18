# Incident: External Dependency Failure

## Timeline

- 18:20 UTC: AI service started returning 502 errors from the external provider.
- 18:25 UTC: Backend retry logs showed repeated failed attempts.
- 18:30 UTC: AI service switched to fallback response behavior.
- 18:45 UTC: Provider outage resolved and full traffic resumed.

## Root cause

- External AI provider experienced a service outage.

## Impact

- AI insight pages returned degraded fallback results.
- Non-critical enrichment data was delayed, but primary platform flows remained available.

## Mitigation and resolution

- Implemented fallback output with a warning when the AI provider was unavailable.
- Added retry logic with exponential backoff in the AI service.
- Verified user-facing pages gracefully handled degraded responses.

## Prevention

- Document alternative providers and integration fallbacks.
- Add alerting for AI provider error rates and provider-side latency.
- Cache previous successful AI responses for critical content.
