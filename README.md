# 🚀 CodeVision Pro

A professional **Streamlit** application that transforms images into production-ready code using **AI Vision technology**.

---

## 🌟 Features

- **Smart Code Generation** — Automatically detects the best framework and generates appropriate code.  
- **Multi-Platform Support** — Web (HTML/CSS/JS), Mobile (React Native/Flutter), and Auto-detection.  
- **Professional UI** — Yellow-black-gold themed interface with smooth animations.  
- **History Management** — Keep track of your recent analyses with restore functionality.  
- **Real-time Preview** — Instant code generation and preview.  
- **Multiple Input Methods** — Upload files or use image URLs.  
- **Download Support** — Export generated code as files.  

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Setup
Create a `.env` file in your project root and add your **GROQ API key**:

```ini
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Application
```bash
streamlit run app.py
```

### 4. Access the App
Open your browser and go to:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧠 Usage Guide

### 1. Select Analysis Type
- **Smart Detection** — Auto-detects the best framework  
- **Web Application** — Generates HTML/CSS/JavaScript code  
- **Mobile Application** — Generates React Native or Flutter code  

### 2. Input Image
- Upload an image file (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp`)  
- Or provide an **image URL**

### 3. Generate Code
- Click **"Generate Code"** to analyze the image  
- View generated code instantly in the output section  
- Optionally, **download** the code as a file  

### 4. History
- View your recent analyses in the sidebar  
- **Restore** previous analyses  
- **Clear history** anytime  

---

## 🖼️ Supported Image Types

- **Formats:** PNG, JPG, JPEG, GIF, BMP, WebP  
- **Sources:** Local uploads or web URLs  
- **Optimized for:** UI/UX screenshots and mockups  

---

## 🤖 AI Models

**Llama 4 Scout** — `meta-llama/llama-4-scout-17b-16e-instruct`

- Advanced multimodal model with strong vision capabilities  
- Supports multilingual interaction and tool use  
- 128K context window  
- Maximum: **33 megapixels per image**, up to **5 images per request**

---

## 🎨 Theme & Design

Professional **yellow–black–gold** color scheme featuring:
- Animated title and interface elements  
- Smooth hover effects  
- Consistent button styling  
- **Orbitron** professional typography  
- Fully **responsive** design  

---

## 🧩 Technical Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit with custom CSS |
| **AI Vision** | Groq API (Llama Vision Models) |
| **Image Processing** | Pillow (PIL) |
| **HTTP Requests** | requests |
| **Environment Management** | python-dotenv |

---

## 📜 License

This project is open source and available under the **MIT License**.

---

> © 2025 **CodeVision Pro** — Powered by **Groq AI + Streamlit**
