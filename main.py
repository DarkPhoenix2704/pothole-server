import io
from flask import Flask, request
from predict import predict
app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        f = request.files['file']
        return {
            "prediction":  predict(io.BytesIO(f.read()))
        }


if __name__ == '__main__':
    app.run(debug=False, port=5000)
