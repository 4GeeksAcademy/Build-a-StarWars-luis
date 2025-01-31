from .. import db

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(80), nullable=True)
    diameter = db.Column(db.String(50), nullable=True)
    terrain = db.Column(db.String(100), nullable=True)
    population = db.Column(db.String(50), nullable=True)

    # Relación inversa con la tabla Favorite
    favorites = db.relationship('Favorite', back_populates='planet', lazy=True)

    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "terrain": self.terrain,
            "population": self.population
        }
