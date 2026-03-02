from fastapi import FastAPI, HTTPException
from app.providers.llama8b import Llama8BProvider
from app.insight.generator import generate_insight
from app.insight.schema import InsightInput

app = FastAPI(title="AssetFlow AI Service", version="0.1.0")
provider = Llama8BProvider()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate-insight")
def generate_insight_endpoint(payload: InsightInput):
    try:
        return generate_insight(provider, payload.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))