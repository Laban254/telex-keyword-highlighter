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
            "Supports multiple highlight styles (bold, italic, uppercase).",
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
                "default": "uppercase",
                "description": "Set the style for highlighted words (bold, italic, uppercase)."
            }
        ],
        "target_url": "https://keyword-highlighter-debug.onrender.com/highlight-message",
    }
}
