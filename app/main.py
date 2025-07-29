from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/", methods=["GET", "POST"])
def summarize():
    summary = ""
    if request.method == "POST":
        user_input = request.form["input_text"]
        if user_input:
            try:
                result = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
                summary = result[0]['summary_text']
            except Exception as e:
                summary = f"Error: {e}"

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
