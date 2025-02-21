### **Keyword Highlighter API 🚀**

A FastAPI-based service that processes messages and highlights specific keywords based on user-defined settings.

----------

## **📌 Features**

-   🔍 **Keyword Highlighting** – Automatically highlights specified words in a message.
-   🎨 **Custom Styles** – Supports **bold, italic, and uppercase** highlighting.
-   🔄 **Dynamic Processing** – Users can set their own highlight words and styles.
-   📡 **REST API** – Exposes endpoints for easy integration.

----------
## 🔗 Integration Preview

Here’s a preview of the Keyword Highlighter integration:

## **⚙️ Setup & Installation**

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/telexintegrations/keyword-highlighter
cd keyword-highlighter` 
```
### **2️⃣ Create a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows` 
```
### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt` 
```
----------

## **🚀 Running the API**

### **Start the FastAPI Server**

```sh
`uvicorn src.main:app --reload` 

The API will be available at **`http://127.0.0.1:8000`**.
```
----------

## **📡 API Endpoints**

### **1️⃣ Get Integration Metadata**

#### **GET `/integration.json`**

Returns metadata about the integration.

**Example Response:**

```json

{
  "data": {
    "author": "Laban Kibet",
    "descriptions": {
      "app_name": "Keyword Highlighter",
      "app_description": "A bot that highlights specific keywords in messages."
    },
    "key_features": [
      "Highlight specific words",
      "Supports multiple highlight styles"
    ]
  }
}
```
----------

### **2️⃣ Highlight Message**

#### **POST `/highlight-message`**

Highlights keywords in a given message based on user settings.

**📩 Request Example:**

```json

{
  "channel_id": "123",
  "settings": [
    {"label": "highlightWords", "type": "multi-select", "required": true, "default": "alert,check", "description": ""},
    {"label": "highlightStyle", "type": "string", "required": true, "default": "bold", "description": ""}
  ],
  "message": "Check this alert now!"
} 
```
**📤 Response Example:**

```json
{
  "event_name": "message_highlighted",
  "message": "Check this **alert** now!",
  "status": "success",
  "username": "keyword-highlighter-bot"
} 
```
----------

## **🧪 Running Tests**

Run the test suite with:

```sh
pytest tests/` 

```
----------

## **📜 License**

This project is **open-source** under the **MIT License**.

----------

## **👨‍💻 Author**

Developed by **Laban Kibet** 🏆