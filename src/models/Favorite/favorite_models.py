from .. import db

class Favorite(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)

    # Relación inversa con User, Character y Planet
    user = db.relationship('User', back_populates='favorites')
    character = db.relationship('Character', back_populates='favorites')
    planet = db.relationship('Planet', back_populates='favorites')

    def __repr__(self):
        return f'<Favorite User={self.user_id} Character={self.character_id} Planet={self.planet_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }