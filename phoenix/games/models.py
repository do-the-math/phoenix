
from django.conf import settings
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import models, transaction
from django import forms

from phoenix.accounts.models import User
# from phoenix.games.managers.match_manager import MatchManager
from phoenix.games.constants import *


class BaseTimeClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Score(BaseTimeClass):
    match_played = models.IntegerField(default=0)
    match_won = models.IntegerField(default=0)
    player = models.OneToOneField('Player',
                                  on_delete=models.CASCADE,
                                  related_name='score')

    def __str__(self):
        return str(self.match_played)


class Player(BaseTimeClass):

    user_orig = models.OneToOneField(User,
                                     on_delete=models.SET_NULL,
                                     null=True)

    matches = models.ManyToManyField('Match',
                                     through='MatchPlayerMembership',
                                     related_name='player_list',)

    last_played = models.DateTimeField(auto_now_add=True, db_index=True)
    user_agent = models.CharField(max_length=254, blank=True, null=True)
    channel = models.CharField(
        max_length=10, choices=CHANNEL_CHOICES, blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = ("Player")
        verbose_name_plural = ("Players")

    def __str__(self):
        return "players "+str(self.id)


class Match(BaseTimeClass):
    game_type = models.CharField(choices=GAME_TYPE_CHOICES,
                                 default=TICTACTOE_GAME,
                                 max_length=20,
                                 null=False,)
    players = models.ManyToManyField('Player',
                                     through='MatchPlayerMembership',
                                     related_name='players',)

    def __str__(self):
        return "Match #"+str(self.id)

    class Meta:
        verbose_name_plural = "Matches"


class MatchPlayerMembership(BaseTimeClass):

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    is_first_player = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['player', 'match'], name='unique appversion'
            )
        ]

    def __str__(self):
        return "MatchPlayerMembership #"+str(self.id)
