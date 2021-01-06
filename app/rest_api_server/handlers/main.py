from flask import request, jsonify
from rest_api_server import server
from telegram_bot import bot as tg_bot
import asyncio


@server.route('/api/v1.0/send_notification', methods=['POST'])
def send_notification() -> tuple:
    if not request.json or (not ('phone_number' in request.json) and not ('text' in request.json)):
        return jsonify({'error': 'parameters "phone_number", "text" are not defined'}), 400
    elif not ('phone_number' in request.json):
        return jsonify({'error': 'parameter "phone_number" is not defined'}), 400
    elif not ('text' in request.json):
        return jsonify({'error': 'parameter "text" is not defined'}), 400
    success: dict = dict()
    errors: dict = dict()
    tasks: list = [
        server.async_loop.create_task(tg_bot.send_message_to_phone_number(request.json['phone_number'],
                                                                          request.json['text']), name='telegram')
    ]
    server.async_loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        task: asyncio.Task
        result: dict = task.result()
        if result.get('success'):
            success[task.get_name()] = result["success"]
        else:
            errors[task.get_name()] = result["error"]
    result: dict = dict()
    if success:
        result['success'] = success
    if errors:
        result['errors'] = errors
    return jsonify(result), 200
