from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from players.models import Player, Team, Score, Fixture, Statistics
from players.serializers import PlayerSerializer, TeamSerializer, ScoreSerializer, FixtureSerializer, StatisticSerializer
from .forms import HomeForm
from rest_framework.generics import ListAPIView


@api_view(['GET', 'POST'])
def player_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Player.objects.all()
        serializer = PlayerSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        print("In player list")
        ##d = Team(id=1, name="Thomas Davis")
        ##c = Player(id=9, name="Thomas", DOB='28/01/1998')
        ##d.players.add(c)
        ##data = request.data['Home_Team']
        ##snippet = Player.objects.get(name=name)
        print(request.data['TeamID'])
        if serializer.is_valid():
            player = Player(name=request.data['name'], DOB=request.data['DOB'])
            player.save()
            print(player.name)
            print(player.id)
            ##serializer.save()
            addPlayer = Player(id=player.id, name=request.data['name'], DOB=request.data['DOB'])
            team = Team(id=request.data['TeamID'])
            team.players.add(addPlayer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def player_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlayerSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlayerSerializer(snippet, data=request.data)
        print("In player detail")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def player_detail_name(request, name, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Player.objects.filter(name=name)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print("hello")
        print(snippet)
        playername = str(snippet)
        serializer = PlayerSerializer(snippet, many=True)
        ##queryset = Player.objects.raw("select id, name from players_Player where name = "+"'"+playername+"'")
        ##serializer = PlayerSerializer(list(queryset), many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlayerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def team_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Team.objects.all()
        serializer = TeamSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeamSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def score_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Score.objects.all()
        serializer = ScoreSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def score_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Score.objects.get(pk=pk)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScoreSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ScoreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def fixture_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Fixture.objects.all()
        serializer = FixtureSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        ##c = Score(FixtureID = snippets, Home_goal=0, Home_point=0, Away_goal=0, Away_point=0)
        ##d = Fixture(Home_Team='Thomas Davis', Away_Team='Ballyboden', scoreID=c, Referee='Gerry Burns', Date=24-3-2019, Time='02:00', Location='K road')
        serializer = FixtureSerializer(data=request.data)
        data = request.data['Home_Team']
        fixture = Fixture(Home_Team=request.data['Home_Team'], Away_Team=request.data['Away_Team'], Referee=request.data['Referee'], Date=request.data['Date'], Time=request.data['Time'], Location=request.data['Location'])
        print(serializer)
        print("Thisssssssssssss")
        print(data)
        if serializer.is_valid():
            print("Its valid")
            fixture = Fixture(Home_Team=request.data['Home_Team'], Away_Team=request.data['Away_Team'],
                              Referee=request.data['Referee'], Date=request.data['Date'], Time=request.data['Time'],
                              Location=request.data['Location'])
            fixture.save()
            ##serializer.save()
            score = Score(FixtureID=fixture, Home_goal=0, Home_point=0, Away_goal=0, Away_point=0)
            score.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fixture_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Fixture.objects.get(pk=pk)
    except Fixture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FixtureSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FixtureSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
def stat_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Statistics.objects.all()
        print(snippets)
        serializer = StatisticSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StatisticSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            p = Player(id = request.data['Player_ID'])
            f = Fixture(id = request.data['Fixture_ID'])
            stat = Statistics(Player_ID = p, Fixture_ID = f,
            Pass=0, Pass_Miss = 0, Point=0,
            Point_Miss=0, Goal=0, Goal_Miss=0,
            Turnover=0, Dispossessed=0, Block=0,
            Kickout_won=0, Kickout_lost=0, Goal_save=0,
            Goal_conceded=0, Yellow_card=0, Red_card=0,
            Black_card=0)
            stat.save()
            ##serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stat_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Statistics.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StatisticSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StatisticSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def PlayersStats(request, Player_ID, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Statistics.objects.filter(Player_ID=Player_ID)
        ##qs = Statistics.objects.all()
        ##print("Test")
        ##passI = snippet.values('Pass') + snippet.values('Pass_Miss')
        print(snippet.values('Pass'))
        ##pID = str(snippet)
    except Statistics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ##queryset2 = Statistics.objects.raw("select * from players_Statistics where Player_ID = "+"'"+pID+"'")
        ##queryset2 = Player.objects.raw("select * from players_Statistics where Player_ID = 9")
        ##serializer = StatisticSerializer(list(queryset2), many=True)
        serializer = StatisticSerializer(snippet,many=True)
        return Response(serializer.data)





def test(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HomeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = Player()
            return HttpResponseRedirect('http://127.0.0.1:8000/world/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HomeForm()
    return render(request, "test.html", {'form': form})

