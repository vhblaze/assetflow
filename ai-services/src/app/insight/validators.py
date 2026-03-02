import json
import re
from typing import Any, Dict, Optional, List
from .prompts import ALLOWED_TAGS

BANNED_PHRASES = [
    "é recomendável", "recomendo", "aconselho",
    "você deve", "deve ", "deveria",
    "ajuste", "ajustar", "estratégia",
    "compre", "compra", "venda", "vender",
    "reduza", "reduzir", "aumente", "aumentar",
    "considere", "considerar",

    "recommend", "recommended",
    "should", "must", "consider",
    "adjust", "buy", "sell", "increase", "reduce",
]

def _contains_banned_language(text: str) -> bool:
    t = (text or "").lower()
    return any(p in t for p in BANNED_PHRASES)

def extract_json(text: str) -> Optional[Dict[str, Any]]:
    """Try to extract a valid JSON object from a text."""
    if not text:
        return None

    text = re.sub(r"```json\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None

    raw = text[start:end + 1].strip()

    try:
        obj = json.loads(raw)
        if isinstance(obj, dict):
            return obj
        return None
    except Exception:
        return None

def normalize_tags(tags: Any) -> List[str]:
    """Normalize tags into a deduplicated, allowed list."""
    if isinstance(tags, list):
        raw = [str(t).strip() for t in tags if str(t).strip()]
    elif isinstance(tags, str):
        raw = [t.strip() for t in tags.split(",") if t.strip()]
    else:
        raw = ["overview"]

    out: List[str] = []
    seen = set()
    for t in raw:
        if t in ALLOWED_TAGS and t not in seen:
            seen.add(t)
            out.append(t)

    return out or ["overview"]

def _safe_float(value: Any, default: float = 0.5) -> float:
    """Parse float robustly (handles '0,8' or None)."""
    try:
        if isinstance(value, str):
            value = value.replace(",", ".").strip()
        return float(value)
    except Exception:
        return default

def normalize_insight(obj: Dict[str, Any], default_disclaimer: str) -> Optional[Dict[str, Any]]:
    """
    Normalize and validate the insight output.
    Returns None if invalid or if banned/prescriptive language is detected.
    """
    try:
        headline = str(obj.get("headline", "")).strip()
        message = str(obj.get("message", "")).strip()
        tags = normalize_tags(obj.get("tags", ["overview"]))
        confidence = _safe_float(obj.get("confidence", 0.5), default=0.5)
        disclaimer = default_disclaimer
    except Exception:
        return None

    if not headline or not message:
        return None

    if _contains_banned_language(f"{headline} {message}"):
        return None

    confidence = max(0.0, min(1.0, confidence))

    headline = headline[:120]
    message = message[:600]

    return {
        "headline": headline,
        "message": message,
        "tags": tags,
        "confidence": confidence,
        "disclaimer": disclaimer,
    }

def parse_four_lines(text: str) -> Optional[Dict[str, Any]]:
    """
    Parse the "4-line" format:
      HEADLINE: ...
      MESSAGE: ...
      TAGS: tag1, tag2
      CONFIDENCE: 0.7
    """
    if not text:
        return None

    text = re.sub(r"```.*?\n", "", text, flags=re.DOTALL)
    text = text.replace("```", "").strip()

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) < 4:
        return None

    def get_value(prefix: str) -> Optional[str]:
        pref = prefix.upper()
        for ln in lines:
            if ln.upper().startswith(pref):
                return ln.split(":", 1)[1].strip() if ":" in ln else None
        return None

    headline = get_value("HEADLINE")
    message = get_value("MESSAGE")
    tags_raw = get_value("TAGS")
    conf_raw = get_value("CONFIDENCE")

    if not headline or not message or not tags_raw or not conf_raw:
        return None

    if _contains_banned_language(f"{headline} {message}"):
        return None

    tags = normalize_tags(tags_raw)

    confidence = _safe_float(conf_raw, default=0.5)
    confidence = max(0.0, min(1.0, confidence))

    return {
        "headline": headline,
        "message": message,
        "tags": tags,
        "confidence": confidence,
    }