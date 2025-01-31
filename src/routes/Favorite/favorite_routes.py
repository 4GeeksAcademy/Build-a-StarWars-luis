from flask import Blueprint, jsonify, request
from models import Favorite, User, Character, Planet
from models import db

favorites_bp = Blueprint('favorites', __name__)

# [GET] /users/favorites - Listar todos los favoritos del usuario actual
@favorites_bp.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    body = request.get_json()
    user_id = body.get('user_id')

    if not user_id:
        return jsonify({"error": "Se requiere el user_id"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    favorites = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify([favorite.serialize() for favorite in favorites]), 200

# [POST] /favorite/people/<int:people_id> - Añadir un personaje a favoritos
@favorites_bp.route('/people/<int:people_id>', methods=['POST'])
def add_people_favorite(people_id):
    body = request.get_json()
    user_id = body.get('user_id')

    if not user_id:
        return jsonify({"error": "Se requiere el user_id"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    character = Character.query.get(people_id)
    if not character:
        return jsonify({"error": "Personaje no encontrado"}), 404

    new_favorite = Favorite(user_id=user_id, character_id=people_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({"message": f"Personaje {character.name} añadido a favoritos"}), 201

# [POST] /favorite/planet/<int:planet_id> - Añadir un planeta a favoritos
@favorites_bp.route('/planet/<int:planet_id>', methods=['POST'])
def add_planet_favorite(planet_id):
    body = request.get_json()
    user_id = body.get('user_id')

    if not user_id:
        return jsonify({"error": "Se requiere el user_id"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planeta no encontrado"}), 404

    new_favorite = Favorite(user_id=user_id, planet_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({"message": f"Planeta {planet.name} añadido a favoritos"}), 201

# [DELETE] /favorite/people/<int:people_id> - Eliminar un personaje de favoritos
@favorites_bp.route('/people/<int:people_id>', methods=['DELETE'])
def delete_people_favorite(people_id):
    body = request.get_json()
    user_id = body.get('user_id')

    if not user_id:
        return jsonify({"error": "Se requiere el user_id"}), 400

    favorite = Favorite.query.filter_by(user_id=user_id, character_id=people_id).first()
    if not favorite:
        return jsonify({"error": "El personaje no está en favoritos"}), 404

    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Personaje eliminado de favoritos"}), 200

# [DELETE] /favorite/planet/<int:planet_id> - Eliminar un planeta de favoritos
@favorites_bp.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favorite(planet_id):
    body = request.get_json()
    user_id = body.get('user_id')

    if not user_id:
        return jsonify({"error": "Se requiere el user_id"}), 400

    favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if not favorite:
        return jsonify({"error": "El planeta no está en favoritos"}), 404

    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Planeta eliminado de favoritos"}), 200
