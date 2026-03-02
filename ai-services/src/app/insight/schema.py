from pydantic import BaseModel
from typing import Dict, List, Optional

class InsightInput(BaseModel):
    date: str
    locale: str = "pt-BR"
    risk_profile: Optional[str] = None
    metrics: Dict[str, float]
    alerts: List[str] = []