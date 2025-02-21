INTEGRATION_JSON = {
    "data": {
        "author": "Laban Kibet",
        "date": {
            "created_at": "2025-02-13",
            "updated_at": "2025-02-13"
        },
        "descriptions": {
            "app_description": "A keyword highlighter bot that processes messages and highlights specific keywords.",
            "app_logo": "https://media.tifi.tv/telexbucket/public/logos/formatter.png",
            "app_name": "Keyword Highlighter",
            "app_url": "https://keyword-highlighter-debug.onrender.com/",
            "background_color": "#ffffff"
        },
        "integration_category": "Communication & Collaboration",
        "integration_type": "modifier",
        "is_active": True,
        "key_features": [
            "Highlight specific words in messages.",
            "Supports multiple highlight styles (bold, italic, uppercase, colors, backgrounds).",
            "Processes messages dynamically based on user settings."
        ],
        "permissions": {
            "events": [
                "Receive messages from Telex channels.",
                "Highlight specified keywords in messages.",
                "Send highlighted messages back to the channel."
            ]
        },
        "settings": [
            {
                "label": "highlightWords",
                "type": "multi-select",
                "required": True,
                "default": "important,urgent",
                "description": "Set the words that need to be highlighted."
            },
            {
                "label": "highlightStyle",
                "type": "multi-select",
                "required": True,
                "default": "bold",
                "description": "Set the style for highlighted words (bold, italic, uppercase)."
            },
            {
                "label": "textColor",
                "type": "multi-select",
                "required": False,
                "default": "red",
                "description": "Set the text color for highlighted words (red, green, blue, yellow)."
            },
            {
                "label": "backgroundColor",
                "type": "multi-select",
                "required": False,
                "default": "bg_red",
                "description": "Set the background color for highlighted words (bg_red, bg_green, bg_yellow)."
            }
        ],
        "target_url": "https://keyword-highlighter-debug.onrender.com/highlight-message",
    }
}
