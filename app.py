from flask import Flask, request, jsonify
import qrcode
import random, string
from otp_generator import generate_otp
from email_service import send_otp_email
from db import save_user, get_user

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    email = data['email']
    otp = generate_otp()
    save_user(username, email, otp)
    send_otp_email(email, otp)
    return jsonify({"message": "User registered and OTP sent"}), 200

@app.route('/qr', methods=['GET'])
def qr_code():
    otp = generate_otp()
    qr = qrcode.make(otp)
    qr.save("otp.png")
    return jsonify({"qr": "otp.png"}), 200

@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    user = get_user(data['username'])
    if user and user['otp'] == data['otp']:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "failed"}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
