from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Review
        fields = ('text', 'movie', 'stars')


class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=10, max_length=20)

    class Meta:
        model = Movie
        fields = ('title', 'description', 'duration', 'director')


class MovieWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, movie):
        return movie.reviews.aggregate(Avg('stars'))['stars__avg']

    class Meta:
        model = Movie
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=10, max_length=30)
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('name', 'movies_count')

    def get_movies_count(self, director):
        return director.movies.count()
