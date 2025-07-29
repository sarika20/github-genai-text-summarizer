from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here (or via env variable)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def summarize():
    summary = ""
    if request.method == "POST":
        user_input = request.form["input_text"]
        if user_input:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful summarizer."},
                        {"role": "user", "content": f"Summarize this:\n{user_input}"}
                    ],
                    max_tokens=150,
                    temperature=0.5
                )
                summary = response.choices[0].message["content"].strip()
            except Exception as e:
                summary = f"Error: {e}"

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
