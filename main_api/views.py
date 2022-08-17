from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from .models import Comment, Event, Org, Position, WhoAmI, Skill, Project, Reply, CVFile
from .serializers import EventSerializer, OrgSerializer, PositionSerializer, SkillMiniSerializer, WhoAmISerializer, SkillSerializer, ProjectSerializer, CommentSerializer, ReplySerializer, CVFileSerializer

from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

test_per = permissions.AllowAny
prod_per = permissions.IsAuthenticatedOrReadOnly
per_here = prod_per


class WhoAmIViewset(viewsets.ModelViewSet):
    queryset = WhoAmI.objects.all().order_by("-id")
    serializer_class = WhoAmISerializer
    permission_classes = [per_here]


class CVFileViewset(viewsets.ModelViewSet):
    queryset = CVFile.objects.all()
    serializer_class = CVFileSerializer
    permission_classes = [per_here]


class SkillViewset(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [per_here]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SkillSerializer(instance, context={'request': request})
        return Response(serializer.data)


class PositionViewset(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [per_here]


class OrgViewset(viewsets.ModelViewSet):
    queryset = Org.objects.all().order_by("-id")
    serializer_class = OrgSerializer
    permission_classes = [per_here]


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [per_here]


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [per_here]

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


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-id")

    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CommentSerializer(instance)
        return Response(serializer.data)


class ReplyViewset(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [per_here]
