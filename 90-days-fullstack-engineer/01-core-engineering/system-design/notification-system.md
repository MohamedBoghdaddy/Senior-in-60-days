# Notification System

## Requirements
- Deliver push, email, and in-app notifications.
- Support user preferences and rate limits.
- Guarantee at-least-once delivery for critical alerts.

## Scale estimation
- 20M notifications per day.
- 50K outbound messages per minute.
- 5M preference lookups per day.

## APIs
- `POST /notifications` - create a notification.
- `GET /notifications/{user_id}` - list user notification history.
- `PATCH /notifications/{id}/read` - acknowledge delivery.

## Data model
- `notification(id, user_id, channel, payload, status, created_at)`
- `notification_preferences(user_id, channel, enabled, quiet_hours)`

## High-level architecture
- Ingestion service validates messages.
- Queue broker handles delivery retries.
- Worker processes send messages through external channels.
- Audit store preserves delivery results.

## Critical components
- **Preference engine**: evaluate channel eligibility.
- **Retry strategy**: exponential backoff and dead-letter queue.
- **Fallback policy**: escalate push failure to email for critical alerts.

## Scaling strategy
- Batch notifications for throughput.
- Use a dedicated queue for high-priority traffic.
- Store historical delivery state in a relational store.

## Bottlenecks
- External provider rate limits.
- Queue growth during outage recovery.
- Preference evaluation on each send.

## Tradeoffs
- Immediate delivery vs batching for cost control.
- Multi-channel fallback vs notification noise.
- Storing every notification history vs summary retention.
