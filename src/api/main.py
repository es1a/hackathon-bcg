from fastapi import FastAPI


app = FastAPI(
    title="Farmer Advisory API",
    version="0.1.0",
    description="API scaffold for farmer reports, evidence aggregation, and recommendations.",
)


@app.get("/health", tags=["platform"])
def health() -> dict[str, str]:
    """Return a lightweight health response for local and Azure probes."""

    return {"status": "ok", "service": "farmer-api"}

