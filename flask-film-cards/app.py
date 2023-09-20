from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Dummy data
movies = [
    {
        'id': 1,
        'title': "Movie 1",
        'description': "Some random movie"
    },
    {
        'id': 2,
        'title': "Movie 2",
        'description': "Another random movie"
    }
]

class Movie(Resource):
    def get(self, movie_id):
        movie = next((movie for movie in movies if movie["id"] == movie_id), None)
        if movie:
            return jsonify(movie)
        return {"message": "Movie not found"}, 404

    # More CRUD operations can be added here...

api.add_resource(Movie, "/movies/<int:movie_id>")

if __name__ == "__main__":
    app.run(debug=True)
