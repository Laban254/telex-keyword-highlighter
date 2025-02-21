from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
from typing import List, Any, Dict
from src.integration_json import INTEGRATION_JSON 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Setting(BaseModel):
    label: str
    type: str
    required: bool
    default: Any

class ModifierRequest(BaseModel):
    message: str
    settings: List[Setting]

@app.get("/integration.json")
def get_integration_json():
    """Returns integration metadata."""
    return INTEGRATION_JSON

class ModifierRequest(BaseModel):
    message: str
    settings: Dict[str, Dict[str, Any]]  # Dictionary where each keyword has its own settings

@app.post("/highlight-message")
async def modify_message(request: ModifierRequest):
    """Modifies incoming messages based on settings (Keyword Highlighter)."""
    modified_message = process_highlight(request.message, request.settings)
    return {"message": modified_message}

def process_highlight(message: str, settings: Dict[str, Dict[str, Any]]) -> str:
    """Applies keyword highlighting based on the settings provided."""
    keywords = list(settings.keys())  # Extract keywords from settings dictionary
    return apply_highlighting(message, keywords, settings)

def apply_highlighting(message: str, highlight_words, keyword_settings: Dict[str, Dict[str, Any]]) -> str:
    """Applies custom highlight styles per keyword."""
    
    def style_word(match):
        word = match.group(0)  # Preserve original case
        lower_word = word.lower()
        settings = keyword_settings.get(lower_word, {})
        styled_word = word
        
        if settings.get("emoji", False):
            styled_word = f"🔥 {styled_word} 🔥"
        if settings.get("bold", False):
            styled_word = f"**{styled_word}**"
        if settings.get("italic", False):
            styled_word = f"*{styled_word}*"
        if settings.get("uppercase", False):
            styled_word = styled_word.upper()
        
        return styled_word
    
    if not highlight_words:
        return message
    
    keywords = sorted(highlight_words, key=len, reverse=True)
    pattern = r"\b(" + "|".join(map(re.escape, keywords)) + r")\b"
    modified_message = re.sub(pattern, style_word, message, flags=re.IGNORECASE)

    return modified_message