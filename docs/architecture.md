# Architecture

## MVP deployment shape

```text
Azure Container Apps Environment
├── farmer-api          external HTTPS ingress
├── officer-dashboard   external HTTPS ingress + officer authentication
└── sensor-simulator    optional scheduled job

Azure SQL Database, Key Vault, Application Insights, Azure AI Speech,
Azure OpenAI, Azure Communication Services, and external weather API
```

The API is the only application component that talks directly to SQL. The dashboard calls API endpoints, keeping authorization and business logic centralized.

## Module boundaries

- `api`: transport and request validation only.
- `domain`: report, observation, recommendation, and risk concepts.
- `services`: integrations and orchestration workflows.
- `repositories`: database access abstractions.
- `dashboard`: presentation only; it should not contain recommendation logic.

For the MVP, these remain in one backend deployment. They can become independently deployed services later if scale or team ownership requires it.

