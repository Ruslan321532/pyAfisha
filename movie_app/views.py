from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import MovieSerializer, ReviewSerializer, DirectorSerializer
from movie_app.models import Movie, Director, Review


@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(instance=directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def dir_detail_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'message': 'Director does not exist!'}, status=404)
    data = DirectorSerializer(instance=directors, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'message': 'Movie does not exist!'}, status=404)
    data = MovieSerializer(instance=movies, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Review does not exist!'}, status=404)
    data = ReviewSerializer(instance=reviews, many=False).data
    return Response(data=data)
