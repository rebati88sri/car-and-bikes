print("hello world")
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
  return render_template('carandbike.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)