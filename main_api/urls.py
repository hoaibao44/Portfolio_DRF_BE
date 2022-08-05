from django.urls import include, path
from rest_framework import routers


from .views import EventViewset, PositionViewset, WhoAmIViewset, SkillViewset, ProjectViewset, OrgViewset, get_mini_skill

router = routers.DefaultRouter()
router.register(r'api-infos', WhoAmIViewset)
router.register(r'api-skills', SkillViewset)
router.register(r'api-projects', ProjectViewset)
router.register(r'api-events', EventViewset)
router.register(r'api-positions', PositionViewset)
router.register(r'api-orgs', OrgViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('mini-skill/', get_mini_skill)
]
