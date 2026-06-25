from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    color = os.getenv("APP_COLOR", "white")

    return f"""
    <body style="background-color:{color};">

    <h1 style="
        text-align:center;
        margin-top:300px;
        font-size:50px;">

    APP_COLOR = {color}

    </h1>

    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
    