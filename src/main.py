from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
from typing import List, Any
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

@app.post("/highlight-message")
async def modify_message(request: ModifierRequest):
    """Modifies incoming messages based on settings (Keyword Highlighter)."""
    modified_message = process_highlight(request.message, request.highlightWords, request.settings)
    return {"message": modified_message}

def process_highlight(message: str, highlight_words: List[str], settings: Dict[str, Dict[str, Any]]) -> str:
    """Applies keyword highlighting based on user-selected words and settings."""
    return apply_highlighting(message, highlight_words, settings)

def apply_highlighting(message: str, highlight_words: List[str], keyword_settings: Dict[str, Dict[str, Any]]) -> str:
    """Dynamically applies custom highlight styles per keyword."""
    
    def style_word(match):
        word = match.group(0)
        lower_word = word.lower()
        settings = keyword_settings.get(lower_word, {})
        styled_word = word  # Preserve original casing
        
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

    # Sorting ensures longer words are matched first, avoiding partial replacements
    highlight_words = sorted(highlight_words, key=len, reverse=True)
    pattern = r"\b(" + "|".join(map(re.escape, highlight_words)) + r")\b"
    modified_message = re.sub(pattern, style_word, message, flags=re.IGNORECASE)

    return modified_message