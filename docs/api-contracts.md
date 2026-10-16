# API contracts

Initial endpoints from the product architecture:

| Endpoint | Purpose |
| --- | --- |
| `GET /health` | Container and platform health check |
| `POST /reports` | Save an extracted farmer report |
| `GET /reports/nearby` | Retrieve recent reports near a location |
| `GET /context/{report_id}` | Return combined report and supporting evidence |
| `POST /recommendations/{report_id}` | Create and persist a recommendation |
| `GET /dashboard/reports` | Supply incidents and dashboard filters |

The first scaffold only implements `GET /health`. The remaining routes should be added alongside agreed request/response schemas before the workstreams are integrated.

