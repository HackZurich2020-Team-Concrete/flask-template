from flask import current_app, jsonify

from . import api_bp

@api_bp.route('/', methods=['GET'])
def home():
    data = 	{
        "items": [],
        "total": 0
    }
    data['items'].append({ 'name': 'Gerd' })
    data['total'] = data['total'] + 1

    return jsonify(data)
