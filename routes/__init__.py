from flask import Blueprint, jsonify
from models import Career

bp = Blueprint('main', __name__)

@bp.route('/api/careers', methods=['GET'])
def get_careers():
    careers = Career.query.all()
    return jsonify([{'id': career.id, 'title': career.title, 'description': career.description} for career in careers])
