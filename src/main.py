from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
from typing import List, Any
from src.integration_json import INTEGRATION_JSON  # Ensure this exists and is correctly formatted

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

# ANSI color codes for CLI styling
COLOR_STYLES = {
    "red": lambda word: f"\033[31m{word}\033[0m",
    "green": lambda word: f"\033[32m{word}\033[0m",
    "blue": lambda word: f"\033[34m{word}\033[0m",
    "yellow": lambda word: f"\033[33m{word}\033[0m",
    "bg_red": lambda word: f"\033[41m{word}\033[0m",
    "bg_green": lambda word: f"\033[42m{word}\033[0m",
    "bg_yellow": lambda word: f"\033[43m{word}\033[0m",
    "bold": lambda word: f"**{word}**",
    "italic": lambda word: f"*{word}*",
    "uppercase": lambda word: word.upper(),
}

def process_highlight(message: str, settings: List[Setting]) -> str:
    """Applies keyword highlighting based on the settings provided."""
    highlight_words, highlight_style, text_color, bg_color = extract_settings(settings)
    return apply_highlighting(message, highlight_words, highlight_style, text_color, bg_color)

def extract_settings(settings: List[Setting]) -> tuple:
    """Extracts the words to highlight, styles, text color, and background color."""
    highlight_words = []
    highlight_style = []
    text_color = None
    bg_color = None

    for setting in settings:
        if setting.label == "highlightWords":
            highlight_words = setting.default.split(",")
        elif setting.label == "highlightStyle":
            highlight_style = setting.default.split(",")
        elif setting.label == "textColor":
            text_color = setting.default
        elif setting.label == "backgroundColor":
            bg_color = setting.default

    return highlight_words, highlight_style, text_color, bg_color

def apply_highlighting(message: str, keywords: List[str], styles: List[str], text_color: str, bg_color: str) -> str:
    """Applies multiple styles (bold, italic, uppercase, text color, background color) to keywords in the message."""
    
    def style_word(match):
        word = match.group(0)
        for style in styles:
            if style in COLOR_STYLES:
                word = COLOR_STYLES[style](word)
        if text_color in COLOR_STYLES:
            word = COLOR_STYLES[text_color](word)
        if bg_color in COLOR_STYLES:
            word = COLOR_STYLES[bg_color](word)
        return word

    if not keywords:
        return message  # Return original message if no keywords are provided

    # Sort keywords to prioritize longer words first
    keywords = sorted(set(keywords), key=len, reverse=True)
    
    # Use a regex pattern that ensures whole-word matching
    pattern = r"\b(" + "|".join(map(re.escape, keywords)) + r")\b"
    modified_message = re.sub(pattern, style_word, message, flags=re.IGNORECASE)

    return modified_message
