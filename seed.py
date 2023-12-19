from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
pet1 = Pet(name="woofly", species="Dog", photo_url="https://wallpaperaccess.com/full/2564865.jpg", age=10, notes="Electric type", available=True)
pet2 = Pet(name="Charmander", species="Dog", photo_url="https://www.travelandleisure.com/thmb/XIQ66ILqKplKWPJI48I8dQHTPiw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/corgi-dog-name-POPDOGS0819-1ebb8efb2c68499eab1c76411c9d1c15.jpg", age=10, notes="Fire type", available=True)
pet3 = Pet(name="Squirtle", species="Cat", photo_url="https://get.pxhere.com/photo/profile-model-cat-livestock-mammal-close-fauna-close-up-pets-whiskers-vertebrate-expensive-tabby-cat-fur-animals-european-shorthair-wild-cat-small-to-medium-sized-cats-cat-like-mammal-domestic-short-haired-cat-pixie-bob-rusty-spotted-cat-869640.jpg", age=10, notes="Water type", available=True)
pet4 = Pet(name="Bulbasaur", species="Dog", photo_url="https://media.istockphoto.com/id/1503385646/photo/portrait-funny-and-happy-shiba-inu-puppy-dog-peeking-out-from-behind-a-blue-banner-isolated.jpg?s=612x612&w=is&k=20&c=d3_Foq65pSBGelz6FDDrHf61HviqDmKDN-2CIUd4Bvk=", age=10, notes="Grass type", available=True)
pet5 = Pet(name="Eevee", species="Cat", photo_url="https://unionlakeveterinaryhospital.com/wp-content/uploads/2020/03/ULVH-cat-fav-human-shutterstock_774405733-980x654.jpg", age=10, notes="Normal type", available=True)
pet6 = Pet(name="Pidgey", species="Pig", photo_url="https://media.istockphoto.com/id/956025942/photo/newborn-piglet-on-spring-green-grass-on-a-farm.jpg?s=612x612&w=is&k=20&c=XI7-V7gj13rQG0_ly4DYn3pRie88RCCESGJTwKCFc-c=", age=10, notes="Flying type", available=False)
pet7 = Pet(name="Rattata", species="Cat", photo_url="https://media.istockphoto.com/id/1389862392/photo/womans-hand-stroking-a-ginger-cat-on-isolated-white-background.jpg?s=612x612&w=is&k=20&c=rUacpL74HL7r5i6Eg_nYBDNkBLrh3IUqS1mduOWTEdk=", age=10, notes="Normal type", available=True)
pet8 = Pet(name="Pikachu", species="Dog", photo_url="https://media.istockphoto.com/id/176527406/photo/curious-dog.jpg?s=612x612&w=is&k=20&c=A55bVa0DIpSVXia3nhafc7aPumsxQt8MM-cBAlX_ngw=", age=10, notes="Electric type", available=True)

# Add new objects to session, so they'll persist
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)
db.session.add(pet5)
db.session.add(pet6)
db.session.add(pet7)
db.session.add(pet8)

db.session.commit()