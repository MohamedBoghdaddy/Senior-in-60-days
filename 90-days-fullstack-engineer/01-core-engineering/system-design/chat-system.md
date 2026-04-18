# Chat System

## Requirements
- Real-time messaging between users.
- Presence indicators and message delivery status.
- Message history storage and search.
- Support mobile and web clients.

## Scale estimation
- 10M users.
- 500K concurrent sessions.
- 100K messages per second peak.

## APIs
- `POST /messages` - send a message.
- `GET /conversations/{id}` - fetch history.
- `POST /presence` - update availability.

## Data model
- `conversation(id, type, participants, updated_at)`
- `message(id, conversation_id, sender_id, text, status, created_at)`

## High-level architecture
- WebSocket gateway for real-time events.
- Backend service for persistence and business rules.
- Message broker for fan-out and retries.
- Search index for conversation lookup.

## Critical components
- **Delivery pipeline**: accept, persist, publish, acknowledge.
- **Presence store**: lightweight connection registry in Redis.
- **History service**: paginated reads from PostgreSQL or document store.

## Scaling strategy
- Partition conversations by conversation id.
- Use horizontal WebSocket nodes behind sticky session handling.
- Keep message transport decoupled from storage.

## Bottlenecks
- Fan-out of group chat.
- Message ordering under distributed delivery.
- Hot conversation read/write hotspots.

## Tradeoffs
- Real-time persistence vs eventual consistency for delivery receipts.
- Using a single broker vs multiple topic namespaces.
- WebSockets for UX vs backpressure and connection management overhead.
