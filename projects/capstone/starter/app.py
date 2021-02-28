import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from models import setup_db, Movie, Actor


def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response


    #actors section


    @app.route('/actors ', methods=['GET'])
    @requires_auth('get:actor')
    def get_actors():
        try:
            actors = Actor.query.all()
            if actors is None:
                abort(404)
            formatted_Actors = [Actor.format() for Actor in actors]
            return jsonify({
                'seccess': True,
                'actors': formatted_Actors
                })
        except:
            abort(500)


    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(id):
        try:
            actor = Actor.query.filter_by(id=id).one_or_none()
        except:
            abort(500)

        if actor is None:
            abort(404)

        try:
            actor.delete()
            return jsonify({
                'seccess': True,
                'deleted': id
                })
        except:
            abort(500)


    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor():
        try:
            body = request.get_json()
            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')

        except:
            abort(400)

        if not name:
            abort(400)
        if not age:
            abort(400)
        if not gender:
            abort(400)

        try:
            actor = Actor(name=name, age=age, gender=gender)
            actor.insert()
            return jsonify({
                'seccess': True,
                'created ': actor.id
                })
        except:
            abort(500)


    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def edit_actor(token, id):
        data = request.get_json()
        if not ('name' in data or 'age' in data or 'gender' in data):
            abort(422)
        name = data.get('name', None)
        age = data.get('age', None)
        gender = data.get('gender', None)
        
        actor = Actor.query.filter_by(id=id).one_or_none()
        if actor is None:
            abort(404)

        if name is not None:
            actor.name = name
        if age is not None:
            actor.age = age
        if gender is not None:
            actor.gender = gender

        actor.update()
        return jsonify({
            'success': "true",
            'updated': id
        })


    #movies section


    @app.route('/movies ', methods=['GET'])
    @requires_auth('get:movie')
    def get_Movies():
        try:
            movies = Movie.query.all()
            if movies is None:
                abort(404)
            formatted_Movies = [Movie.format() for Movie in movies]
            return jsonify({
                'seccess': True,
                'actors': formatted_Movies
                })
        except:
            abort(500)


    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(id):
        try:
            movie = Movie.query.filter_by(id=id).one_or_none()
        except:
            abort(500)

        if movie is None:
            abort(404)

        try:
            movie.delete()
            return jsonify({
                'seccess': True,
                'deleted': id
                })
        except:
            abort(500)


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie():
        try:
            body = request.get_json()
            title = body.get('title')
            release_date = body.get('release_date')

        except:
            abort(400)

        if not title:
            abort(400)
        if not release_date:
            abort(400)

        try:
            movie = Movie(title=title, release_date=release_date)
            movie.insert()
            return jsonify({
                'seccess': True,
                'created ': movie.id
                })
        except:
            abort(500)


    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def edit_movie(token, id):
        data = request.get_json()
        if not ('title' in data or 'release_date'):
            abort(422)

        title = data.get('title', None)
        release_date = data.get('release_date', None)

        movie = Movie.query.filter_by(id=id).one_or_none()
        if movie is None:
            abort(404)

        if title is not None:
            movie.title = title
        if release_date is not None:
            movie.age = release_date

        movie.update()
        return jsonify({
            'success': "true",
            'updated': id
        })

    #Error Handlers


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }), 404


    @app.errorhandler(422)
    def unprocessabley(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500


    @app.errorhandler(401)
    def Unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401


    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)