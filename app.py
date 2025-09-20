from flask import Flask
from flask_restful import Api
from models import db
from controller import LibraryListResource, LibraryResource

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

api.add_resource(LibraryListResource, '/libraries')
api.add_resource(LibraryResource, '/libraries/<string:isbn>')

if __name__ == '__main__':
    app.run(debug=True)