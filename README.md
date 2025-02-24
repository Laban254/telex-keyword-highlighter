### **Keyword Highlighter 🚀**

A **[Telex](https://telex.im/) integration** that processes messages and highlights specific keywords based on user-defined settings.



## **📌 Features**

-   🔍 **Keyword Highlighting** – Automatically highlights specified words in a message.
    
-   🎨 **Custom Styles** – Supports **bold, italic, underline, strikethrough, uppercase, custom colors, and background highlights**.
    
-   ♻️ **Dynamic Processing** – Users can define keywords and choose highlight styles.
    
-   🔧 **Modifier Integration** – Seamlessly works within Telex channels.

## 🔗 Integration Preview

Here’s a preview of the Keyword Highlighter integration:

![setings](https://github.com/user-attachments/assets/85ba71a5-64d5-49e9-b78f-c7e8cd8f0183)
![settings-](https://github.com/user-attachments/assets/6da83758-5578-46a4-a5ef-310d571250b3)
![chat](https://github.com/user-attachments/assets/8a8145d8-0c89-44ea-8ce3-1f28ef83b4b6)


## **⚙️ Setup & Installation**

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/yourusername/keyword-highlighter.git
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
uvicorn src.main:app --reload` 

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
    "date": {
      "created_at": "2025-02-13",
      "updated_at": "2025-02-21"
    },
    "descriptions":
    ...
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
  "message": "Check this alert now!",
  "channel_id": "123",
  "settings": [
    {"label": "highlightWords", "type": "multi-select", "required": true, "default": "important,urgent"},
    {"label": "highlightStyle", "type": "dropdown", "required": true, "default": "red-color"}
  ]
}
```
**📤 Response Example:**

```json
{
  "message": "Check this <span style='color: red;'>alert</span> now!"
}
```
----------

## **🧪 Running Tests**

Run the test suite with:

```sh
pytest tests/` 

```
----------
For more details, refer to the[Telex Integration Documentation](https://docs.telex.im/docs/Integrations/intro)

## **📜 License**

This project is **open-source** under the **MIT License**.

----------

