import json
from typing import Any, Dict
from app.providers.base import BaseProvider
from . import prompts
from .validators import extract_json, normalize_insight, parse_four_lines

def default_disclaimer(locale: str) -> str:
    return prompts.DISCLAIMER_PT if (locale or "").lower().startswith("pt") else prompts.DISCLAIMER_EN

def minimize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "date": payload.get("date"),
        "locale": payload.get("locale", "pt-BR"),
        "risk_profile": payload.get("risk_profile"),
        "metrics": payload.get("metrics", {}),
        "alerts": payload.get("alerts", []),
    }

def build_user_prompt(payload_min: Dict[str, Any]) -> str:
    return (
        "Gere um insight diário com base no payload abaixo.\n\n"
        f"Payload:\n{json.dumps(payload_min, ensure_ascii=False)}"
    )

def generate_insight(provider: BaseProvider, payload: Dict[str, Any]) -> Dict[str, Any]:
    payload_min = minimize_payload(payload)
    user_prompt = build_user_prompt(payload_min)

    locale = payload_min.get("locale", "pt-BR")
    disclaimer = default_disclaimer(locale)

    # Attempt 1 (PT JSON strict)
    text1 = provider.chat(prompts.SYSTEM_JSON_PT, user_prompt, max_tokens=220)
    obj1 = extract_json(text1)
    norm1 = normalize_insight(obj1, default_disclaimer=disclaimer) if obj1 else None
    if norm1:
        return norm1

    # Attempt 2 (EN JSON strict)
    text2 = provider.chat(prompts.SYSTEM_JSON_EN_STRICT, user_prompt, max_tokens=220)
    obj2 = extract_json(text2)
    norm2 = normalize_insight(obj2, default_disclaimer=disclaimer) if obj2 else None
    if norm2:
        return norm2

    # Attempt 3 (4 lines)
    text3 = provider.chat(prompts.SYSTEM_4LINES, user_prompt, max_tokens=180)
    obj3 = parse_four_lines(text3)
    if obj3:
        obj3["disclaimer"] = disclaimer
        norm3 = normalize_insight(obj3, default_disclaimer=disclaimer)
        if norm3:
            return norm3

    # Fallback final (sempre retorna)
    return {
        "headline": "Resumo do dia",
        "message": "Não foi possível gerar um insight completo hoje. Tente novamente mais tarde.",
        "tags": ["overview"],
        "confidence": 0.3,
        "disclaimer": disclaimer,
    }