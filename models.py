from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(500), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(500), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        """Show info about pet."""

        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.age} {p.available}>"

    def get_photo_url(self):
        """Return photo_url."""

        return self.photo_url

    @classmethod
    def all_pets(cls):
        """Return all pets."""

        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        """Return pet by id."""

        return cls.query.get_or_404(id)

    @classmethod
    def get_by_species(cls, species):
        """Return pets by species."""

        return cls.query.filter_by(species=species).all()

    @classmethod
    def get_by_availability(cls, available):
        """Return pets by availability."""

        return cls.query.filter_by(available=available).all()

    @classmethod
    def get_by_name(cls, name):
        """Return pets by name."""

        return cls.query.filter_by(name=name).all()

    @classmethod
    def find_or_create_pet(cls, name, species, photo_url, age, notes, available):
        """Find or create pet."""

        pet = cls.query.filter_by(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available,
        ).first()

        if pet:
            return pet
        else:
            new_pet = cls(
                name=name,
                species=species,
                photo_url=photo_url,
                age=age,
                notes=notes,
                available=available,
            )
            db.session.add(new_pet)
            db.session.commit()
            return new_pet

    @classmethod
    def edit_pet(cls, id, name, species, photo_url, age, notes, available):
        """Edit pet."""

        pet = cls.query.get_or_404(id)
        pet.name = name
        pet.species = species
        pet.photo_url = photo_url
        pet.age = age
        pet.notes = notes
        pet.available = available
        db.session.commit()
        return pet

    @classmethod
    def delete_pet(cls, id):
        """Delete pet."""

        pet = cls.query.get_or_404(id)
        db.session.delete(pet)
        db.session.commit()
        return pet

    @classmethod
    def change_availability(cls, id):
        """Change pet availability."""

        pet = cls.query.get_or_404(id)
        pet.available = not pet.available
        db.session.commit()
        return pet
