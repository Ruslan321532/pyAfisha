from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'movie', 'stars')


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('title', 'description', 'duration', 'director', 'reviews', 'rating')

    def get_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            total_stars = sum(review.stars for review in reviews)
            return total_stars / len(reviews)
        return 0


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('name', 'movies_count')

    def get_movies_count(self, director):
        return director.movies.count()
