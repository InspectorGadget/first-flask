from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def dummy_api():
    name = request.args.get("name")

    if name is None:
        return jsonify(error="Invalid GET Parameters"), 400

    return jsonify(data=name), 200


@app.route("/hello")
def hi():
    return jsonify(data="Hi"), 200


if __name__ == "__main__":
    app.run(debug=True)
