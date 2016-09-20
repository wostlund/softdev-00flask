from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return("salutations")

@app.route("/var")
def title():
    return hello() + "<br><b> Welcome to my page!</b>"

if __name__ == "__main__":
    app.run()
