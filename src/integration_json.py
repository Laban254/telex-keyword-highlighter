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
            "app_logo": "https://img.icons8.com/?size=100&id=XGSm8Ac3FGzj&format=png&color=000000",  # Ensure this URL is correct
            "app_url": "https://keyword-highlighter-debug.onrender.com/",
            "background_color": "#ffffff"
        },
        "integration_category": "📢 Communication & Collaboration",
        "integration_type": "🖍️ Modifier",
        "is_active": True,
        "key_features": [
            "🔍 <strong>Automatic Keyword Detection</strong> - Instantly identifies and highlights specified words.",
            "🎨 <strong>Multiple Highlight Styles</strong> - Supports bold, italic, underline, strikethrough, uppercase, custom colors, and background highlights.",
            "⚙️ <strong>Customizable Preferences</strong> - Users can define keywords and choose highlight styles.",
            "⚡ <strong>Real-time Processing</strong> - Works dynamically as messages are received.",
            "🔗 <strong>Seamless Integration</strong> - Easily connects with Telex channels and other communication tools.",
            "📌 <strong>Enhanced Readability</strong> - Ensures important words stand out for better message clarity."
        ],
        "permissions": {
            "events": [
                "📥 <strong>Receive Messages</strong> - Captures incoming messages from Telex channels.",
                "📝 <strong>Process & Highlight</strong> - Identifies keywords and applies selected highlight styles.",
                "📤 <strong>Send Enhanced Messages</strong> - Returns the formatted message with highlighted words.",
                "🔧 <strong>User Configurable</strong> - Supports user-defined keyword lists and highlight preferences."
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
