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
    description: str

class HighlightRequest(BaseModel):
    channel_id: str
    settings: List[Setting]
    message: str

@app.get("/integration.json")
def get_integration_json():
    """Returns integration metadata."""
    return INTEGRATION_JSON

@app.post("/highlight-message")
def highlight_text(request: HighlightRequest):
    """Highlights keywords in a given message based on user settings."""
    highlighted_message = process_highlight(request)
    return {
        "event_name": "message_highlighted",
        "message": highlighted_message,
        "status": "success",
        "username": "keyword-highlighter-bot"
    }

def process_highlight(request: HighlightRequest) -> str:
    """Processes the message and applies keyword highlighting."""
    
    highlight_words, highlight_style = extract_settings(request.settings)
    return apply_highlighting(request.message, highlight_words, highlight_style)

def extract_settings(settings: List[Setting]) -> tuple:
    """Extracts the highlight words and style from settings."""
    
    highlight_words = []
    highlight_style = "bold"  

    for setting in settings:
        if setting.label == "highlightWords":
            highlight_words = setting.default.split(",") 
        elif setting.label == "highlightStyle":
            highlight_style = setting.default.lower()

    return highlight_words, highlight_style

def apply_highlighting(message: str, keywords: List[str], style: str) -> str:
    """Applies highlighting to specified keywords in the message."""
    
    def style_word(match):
        word = match.group(0)
        if style == "bold":
            return f"**{word}**"
        elif style == "italic":
            return f"*{word}*"
        elif style == "uppercase":
            return word.upper()
        return word  

    highlighted_message = message
    for keyword in sorted(keywords, key=len, reverse=True):
        highlighted_message = re.sub(rf"\b{re.escape(keyword)}\b", style_word, highlighted_message, flags=re.IGNORECASE)

    return highlighted_message
