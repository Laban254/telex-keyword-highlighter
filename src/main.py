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
    modified_message = process_highlight(request.message, request.settings)
    return {"message": modified_message}

def process_highlight(message: str, settings: List[Setting]) -> str:
    """Applies keyword highlighting based on the settings provided."""
    highlight_words, highlight_style, highlight_color, highlight_bg, highlight_emoji = extract_settings(settings)
    return apply_highlighting(message, highlight_words, highlight_style, highlight_color, highlight_bg, highlight_emoji)

def extract_settings(settings: List[Setting]) -> tuple:
    """Extracts the words to highlight, the highlight style, color, background, and emoji setting."""
    highlight_words = []
    highlight_style = "bold"
    highlight_color = "red"
    highlight_bg = "yellow"
    highlight_emoji = True

    for setting in settings:
        if setting.label == "highlightWords":
            highlight_words = setting.default.split(",")
        elif setting.label == "highlightStyle":
            highlight_style = setting.default.lower()
        elif setting.label == "highlightColor":
            highlight_color = setting.default.lower()
        elif setting.label == "highlightBackgroundColor":
            highlight_bg = setting.default.lower()
        elif setting.label == "highlightWithEmoji":
            highlight_emoji = setting.default

    return highlight_words, highlight_style, highlight_color, highlight_bg, highlight_emoji

def apply_highlighting(message: str, keywords: List[str], style: str, color: str, background: str, use_emoji: bool) -> str:
    """Applies the chosen highlight styles to keywords in the message."""
    def style_word(match):
        word = match.group(0)
        styled_word = word
        
        if use_emoji:
            styled_word = f"🔥 {styled_word} 🔥"
        if style == "bold":
            styled_word = f"**{styled_word}**"
        elif style == "italic":
            styled_word = f"*{styled_word}*"
        elif style == "uppercase":
            styled_word = styled_word.upper()
        
        return styled_word
    
    if not keywords:
        return message
    
    keywords = sorted(set(keywords), key=len, reverse=True)
    pattern = r"\b(" + "|".join(map(re.escape, keywords)) + r")\b"
    modified_message = re.sub(pattern, style_word, message, flags=re.IGNORECASE)

    return modified_message
