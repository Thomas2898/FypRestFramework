from rest_framework.generics import ListAPIView
from rest_framework import serializers
from players.models import Player, Team, Score, Fixture, Statistics, LANGUAGE_CHOICES, STYLE_CHOICES


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'DOB')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.DOB = validated_data.get('DOB', instance.DOB)
        instance.save()
        return instance

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'players')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.players = validated_data.get('players', instance.players)
        instance.save()
        return instance

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'FixtureID', 'Home_goal', 'Home_point', 'Away_goal', 'Away_point')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Score.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.FixtureID = validated_data.get('FixtureID', instance.FixtureID)
        instance.Home_goal = validated_data.get('Home_goal', instance.Home_goal)
        instance.Home_point = validated_data.get('Home_point', instance.Home_point)
        instance.Away_goal = validated_data.get('Away_goal', instance.Away_goal)
        instance.Away_point = validated_data.get('Away_point', instance.Away_point)
        instance.save()
        return instance

class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields = ('id', 'Home_Team', 'Away_Team', 'Referee', 'Date', 'Time', 'Location')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Fixture.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.Home_Team = validated_data.get('Home_Team', instance.Home_Team)
        instance.Away_Team = validated_data.get('Away_Team', instance.Away_Team)
        instance.Referee = validated_data.get('Referee', instance.Referee)
        instance.Date = validated_data.get('Date', instance.Date)
        instance.Time = validated_data.get('Time', instance.Time)
        instance.Location = validated_data.get('Location', instance.Location)
        instance.save()
        return instance


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('id', 'Player_ID', 'Fixture_ID', 'Pass', 'Pass_Miss', 'Point', 'Point_Miss', 'Goal', 'Goal_Miss', 'Turnover', 'Dispossessed', 'Block', 'Kickout_won', 'Kickout_lost', 'Goal_save', 'Goal_conceded', 'Yellow_card', 'Red_card', 'Black_card')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Statistics.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.Player_ID = validated_data.get('Player_ID', instance.Player_ID)
        instance.Fixture_ID = validated_data.get('Fixture_ID', instance.Fixture_ID)
        instance.Pass = validated_data.get('Pass', instance.Pass)
        instance.Pass_Miss = validated_data.get('Pass_Miss', instance.Pass_Miss)
        instance.Point = validated_data.get('Point', instance.Point)
        instance.Point_Miss = validated_data.get('Point_Miss', instance.Point_Miss)
        instance.Goal = validated_data.get('Goal', instance.Goal)
        instance.Goal_Miss = validated_data.get('Goal_Miss', instance.Goal_Miss)
        instance.Turnover = validated_data.get('Turnover', instance.Turnover)
        instance.Dispossessed = validated_data.get('Dispossessed', instance.Dispossessed)
        instance.Block = validated_data.get('Block', instance.Block)
        instance.Kickout_won = validated_data.get('Kickout_won', instance.Kickout_won)
        instance.Kickout_lost = validated_data.get('Kickout_lost', instance.Kickout_lost)
        instance.Goal_save = validated_data.get('Goal_save', instance.Goal_save)
        instance.Goal_conceded = validated_data.get('Goal_conceded', instance.Goal_conceded)
        instance.Yellow_card = validated_data.get('Yellow_card', instance.Yellow_card)
        instance.Red_card = validated_data.get('Red_card', instance.Red_card)
        instance.Black_card = validated_data.get('Black_card', instance.Black_card)
        instance.save()
        return instance


