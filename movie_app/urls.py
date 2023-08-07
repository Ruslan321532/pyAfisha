from . import views
from django.urls import path

urlpatterns = [
    path('directors/', views.DirectorView.as_view({
        'get':'list', 'post':'create'})),
    path('directors/<int:pk>/', views.DirectorView.as_view({
        'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('movies/', views.MovieView.as_view({
        'get':'list', 'post':'create'})),
    path('movies/<int:pk>/', views.MovieView.as_view({
        'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('reviews/', views.ReviewView.as_view({'get':'list', 'post':'create'})),
    path('reviews/<int:pk>/', views.ReviewView.as_view({
        'get':'retrieve', 'put':'update', 'delete':'destroy'})),
    path('movies/reviews/', views.MovieListView.as_view()),
]

# urlpatterns = [
#     path('directors/', views.director_list_api_view),
#     path('directors/<int:id>/', views.dir_detail_api_view),
#     path('movies/', views.movie_list_api_view),
#     path('movies/<int:id>/', views.movie_detail_api_view),
#     path('reviews/', views.review_list_api_view),
#     path('reviews/<int:id>/', views.review_detail_api_view),
#     path('movies/reviews/', views.MovieListView.as_view()),
# ]