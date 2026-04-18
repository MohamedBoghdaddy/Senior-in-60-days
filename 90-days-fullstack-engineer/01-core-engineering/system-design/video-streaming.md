# Video Streaming

## Requirements
- Deliver video content to web and mobile clients.
- Support adaptive bitrate, CDN integration, and analytics.
- Handle VOD and live streaming use cases.

## Scale estimation
- 5M concurrent viewers during peak events.
- 50K video uploads per day.
- 500K playbacks per minute.

## APIs
- `POST /videos` - upload metadata and generate processing jobs.
- `GET /videos/{id}` - retrieve playback metadata.
- Streaming is served through CDN endpoints.

## Data model
- `video(id, owner_id, title, status, storage_key, created_at)`
- `encoding_job(id, video_id, resolution, status, started_at, finished_at)`

## High-level architecture
- Upload service generates ingestion and encoding jobs.
- Processing pipeline transcodes and stores multiple renditions.
- Metadata service tracks content and playback URLs.
- CDN caches delivery at the edge.

## Critical components
- **Encoding pipeline**: job orchestration and retries.
- **Playback metadata service**: signed URLs, DRM tags.
- **Analytics**: collect play events and error rates.

## Scaling strategy
- Separate ingestion from processing.
- Use object storage for large files.
- Cache CDN edge responses and metadata for hot assets.

## Bottlenecks
- Encoding cluster capacity.
- Large object upload and storage throughput.
- Hot popular videos causing origin load.

## Tradeoffs
- Offloading to external CDN vs owning delivery.
- Pre-encoding all renditions vs on-demand packaging.
- DRM complexity vs open playback.
