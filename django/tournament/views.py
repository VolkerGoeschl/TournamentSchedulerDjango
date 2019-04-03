from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Tournament, Division

# Create your views here.

class TournamentListView(ListView):
    template_name = 'tournament-list.html'
    queryset = Tournament.objects.all()
    context_object_name = 'tournaments'

class TournamentDetailView(TemplateView):

    template_name = 'tournament_detail.html'

    def get_context_data(self, **kwargs):

        tournament = Tournament.objects.get(id=self.kwargs['tid'])

        division_seed = {
            div : [
                seed.teamPlaceholder.team_name
                for seed in div.divisionseed_set.all()
            ]
            for div in tournament.division_set.all()
        }

        context = {
            'tournament' : tournament,
            'division_seed' : division_seed,
            #''

        }

        return context

class DivisionSystemView(TemplateView):

    template_name = 'division_system.html'

    def get_context_data(self, **kwargs):

        division = Division.objects.get(id = self.kwargs['did'])

        groups = {

            group : [
                seed.teamPlaceholder.team_name
                for seed in group.groupseed_set.all()
            ]
            for group in division.group_set.all()
        }

        context = {
            'division' : division,
            'groups' : groups,
            'matches' : division.match_set.all().order_by('group__phase','phase_block','id')
        }

        return context

class ScheduleView(TemplateView):

    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):

        tournament = Tournament.objects.get(id=self.kwargs['tid'])

        if 'did' in self.kwargs:
            schedules = tournament.schedule_set.filter(match__division__id = self.kwargs['did'])
        elif 'pid' in self.kwargs:
            schedules = tournament.schedule_set.filter(pitch__id = self.kwargs['pid'])
        else:
            schedules = tournament.schedule_set.all()

        context = {
            'tournament' : tournament,
            'pitches' : tournament.pitch_set.all(),
            'schedules' : schedules,
        }

        return context
