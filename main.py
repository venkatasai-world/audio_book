from flask import Flask, render_template, request
import PyPDF2
import pyttsx3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    audio_ready = False

    if request.method == 'POST':
        file = request.files['pdf']

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        # Convert text to speech
        engine = pyttsx3.init()
        audio_path = "static/output.mp3"
        engine.save_to_file(text, audio_path)
        engine.runAndWait()

        audio_ready = True

    return render_template('index.html', text=text, audio_ready=audio_ready)

if __name__ == "__main__":
    app.run(debug=True)
