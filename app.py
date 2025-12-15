from flask import Flask, render_template, request, redirect, url_for
import os
import json
import pdfplumber
import openai

# Initialize Flask app
app = Flask(__name__, template_folder="index.html")  # Ensure it points to your index.html folder

# Load skills JSON if needed
SKILLS_FILE = "skills.json"
if os.path.exists(SKILLS_FILE):
    with open(SKILLS_FILE, "r") as f:
        skills_data = json.load(f)
else:
    skills_data = []

# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle file upload
        uploaded_file = request.files.get("resume")
        if uploaded_file:
            file_path = os.path.join("uploaded_resume.pdf")
            uploaded_file.save(file_path)
            # Extract text from PDF
            text = extract_text_from_pdf(file_path)
            # Optionally: analyze with OpenAI
            analysis = analyze_resume(text)
            return render_template("index.html", analysis=analysis)
    return render_template("index.html")

# PDF text extraction
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print("PDF extraction error:", e)
    return text

# Example: OpenAI analysis
def analyze_resume(text):
    if not text:
        return "No text extracted."
    try:
        # Ensure OPENAI_API_KEY is set in Render environment
        openai.api_key = os.environ.get("OPENAI_API_KEY", "")
        if not openai.api_key:
            return "OpenAI API key not set."

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Analyze this resume and summarize key skills:\n{text}",
            max_tokens=300
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("OpenAI analysis error:", e)
        return "Analysis failed."

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)






