from flask import Blueprint, jsonify, request
from models import User, Character, Planet, Favorite
from models import db

users_bp = Blueprint('users', __name__)

# [GET] /users - Listar todos los usuarios
@users_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200


@users_bp.route('/create', methods=['POST'])
def create_user():
    body = request.get_json()

    if not body or not body.get('email') or not body.get('password'):
        return jsonify({"error": "Faltan datos requeridos (email y password)"}), 400

    # Verificar si el usuario ya existe
    if User.query.filter_by(email=body['email']).first():
        return jsonify({"error": "El usuario ya está registrado"}), 400

    new_user = User(email=body['email'], password=body['password'], is_active=True)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"Usuario {new_user.email} creado exitosamente"}), 201



# [GET] /users/<int:user_id> - Obtener detalles de un usuario por ID
@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.serialize()), 200

# [DELETE] /users/<int:user_id> - Eliminar un usuario
@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"Usuario {user.email} eliminado exitosamente"}), 200