from flask import Flask
from flask_cors import CORS
import os
from database import db
from routes import register_routes

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

    # Configure SQLite database
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pharmacy.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initializing database with app
    db.init_app(app)

    # Registration routes
    register_routes(app)

    # database tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')