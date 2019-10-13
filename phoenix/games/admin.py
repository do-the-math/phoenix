from django import forms
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.db import IntegrityError
from django.forms import inlineformset_factory


from phoenix.games.models import *


class ScoreInline(admin.StackedInline):
    title = 'Player`s Score'
    model = Score
    extra = 0


class MatchPlayerMembershipForm(forms.ModelForm):
    class Meta:
        model = MatchPlayerMembership
        fields = '__all__'


class MatchPlayerMembershipFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        # get forms that actually have valid data
        player_count = 0
        winner_count = 0
        game_type = None
        for form in self.forms:
            try:
                game_type = form.data.get('game_type')
                if form.cleaned_data:
                    player_count += 1
                    winner_count += (
                        1 if form.cleaned_data.get('game_type') else 0)
            except AttributeError:
                # annoyingly, if a subform is invalid Django explicity raises
                # an AttributeError for cleaned_data
                pass

        if(game_type == TICTACTOE_GAME):
            if(player_count > 2):
                raise forms.ValidationError(
                    'Number of Players In {} should be atmost 2'.format(game_type))
            elif(winner_count > 1):
                raise forms.ValidationError(
                    'Cant have more than one winner in {}'.format(game_type))

        elif(game_type == NIM_GAME):
            if(player_count > 3):
                raise forms.ValidationError(
                    'Number of Players In {} should be atmost 4'.format(game_type))
        pass


class MatchPlayerMembershipInline(admin.TabularInline):
    title = 'Players in the Match'
    verbose_name = 'Players in the Match'
    readonly_fields = ('edit_link',)

    model = MatchPlayerMembership
    extra = 0
    can_delete = False
    form = MatchPlayerMembershipForm
    formset = MatchPlayerMembershipFormset

    def edit_link(self, obj):
        return format_html(u'<a href="{}">Edit</a>', '../../'+str(obj.id))


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['game_type', 'players', ]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'game_type', )
    readonly_fields = ('updated_at', 'created_at',)
    inlines = [MatchPlayerMembershipInline, ]
    form = MatchForm


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'score',)
    readonly_fields = ('channel',)
    inlines = [MatchPlayerMembershipInline, ScoreInline]


admin.site.register(MatchPlayerMembership)
