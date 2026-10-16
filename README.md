# Farmer Advisory & Early-Warning System

MVP scaffold for a farmer hotline that turns spoken reports into structured incidents, enriches them with nearby history, weather, and sensor readings, and presents recommendations to farmers and agricultural officers.

## Architecture

This project is intentionally a modular monolith for the hackathon:

- `farmer-api`: FastAPI backend containing the domain modules and API contracts.
- `officer-dashboard`: Streamlit dashboard consuming the backend API.
- Azure SQL Database: persistent application data.
- Azure AI Speech, Azure OpenAI, Azure Communication Services: voice and AI capabilities.
- Open-Meteo and simulated/physical sensors: external evidence sources.

The backend and dashboard are separate Docker images. The logical capabilities inside the backend are modules, not separate microservices.

See [docs/architecture.md](docs/architecture.md), [docs/api-contracts.md](docs/api-contracts.md), and [docs/deployment.md](docs/deployment.md).

## Prerequisites

- Python 3.11 or newer
- `pip` and `venv`
- Docker Desktop, only if you want to run the containers locally
- Azure resources are not required for the current scaffold

## Run locally

Clone the repository and create an isolated Python environment:

```bash
git clone https://github.com/es1a/hackathon-bcg.git
cd hackathon-bcg

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dashboard,dev]'
cp .env.example .env
```

Start the API:

```bash
uvicorn api.main:app --reload --app-dir src
```

The API is available at `http://localhost:8000`.

- Swagger UI: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

In a second terminal, activate the same virtual environment and start the dashboard:

```bash
source .venv/bin/activate
streamlit run src/dashboard/app.py
```

The dashboard is available at `http://localhost:8501`. It is currently a UI scaffold and does not yet display live incidents.

Run the automated checks:

```bash
python -m pytest
python -m compileall -q src tests
```

## Run with Docker

Build the images from the repository root:

```bash
docker build -f docker/api.Dockerfile -t farmer-api .
docker build -f docker/dashboard.Dockerfile -t officer-dashboard .
```

Run the API container:

```bash
docker run --rm --name farmer-api -p 8000:8000 farmer-api
```

Run the dashboard container in a second terminal:

```bash
docker run --rm --name officer-dashboard -p 8501:8501 officer-dashboard
```

The containers currently expose the health endpoint and dashboard scaffold. They do not yet require Azure credentials.

## Configuration

`.env.example` lists the configuration expected by the planned integrations. Copy it to `.env` for local development and populate Azure values only when those integrations are implemented.

Never commit `.env` or real credentials. In Azure, provide secrets through Key Vault and managed identity rather than storing them in the repository.

## Azure deployment direction

The intended deployment has two primary Azure Container Apps:

1. `farmer-api`, built from `docker/api.Dockerfile`
2. `officer-dashboard`, built from `docker/dashboard.Dockerfile`

The optional sensor simulator will run as a scheduled Container Apps Job. Azure SQL, Azure OpenAI, Azure AI Speech, Azure Communication Services, Key Vault, and Application Insights are managed dependencies rather than application containers.

See [docs/deployment.md](docs/deployment.md) for the resource plan and [infra/README.md](infra/README.md) for the infrastructure-as-code roadmap.

## Current implementation status

- API health endpoint: implemented
- Dashboard shell: implemented
- Docker build definitions: implemented
- Database migrations: not implemented yet
- Farmer report and recommendation endpoints: planned
- Speech, LLM, weather, sensor, and telephony integrations: planned
- Azure infrastructure-as-code: planned

## Repository layout

```text
src/api/          HTTP routes and application entry point
src/domain/       schemas and business rules
src/services/     speech, extraction, aggregation, weather, sensors, recommendations
src/repositories/ persistence boundaries
src/dashboard/    officer-facing Streamlit application
database/         migrations and seed-data notes
infra/            Azure deployment notes and future Bicep modules
docker/           container build definitions
tests/            unit, integration, and end-to-end tests
```
