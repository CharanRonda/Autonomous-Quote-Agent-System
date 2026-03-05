from flask import Flask,render_template,request
import agents

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    premium=int(request.form["premium"])
    accidents=int(request.form["accidents"])

    risk=agents.risk_profiler(accidents)

    conversion=agents.conversion_predictor()

    advice=agents.premium_advisor(premium)

    decision=agents.decision_router(risk,conversion)

    return render_template("index.html",
                           risk=risk,
                           conversion=conversion,
                           advice=advice,
                           decision=decision)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
