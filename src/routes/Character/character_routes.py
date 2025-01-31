from flask import Blueprint, jsonify, request
from models import Character, User, Favorite
from models import db

people_bp = Blueprint('people', __name__)

# [GET] /people - Listar todos los personajes
@people_bp.route('/people', methods=['GET'])
def get_all_people():
    characters = Character.query.all()
    return jsonify([character.serialize() for character in characters]), 200

# [GET] /people/<int:people_id> - Obtener un personaje por su ID
@people_bp.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    character = Character.query.get(people_id)
    if not character:
        return jsonify({"error": "Personaje no encontrado"}), 404
    return jsonify(character.serialize()), 200


@people_bp.route('/create', methods=['POST'])
def create_character():
    body = request.get_json()

    if not body or not body.get('name') or not body.get('gender') or not body.get('birth_year'):
        return jsonify({"error": "Faltan datos requeridos (name, gender y birth_year)"}), 400

    new_character = Character(
        name=body['name'],
        gender=body['gender'],
        birth_year=body['birth_year'],
        height=body.get('height'),
        skin_color=body.get('skin_color'),
        hair_color=body.get('hair_color')
    )

    db.session.add(new_character)
    db.session.commit()

    return jsonify({"message": f"Personaje {new_character.name} creado exitosamente"}), 201



