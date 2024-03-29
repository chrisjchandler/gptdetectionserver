import openai
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # Get the text from the request
    text = flask.request.form["text"]

    # Use the OpenAI API to determine if the text was generated by the GPT model
    model_engine = "gpt-3.5-turbo-instruct"  # Updated model engine
    prompt = (f"Was this text generated by a GPT model?\n{text}")

    completions = openai.Completion.create(
        model=model_engine,  # Updated parameter name from 'engine' to 'model'
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()

    return message

if __name__ == "__main__":
    app.run()
