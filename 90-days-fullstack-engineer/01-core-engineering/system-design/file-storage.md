# File Storage

## Requirements
- Upload and retrieve files securely.
- Support metadata, access control, and versioning.
- Integrate with CDN or object storage.

## Scale estimation
- 100TB of stored objects.
- 50K upload/download requests per second.
- 1M active users.

## APIs
- `POST /files` - upload metadata and generate signed upload URL.
- `GET /files/{id}` - retrieve file metadata and download URL.
- `DELETE /files/{id}` - soft delete or archive.

## Data model
- `file_object(id, owner_id, storage_key, status, uploaded_at)`
- `file_version(id, file_id, version_number, checksum, created_at)`

## High-level architecture
- API service for metadata and access policy.
- Object store for binary content.
- Cache for signed URLs and metadata.
- Background cleanup job for expired file references.

## Critical components
- **Signed upload/download**: avoid proxying large files through the API.
- **Access policy enforcement**: check user and role before returning URLs.
- **Lifecycle rules**: automated archive or deletion for old files.

## Scaling strategy
- Store binaries in S3-compatible storage.
- Use CDN for file delivery.
- Keep metadata in a relational database and large content offloaded.

## Bottlenecks
- Hot object store throughput with large files.
- Metadata consistency between DB and object storage.
- Expensive scans for orphan cleanup.

## Tradeoffs
- Proxying files vs signed URLs.
- Immediate deletion vs soft-delete for recovery.
- Using object storage vs local persistence for speed and durability.
