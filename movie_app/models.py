from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Review for {self.movie.title}"
