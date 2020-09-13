from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Sistema de coleta de dados epidemiológicos</h1><br><p>Tiago Soares - 1460481621079</p><br><p>Professor Fabrício Galende</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
