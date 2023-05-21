from flask import Blueprint, jsonify

# Models
from models.NoticiaModel import NoticiaModel

main = Blueprint('noticias_blueprint', __name__)


@main.route('/')
def get_noticias():
    try:
        noticias = NoticiaModel.get_movies()
        return jsonify(noticias)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<query>')
def get_movie_query(query):
    try:
        noticia = NoticiaModel.get_movie_query(query)
        if noticia != None:
            return jsonify(noticia)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
