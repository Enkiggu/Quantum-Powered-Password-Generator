from flask import Flask, jsonify, request
from password_generator import PasswordGenerator

app = Flask(__name__)

@app.route('/generate_password', methods=['GET'])
def generate_password():
    length = int(request.args.get('length', 8))
    password_generator = PasswordGenerator(length)
    password = password_generator.generate_random_password()
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)