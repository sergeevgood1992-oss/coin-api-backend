from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/log', methods=['GET'])
def log_event():
    event = request.args.get('event', 'unknown')
    nickname = request.args.get('nickname', 'anonymous')
    email = request.args.get('email', '')
    age = request.args.get('age', '')

    print(f"LOG: {event} | {nickname} | {email} | {age}")

    return jsonify({
        "status": "success",
        "message": f"Event '{event}' logged for {nickname}",
        "received": {
            "event": event,
            "nickname": nickname,
            "email": email,
            "age": age
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
