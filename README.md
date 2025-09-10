# 🤖 Flask & n8n Chatbot

Այս նախագիծը ցույց է տալիս **Flask**-ի և **n8n**-ի ինտեգրումը՝ ստեղծելով պարզ, բայց արդյունավետ չատ-բոտ։

---

## 📌 Ինչ ենք կառուցել

- 🌐 **Flask Web Chat Application**՝ պարզ չատ ինտերֆեյս  
- 🔄 **n8n Workflow Integration**՝ ավտոմատ հաղորդագրությունների մշակում  
- ⚡ **Real-time հաղորդակցություն** Flask-ի և n8n-ի միջև  

---

## 💻 Flask Web Chat Application

📑 **Chat Interface**  
Պարզ չատի էջ (`chat.html`)՝ ստեղծված **HTML/JavaScript**-ով։  

📡 **API Endpoints**

- `/product/chat` → Չատի հիմնական էջ  
- `/send_message` → հաղորդագրություն ուղարկելու API 
- `/get_messages` → հաղորդագրությունները ստանալու API 

---

## 🔗 n8n Workflow Integration

- **Webhook Node** → Ստանում է հաղորդագրությունը Flask-ից  
- **Respond to Webhook Node** → Վերադարձնում է ճիշտ JSON պատասխանը Flask-ին  

---

## ⚙️ Ինչպես է աշխատում

Տվյալների հոսքը հետևյալն է․  

## `Օգտատեր → Flask Չատ → n8n Webhook → n8n Response → Flask → Օգտատեր`



1. Օգտատերը գրում է հաղորդագրություն web chat-ում
2. Flask-ը ուղարկում է POST request n8n webhook-ին
3. n8n-ը մշակում է հաղորդագրությունը
4. n8n-ը JSON պատասխան է վերադարձնում Flask-ին
5. Flask-ը ցույց է տալիս պատասխանը չատում

---

## 🛠 Տեխնիկական Բաղադրիչներ

- 🎨 **Frontend** → HTML / JavaScript  
- 🐍 **Backend** → Flask (Python server)  
- 🤖 **Automation** → n8n workflow  
- 🔗 **Communication** → HTTP / JSON API  

---

## ✅ Անվտանգություն և Հուսալիություն

- 📥 Գործող չատ-բոտ, որը կարող է ընդունել հաղորդագրություններ  
- 🔄 n8n ինտեգրում՝ ավտոմատ մշակման համար  
- ⚡ Real-time հաղորդակցություն Flask-ի և n8n-ի միջև  
- 🐞 Սխալների մշակում և debug logging  

---

## ✅ Այսպիսով ունենք:
- ✅ Գործող չատ-բոտ որը կարող է ընդունել հաղորդագրություններ
- ✅ n8n integration ավտոմատացված մշակման համար
- ✅ Real-time հաղորդակցություն Flask և n8n-ի միջև
- ✅ Error handling և debug logging

## 🚀 Հաջորդ Քայլեր

Այժմ կարող եք հեշտությամբ ավելացնել․  

- 🧠 AI ինտեգրում (ChatGPT, LLM-եր և այլն)  
- 💾 Տվյալների բազայի գործողություններ  
- 🌍 Արտաքին API ինտեգրումներ  
- 🛠 Custom Logic  

---


## ENGLISH


---
## 🤖 Flask & n8n Chatbot
This project demonstrates the integration of Flask and n8n to create a simple yet effective chat-bot.

## 📌 What We Built

- 🌐 Flask Web Chat Application: simple chat interface
- 🔄 n8n Workflow Integration: automatic message processing
- ⚡ Real-time communication between Flask and n8n

---

## 💻 Flask Web Chat Application

📑 **Chat Interface**
- Simple chat page (chat.html) created with HTML/JavaScript.
- 
📡 **API Endpoints**

- `/product/chat` → Main chat page
- `/send_message` → API for sending messages
- `/get_messages` → API for retrieving messages


## 🔗 n8n Workflow Integration

- **Webhook Node** → Receives the message from Flask
- **Respond to Webhook Node** → Returns the correct JSON response to Flask

---

## ⚙️ How It Works

The data flow is as follows:

## `User → Flask Chat → n8n Webhook → n8n Response → Flask → User`

- The user writes a message in the web chat
- Flask sends a POST request to the n8n webhook
- n8n processes the message
- n8n returns a JSON response to Flask
- Flask displays the response in the chat

---

## 🛠 Technical Components

- 🎨 Frontend → HTML / JavaScript
- 🐍 Backend → Flask (Python server)
- 🤖 Automation → n8n workflow
- 🔗 Communication → HTTP / JSON API

---

## ✅ Security and Reliability

- 📥 Functional chat-bot that can accept messages
- 🔄 n8n integration for automatic processing
- ⚡ Real-time communication between Flask and n8n
- 🐞 Error handling and debug logging

---

## ✅ Thus We Have:

- ✅ Functional chat-bot that can accept messages
- ✅ n8n integration for automated processing
- ✅ Real-time communication between Flask and n8n
- ✅ Error handling and debug logging

---
## 🚀 Next Steps
**Now you can easily add:**

- 🧠 AI integration (ChatGPT, LLMs, etc.)
- 💾 Database operations
- 🌍 External API integrations
- 🛠 Custom Logic

---
