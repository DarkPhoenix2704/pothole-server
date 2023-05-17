import io
from flask import Flask, request, jsonify
from predict import predict
app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        f = request.files['file']
        return jsonify(
            prediction=predict(io.BytesIO(f.read()))
        )


if __name__ == '__main__':
    app.run(debug=False, port=5000)
