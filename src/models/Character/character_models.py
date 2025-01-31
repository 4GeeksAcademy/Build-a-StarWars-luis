from .. import db

class Character(db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(50), nullable=True)
    birth_year = db.Column(db.String(50), nullable=True)
    height = db.Column(db.String(10), nullable=True)
    skin_color = db.Column(db.String(50), nullable=True)
    hair_color = db.Column(db.String(50), nullable=True)

    # Relación inversa con la tabla Favorite
    favorites = db.relationship('Favorite', back_populates='character', lazy=True)

    def __repr__(self):
        return f'<Character {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "height": self.height,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color
        }

