from flask import Flask, jsonify, Response, request
import pandas as pd

#load_dotenv()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hi():
  df = pd.read_csv("x.csv")
  return Response(df.to_json(orient="records"), mimetype='application/json')


@app.route('/greeting', methods=['GET'])
def greeting():
  return "Holaa"


if __name__ == '__main__':
    app.run()