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
                "Keyword Highlighter is an intelligent message processing bot that automatically detects and highlights "
                "specified keywords in messages. Designed for seamless integration, it enhances readability and ensures "
                "important information stands out."
            ),
            "app_logo": "https://media.tifi.tv/telexbucket/public/logos/highlighter_v2.png",  # Updated logo
            "app_url": "https://keyword-highlighter-debug.onrender.com/",
            "background_color": "#ffffff"
        },
        "integration_category": "Communication & Collaboration",
        "integration_type": "modifier",
        "is_active": True,
        "key_features": [
            "🔍 **Automatic Keyword Detection** – Instantly identifies and highlights specified words in messages.",
            "🎨 **Multiple Highlight Styles** – Supports bold, italic, underline, strikethrough, uppercase, custom colors, and background highlights.",
            "⚙️ **Customizable Preferences** – Users can define keywords and choose highlight styles.",
            "⚡ **Real-time Processing** – Works dynamically to highlight words as messages are received.",
            "🔗 **Seamless Integration** – Easily integrates with Telex channels and other communication platforms.",
            "📌 **Enhanced Readability** – Ensures important words and phrases stand out for better message clarity."
        ],
        "permissions": {
            "events": [
                "📥 **Receive Messages** – Captures incoming messages from Telex channels.",
                "📝 **Process & Highlight** – Identifies keywords and applies selected highlight styles.",
                "📤 **Send Enhanced Messages** – Returns the formatted message with highlighted words.",
                "🔧 **User Configurable** – Supports user-defined keyword lists and highlight preferences."
            ]
        },
        "settings": [
            {
                "label": "highlightWords",
                "type": "multi-select",
                "required": True,
                "default": "important,urgent",
                "description": "Specify keywords to be highlighted in messages."
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
                "description": "Choose a highlight style for selected keywords."
            }
        ],
        "target_url": "https://keyword-highlighter-debug.onrender.com/highlight-message",
    }
}
