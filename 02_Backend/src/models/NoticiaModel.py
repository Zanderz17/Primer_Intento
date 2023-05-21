from database.db import get_connection
from .entities.Noticia import Noticia


class NoticiaModel():

    @classmethod
    def get_movies(self):
        try:
            connection = get_connection()
            noticias = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "select id, titular, ts_rank_cd(par_vector, query) as rank from noticias, phraseto_tsquery('inclusión laboral') query order by 3 desc limit 5")
                resulset = cursor.fetchall()
                for row in resulset:
                    noticia = Noticia(row[0], row[1], row[2])
                    noticias.append(noticia.to_JSON())

            connection.close()
            return noticias

        except Exception as ex:
            raise Exception(ex)

    #########################################################

    @classmethod
    def get_movie_query(self, query):
        try:
            connection = get_connection()
            noticias = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "select id, titular, ts_rank_cd(par_vector, query) as rank from noticias, phraseto_tsquery(%s) query order by 3 desc limit 5", (query,))  # Necesita ser tupla
                resulset = cursor.fetchall()
                for row in resulset:
                    noticia = Noticia(row[0], row[1], row[2])
                    noticias.append(noticia.to_JSON())

            connection.close()
            return noticias

        except Exception as ex:
            raise Exception(ex)
