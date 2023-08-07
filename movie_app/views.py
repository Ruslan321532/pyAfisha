from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import *
from movie_app.models import Movie, Director, Review
from rest_framework import viewsets


class DirectorView(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# @api_view(['GET', 'POST'])
# def director_list_api_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = DirectorSerializer(instance=directors, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializers = DirectorSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def dir_detail_api_view(request, id):
#     try:
#         directors = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'message': 'Director does not exist!'}, status=404)
#     if request.method == 'GET':
#         data = DirectorSerializer(instance=directors, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         serializer = DirectorSerializer(directors, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     else:
#         directors.delete()
#         return Response(status=200)
#
#
# @api_view(['GET', 'POST'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(instance=movies, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializers = MovieSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     try:
#         movies = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'message': 'Movie does not exist!'}, status=404)
#     if request.method == 'GET':
#         data = MovieSerializer(instance=movies, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movies, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewSerializer(instance=reviews, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializers = ReviewSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         reviews = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'message': 'Review does not exist!'}, status=404)
#     if request.method == 'GET':
#         data = ReviewSerializer(instance=reviews, many=False).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(reviews, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         reviews.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieWithReviewsSerializer
