import pytest
from fastapi.testclient import TestClient
from src.main import app, process_highlight, extract_settings
from src.config import INTEGRATION_JSON
from src.main import HighlightRequest, Setting

client = TestClient(app)

# Test for the integration.json endpoint
def test_get_integration_json():
    response = client.get("/integration.json")
    assert response.status_code == 200
    assert response.json() == INTEGRATION_JSON  # Ensure it matches expected config

# Test for keyword highlighting functionality
@pytest.mark.parametrize(
    "message, settings, expected",
    [
        ("This is an important message", 
         [Setting(label="highlightWords", type="multi-select", required=True, default="important,urgent", description=""),
          Setting(label="highlightStyle", type="string", required=True, default="bold", description="")],
         "This is an **important** message"),  # Expected output with bold
        
        ("Urgent meeting at 5 PM!", 
         [Setting(label="highlightWords", type="multi-select", required=True, default="urgent,meeting", description=""),
          Setting(label="highlightStyle", type="string", required=True, default="italic", description="")],
         "*Urgent* *meeting* at 5 PM!"),  # Expected output with italic
        
        ("Check the report now", 
         [Setting(label="highlightWords", type="multi-select", required=True, default="report", description=""),
          Setting(label="highlightStyle", type="string", required=True, default="uppercase", description="")],
         "Check the REPORT now")  # Expected output with uppercase
    ]
)
def test_highlight_keywords(message, settings, expected):
    request = HighlightRequest(channel_id="123", settings=settings, message=message)
    highlighted_message = process_highlight(request)
    assert highlighted_message == expected

# Test API POST request for highlighting
def test_highlight_text_api():
    payload = {
        "channel_id": "123",
        "settings": [
            {"label": "highlightWords", "type": "multi-select", "required": True, "default": "alert,check", "description": ""},
            {"label": "highlightStyle", "type": "string", "required": True, "default": "bold", "description": ""}
        ],
        "message": "Check this alert now!"
    }
    
    response = client.post("/highlight-message", json=payload)
    
    assert response.status_code == 200
    assert response.json()["event_name"] == "message_highlighted"
    assert response.json()["status"] == "success"
    assert response.json()["message"] == "Check this **alert** now!"  # Expected transformation

