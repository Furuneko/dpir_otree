from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']


class BeforeResultsWP(WaitPage):
    def after_all_players_arrive(self):
        # TODO: call the group method to set the players' payoffs
        pass


class Results(Page):
    pass


# TODO: create the corresponding template and add the logic to display this page only in the last round
class FinalResults(Page):
    pass


page_sequence = [
    Intro,
    Contribution,
    BeforeResultsWP,
    Results,
    FinalResults
]
