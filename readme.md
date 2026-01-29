# PDF to Speech Converter (Flask App)

This is a simple Flask web application that converts text from a PDF file into an audio file.

The user uploads a PDF, the app extracts the text from all pages, and then converts that text into an MP3 audio file using Text-to-Speech.

---

## What the App Does

- Upload a PDF file  
- Extract text from the PDF  
- Convert text into speech  
- Generate an MP3 audio file  
- Play or download the audio  

---

## Technologies Used

- Python  
- Flask  
- PyPDF2  
- pyttsx3  
- HTML  

---

## How to Run

Install required packages:
```bash
pip install flask PyPDF2 pyttsx3

python main.py

