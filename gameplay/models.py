from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.DO_NOTHING)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F')


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    be_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
