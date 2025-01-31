from flask import Blueprint, jsonify, request
from models import Planet, User, Favorite
from models import db

planets_bp = Blueprint('planets', __name__)

# [GET] /planets - Listar todos los planetas
@planets_bp.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

# [GET] /planets/<int:planet_id> - Obtener un planeta por su ID
@planets_bp.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planeta no encontrado"}), 404
    return jsonify(planet.serialize()), 200


# [POST] /planets - Crear un nuevo planeta
@planets_bp.route('/create', methods=['POST'])
def create_planet():
    body = request.get_json()

    if not body or not body.get('name') or not body.get('climate') or not body.get('terrain'):
        return jsonify({"error": "Faltan datos requeridos (name, climate y terrain)"}), 400

    new_planet = Planet(
        name=body['name'],
        climate=body['climate'],
        diameter=body.get('diameter'),
        terrain=body['terrain'],
        population=body.get('population')
    )

    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"message": f"Planeta {new_planet.name} creado exitosamente"}), 201

