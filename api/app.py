from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db, Contact
from seed import seed_database

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

seed_database(app)


@app.route('/')
def home():
    return 'Flask API server'


@app.route("/api/contacts/")
@app.route("/api/contacts/<int:contact_id>")
def contacts(contact_id=None):
    if contact_id:
        contact = Contact.query.get(contact_id)
        if not contact:
            return jsonify({'message': 'Contact not found'}), 404
        return jsonify({'contact': contact.print()}), 200
    else:
        contacts = Contact.query.all()
        if not contacts:
            return jsonify({'message': 'No contacts available'}), 200
        return jsonify({'contacts': [contact.print() for contact in contacts]}), 200


@app.route('/api/contacts/favorites')
def favorite_contacts():
    favorites = Contact.query.filter(Contact.favorite == True).all()
    if not favorites:
        return jsonify({'message': 'No favorite contacts'}), 200
    return jsonify({'favorites': [contact.print() for contact in favorites]}), 200


if __name__ == "__main__":
    app.run()
