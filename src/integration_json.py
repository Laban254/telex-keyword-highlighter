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
            "Supports multiple highlight styles (bold, italic, uppercase, emojis).",
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
                "description": "Select words to highlight.",
                "required": True,
                "default": "important,urgent"
            },
            {
                "label": "highlightImportantBold",
                "type": "checkbox",
                "description": "Apply bold to 'important'",
                "default": True
            },
            {
                "label": "highlightImportantItalic",
                "type": "checkbox",
                "description": "Apply italic to 'important'",
                "default": False
            },
            {
                "label": "highlightImportantUppercase",
                "type": "checkbox",
                "description": "Make 'important' uppercase",
                "default": False
            },
            {
                "label": "highlightImportantEmoji",
                "type": "checkbox",
                "description": "Use emoji for 'important'",
                "default": True
            },
            {
                "label": "highlightUrgentBold",
                "type": "checkbox",
                "description": "Apply bold to 'urgent'",
                "default": False
            },
            {
                "label": "highlightUrgentItalic",
                "type": "checkbox",
                "description": "Apply italic to 'urgent'",
                "default": True
            },
            {
                "label": "highlightUrgentUppercase",
                "type": "checkbox",
                "description": "Make 'urgent' uppercase",
                "default": True
            },
            {
                "label": "highlightUrgentEmoji",
                "type": "checkbox",
                "description": "Use emoji for 'urgent'",
                "default": False
            }
        ],
        "target_url": "https://keyword-highlighter-debug.onrender.com/highlight-message"
    }
}
