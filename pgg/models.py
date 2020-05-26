from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pgg'
    players_per_group = 3
    num_rounds = 2
    endowment = 100
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    individual_share = models.IntegerField()

    def set_payoffs(self):

        self.total_contribution = sum([p.contribution for p in self.get_players()])

        # TODO: write code to calculate and store individual share of total contributions


        # TODO: write code to calculate individual payoff (which cannot be 0)
        for p in self.get_players():
            p.payoff = 0



class Player(BasePlayer):
    # TODO: further limit range of possible contributions
    contribution = models.IntegerField(max=Constants.endowment)
