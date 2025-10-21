from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/api/log', methods=['GET'])
def log_event():
    event = request.args.get('event', 'unknown')
    nickname = request.args.get('nickname', 'anonymous')
    email = request.args.get('email', '')
    age = request.args.get('age', '')

    # Форматируем время
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Особое сообщение для новых пользователей
    if event == "register":
        log_message = f"🆕 НОВЫЙ ПОЛЬЗОВАТЕЛЬ: {nickname} | email: {email} | [{timestamp}]"
    elif event == "update_profile":
        log_message = f"✏️ ПРОФИЛЬ ОБНОВЛЁН: {nickname} | email: {email} | возраст: {age} | [{timestamp}]"
    else:
        log_message = f"📊 Событие: {event} | пользователь: {nickname} | [{timestamp}]"

    # Выводим в консоль (это увидишь в Render Logs)
    print(log_message)

    return jsonify({
        "status": "success",
        "message": "Event logged",
        "event": event,
        "nickname": nickname
    })

if __name__ == '__main__':
    app.run(debug=True)
