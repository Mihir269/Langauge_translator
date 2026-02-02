# 🌍 Language Translator using Mistral AI

A simple and interactive **language translation web application** built with **Streamlit** and **Mistral AI**.  
This app allows users to input text and translate it into multiple languages using the **Mistral Large** language model.

---

## 🚀 Features

- Translate text into **20+ languages**
- Powered by **Mistral Large (`mistral-large-latest`)**
- Clean and minimal **Streamlit UI**
- Secure API key handling using **environment variables**
- Fast and accurate translations

---

## 🧠 How It Works

1. User enters text to translate
2. User selects the target language
3. Prompt is constructed using `ChatPromptTemplate`
4. Translation is generated using **Mistral AI**
5. Output is displayed instantly

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM:** Mistral Large  
- **Framework:** LangChain  
- **Prompting:** ChatPromptTemplate  
- **Output Parsing:** StrOutputParser  
- **Environment Management:** python-dotenv  

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mistral-language-translator.git
cd mistral-language-translator

