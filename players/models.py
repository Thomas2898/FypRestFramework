from django.contrib.gis.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Player(models.Model):
    name = models.CharField(max_length=50)
    DOB = models.CharField(max_length=50)
    ##teamID = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    Home_Team = models.CharField(max_length=50)
    Away_Team = models.CharField(max_length=50)
    Referee = models.CharField(max_length=50)
    Date = models.DateField()
    Time = models.CharField(max_length=50)
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Score(models.Model):
    FixtureID = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    Home_goal = models.IntegerField()
    Home_point = models.IntegerField()
    Away_goal = models.IntegerField()
    Away_point = models.IntegerField()

    def __str__(self):
        return self.name

class Statistics(models.Model):
    Player_ID = models.ForeignKey(Player, on_delete=models.CASCADE)
    Fixture_ID = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    Pass = models.IntegerField()
    Pass_Miss = models.IntegerField()
    Point = models.IntegerField()
    Point_Miss = models.IntegerField()
    Goal = models.IntegerField()
    Goal_Miss = models.IntegerField()
    Turnover = models.IntegerField()
    Dispossessed = models.IntegerField()
    Block = models.IntegerField()
    Kickout_won = models.IntegerField()
    Kickout_lost = models.IntegerField()
    Goal_save = models.IntegerField()
    Goal_conceded = models.IntegerField()
    Yellow_card = models.IntegerField()
    Red_card = models.IntegerField()
    Black_card = models.IntegerField()



def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Player, self).save(*args, **kwargs)
