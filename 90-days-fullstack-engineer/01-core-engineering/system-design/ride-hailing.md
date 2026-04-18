# Ride-Hailing

## Requirements
- Customer ride request and driver matching.
- Real-time driver location updates.
- Pricing, dispatch, and trip lifecycle management.

## Scale estimation
- 5M riders.
- 500K active drivers.
- 200K trip requests per minute in peak regions.

## APIs
- `POST /rides` - request a ride.
- `GET /drivers/nearby` - find nearby drivers.
- `PATCH /rides/{id}` - update ride status.

## Data model
- `ride(id, rider_id, driver_id, status, pickup_location, dropoff_location, requested_at)`
- `driver_status(driver_id, location, availability, updated_at)`
- `pricing(ride_id, base_fare, distance_fare, surge_multiplier)`

## High-level architecture
- Mobile apps communicate with an API gateway.
- Matching service evaluates availability and ETA.
- Real-time location platform updates driver position.
- Billing service finalizes pricing and receipts.

## Critical components
- **Dispatch engine**: prioritize nearby drivers and capacity.
- **Availability cache**: keep driver state in Redis for fast lookup.
- **Trip state machine**: enforce ride lifecycle consistency.

## Scaling strategy
- Partition drivers by region.
- Use event streams for location updates.
- Apply backpressure on request spikes using queueing.

## Bottlenecks
- Real-time location update flood.
- Near-neighbor searches under load.
- Surge pricing data freshness.

## Tradeoffs
- Strong consistency for driver assignment vs faster approximate matching.
- In-memory location cache vs persistent history.
- Push-based status updates vs polling.
