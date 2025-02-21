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
    options: List[str] = [] 

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
    highlight_words, highlight_style = extract_settings(settings)
    return apply_highlighting(message, highlight_words, highlight_style)

def extract_settings(settings: List[Setting]) -> tuple:
    """Extracts the words to highlight and the highlight style."""
    highlight_words = []
    highlight_style = "bold"  

    for setting in settings:
        if setting.label == "highlightWords":
            highlight_words = setting.default.split(",")
        elif setting.label == "highlightStyle":
            highlight_style = setting.default.lower()

    return highlight_words, highlight_style

def apply_highlighting(message: str, keywords: List[str], style: str) -> str:
    """Applies the chosen highlight style to keywords in the message."""

    def style_word(match):
        word = match.group(0)
        if style == "bold":
            return f"<span style='font-weight: bold;'>{word}</span>"
        elif style == "italic":
            return f"<span style='font-style: italic;'>{word}</span>"
        elif style == "uppercase":
            return word.upper()
        elif style == "strikethrough":
            return f"<span style='text-decoration: line-through;'>{word}</span>"
        elif style == "underline":
            return f"<span style='text-decoration: underline;'>{word}</span>"
        elif style == "red-color":
            return f'<span style="color: red;">{word}</span>'
        elif style == "yellow-background":
            return f'<span style="background-color: yellow;">{word}</span>'
        elif style == "emoji":
            return f" {word} 🔥"
        return word

    if not keywords:
        return message  

    # Sort keywords to prioritize longer words first
    keywords = sorted(set(keywords), key=len, reverse=True)
    
    # Use a regex pattern that ensures whole-word matching
    pattern = r"\b(" + "|".join(map(re.escape, keywords)) + r")\b"
    modified_message = re.sub(pattern, style_word, message, flags=re.IGNORECASE)

    return modified_message
