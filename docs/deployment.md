# Azure deployment plan

## Resources

- Azure Container Apps environment
- Azure Container Registry
- Azure SQL Database
- Azure Key Vault
- Application Insights / Log Analytics
- Azure OpenAI
- Azure AI Speech
- Azure Communication Services

## Container apps

| App | Image | Ingress |
| --- | --- | --- |
| `farmer-api` | `docker/api.Dockerfile` | External HTTPS for API and phone webhooks |
| `officer-dashboard` | `docker/dashboard.Dockerfile` | External HTTPS protected by Entra ID |
| `sensor-simulator` | `docker/simulator.Dockerfile` | No ingress; optional scheduled job |

Do not containerize Azure SQL, Speech, OpenAI, or the weather provider. They are managed/external dependencies configured through environment variables and secrets.

The initial deployment can use public ingress for the API and dashboard. Before handling real farmer data, add authentication, restrict dashboard access, use approximate locations where appropriate, and move secrets to Key Vault.

