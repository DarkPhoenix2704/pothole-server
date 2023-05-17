import io
from flask import Flask, request, jsonify
from predict import predict
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST'])
@cross_origin()
def main():
    if request.method == 'POST':
        f = request.files['file']
        return jsonify(
            prediction=predict(io.BytesIO(f.read()))
        )


if __name__ == '__main__':
    app.run(debug=False, port=5000)
