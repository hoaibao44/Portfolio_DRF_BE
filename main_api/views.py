from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from .models import Event, Org, Position, WhoAmI, Skill, Project
from .serializers import EventSerializer, OrgSerializer, PositionSerializer, SkillMiniSerializer, WhoAmISerializer, SkillSerializer, ProjectSerializer

from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class WhoAmIViewset(viewsets.ModelViewSet):
    queryset = WhoAmI.objects.all()
    serializer_class = WhoAmISerializer
    permission_classes = [permissions.AllowAny]


class SkillViewset(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SkillSerializer(instance, context={'request': request})
        return Response(serializer.data)


class PositionViewset(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.AllowAny]


class OrgViewset(viewsets.ModelViewSet):
    queryset = Org.objects.all()
    serializer_class = OrgSerializer
    permission_classes = [permissions.AllowAny]


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProjectSerializer(instance)
        return Response(serializer.data)


@api_view(['GET'])
def get_mini_skill(request):
    """
    List all code Skill, or create a new snippet.
    """
    if request.method == 'GET':
        skill = Skill.objects.all()
        serializer = SkillMiniSerializer(skill, many=True)
        return Response(serializer.data)
