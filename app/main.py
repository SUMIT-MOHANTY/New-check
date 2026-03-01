import os
from flask import Blueprint, jsonify
from app import create_app

health_bp = Blueprint('health', __name__, url_prefix='/api')


@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "flask-backend"})


app = create_app()

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', '1') == '1'
    app.run(host='0.0.0.0', port=5000, debug=debug)
