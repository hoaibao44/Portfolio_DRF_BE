from django.urls import include, path
from rest_framework import routers


from .views import CommentViewset, EventViewset, PositionViewset, ReplyViewset, WhoAmIViewset, SkillViewset, ProjectViewset, OrgViewset, get_mini_skill, CVFileViewset

router = routers.DefaultRouter()
router.register(r'api-infos', WhoAmIViewset)
router.register(r'api-skills', SkillViewset)
router.register(r'api-projects', ProjectViewset)
router.register(r'api-events', EventViewset)
router.register(r'api-positions', PositionViewset)
router.register(r'api-orgs', OrgViewset)
router.register(r'api-cmts', CommentViewset)
router.register(r'api-replys', ReplyViewset)
router.register(r'api-files', CVFileViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('mini-skill/', get_mini_skill)
]
