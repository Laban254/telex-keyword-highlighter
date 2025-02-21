INTEGRATION_JSON = {
    "data": {
        "author": "Laban Kibet",
        "date": {
            "created_at": "2025-02-13",
            "updated_at": "2025-02-21"
        },
        "descriptions": {
            "app_name": "Keyword Highlighter",
            "app_description": (
                "✨ Keyword Highlighter is an intelligent tool that automatically detects and highlights "
                "specified keywords in messages. It enhances readability and ensures important information stands out."
            ),
            "app_logo": "https://img.icons8.com/?size=100&id=wWQJ5na5fQNZ&format=png&color=000000",  # Ensure this URL is correct
            "app_url": "https://keyword-highlighter-debug.onrender.com/",
            "background_color": "#ffffff"
        },
        "integration_category": "Communication & Collaboration",
        "integration_type": "Modifier",
        "is_active": True,
        "key_features": [
            "🔍 Instantly identifies and highlights specified words.",
            "🎨 Supports bold, italic, underline, strikethrough, uppercase, custom colors, and background highlights.",
            "⚙️ Users can define keywords and choose highlight styles.",
            "⚡ Works dynamically as messages are received.",
            "📌 Ensures important words stand out for better message clarity."
        ],
        "permissions": {
            "events": [
                "📥 Captures incoming messages from Telex channels.",
                "📝 Identifies keywords and applies selected highlight styles.",
                "📤 Returns the formatted message with highlighted words.",
                "🔧 Supports user-defined keyword lists and highlight preferences."
            ]
        },
        "settings": [
            {
                "label": "highlightWords",
                "type": "multi-select",
                "required": True,
                "default": "important,urgent",
                "description": "✏️ Specify keywords to be highlighted in messages."
            },
            {
                "label": "highlightStyle",
                "type": "dropdown",
                "required": True,
                "default": "red-color",
                "options": [
                    "bold", "italic", "uppercase", "strikethrough", "underline",
                    "red-color", "yellow-background", "emoji"
                ],
                "description": "🎨 Choose a highlight style for selected keywords."
            }
        ],
        "target_url": "https://keyword-highlighter-debug.onrender.com/highlight-message",
    }
}
