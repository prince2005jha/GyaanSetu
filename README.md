
# 💬 EmpowerHer Chatbot

EmpowerHer is an AI-driven chatbot designed to bridge the gender gap by empowering women and girl children with accessible, real-time information on **health**, **legal rights**, and **financial literacy**. The chatbot supports voice and text interactions and is powered by **Dialogflow**, integrated via a **Flask or Django backend**.

---

## 🚀 Project Purpose

The purpose of EmpowerHer is to:
- Promote **gender equality** by providing easy access to essential services and information.
- Empower women and girls to make informed decisions.
- Create a safe, accessible, and supportive digital assistant for women in need.

---

## 🌟 Key Features

### 🔐 1. AI-based Legal Assistance for Women’s Rights
- **Intent:** `Legal Assistance`
- Responds to questions like:
  - “What are my rights as a woman in India?”
  - “How do I report domestic violence?”
  - “What are the laws on property inheritance?”
- **Entities Used:** Location, type of crime.
- **Data Source:** Can be enhanced using legal APIs or government law databases.

---

### 💰 2. Financial Education & Savings Plans
- **Intent:** `Financial Education` / `Savings Plans`
- Provides guidance on:
  - Budgeting and debt management
  - Government schemes (like MUDRA Yojana, Beti Bachao Beti Padhao)
  - Basic investment strategies
- **Entities Used:** Income level, financial goals.
- **APIs (Optional):** Financial data, scheme directories.

---

### ❤️ 3. Health Literacy & Wellness Information
- **Intent:** `Women’s Health`
- Covers:
  - Reproductive health
  - Nutrition, exercise tips
  - Awareness about breast cancer, menopause, etc.
- **Entities Used:** Age, symptoms.
- **API Integration (Optional):** WHO/CDC health info APIs.

---

### 🎤 4. Voice-Enabled Chatbot
- Can be connected to Google Assistant or Alexa for hands-free use.
- **Examples:**
  - “Hey EmpowerHer, what are my rights?”
  - “Tell me how to apply for government financial aid.”

---

## 🛠️ Tech Stack

| Tech         | Description                                     |
|--------------|-------------------------------------------------|
| Python       | Backend development                            |
| Dialogflow   | NLP & Intent Management                        |
| Flask/Django | Web framework for serving backend              |
| Google Cloud | Service account & API credentials             |
| HTML/CSS     | (Optional) Frontend interface for chatbot     |
| Django Templating | For rendering chatbot UI if using Django |

---

## ⚙️ Installation & Setup

### 🔧 Backend Setup (Flask or Django)

#### Install Dependencies
```bash
pip install flask google-cloud-dialogflow django
```

#### Configure Environment
1. Create a Dialogflow agent.
2. Download the **service account key JSON**.
3. Set environment variable:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key.json"
```

---

### 🧠 Dialogflow Agent Setup
- Create **intents** for:
  - Legal Help
  - Health Guidance
  - Financial Literacy
- Add **training phrases**, responses, and parameters (entities).

---

## 🔌 API Integration (Optional Enhancements)

| Domain      | API Example                                       |
|-------------|---------------------------------------------------|
| Health      | WHO or Healthline API                             |
| Finance     | Govt Open Data Portals, Economic Times APIs       |
| Legal       | LawRato API, National Legal Services Authority    |

---

## 🧪 Sample Django View Code

```python
from django.shortcuts import render
from django.http import JsonResponse
from google.oauth2 import service_account
from googleapiclient.discovery import build

credentials = service_account.Credentials.from_service_account_file('path/to/key.json')
dialogflow = build('dialogflow', 'v2', credentials=credentials)

def chatbot_view(request):
    user_input = request.POST.get('user_input')
    session = dialogflow.sessions().create(body={'session': 'empowerher'}).execute()
    response = dialogflow.sessions().detectIntent(
        body={'session': session['session'], 'queryInput': {'text': user_input}}
    ).execute()
    return JsonResponse({'response': response['queryResult']['fulfillmentText']})

def chatbot_template(request):
    return render(request, 'chatbot.html')
```

---

## 📈 Future Enhancements

- 📍 Location-based services (legal aid centers, women’s helplines)
- 🔊 Multi-language support (Hindi, Bengali, Tamil, etc.)
- 📱 Mobile app integration using **Flutter**
- 📂 Resource sharing (PDFs, videos, documents)

---

## 🤝 Contributors

- **DivyaJha** – Developer | Idea Initiator  
- Special thanks to the open-source community and women rights NGOs for the data sources.

---

## 🫶 Impact

EmpowerHer isn't just a chatbot—it's a mission. By making critical information accessible, it empowers women and young girls to break barriers, fight injustice, and build financially independent, healthy lives.
