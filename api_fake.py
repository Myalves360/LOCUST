from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Homepage OK"

@app.route("/api/fake")
def fake_api():
    return {"message": "API fake funcionando"}

if __name__ == "__main__":
    app.run(port=5000)
