
from rest_framework import serializers

from .models import Org, Position, WhoAmI, Skill, Project, Event


class WhoAmISerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoAmI
        fields = '__all__'


class SkillSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class SkillMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id', 'skill_name', 'level', 'exp_years_as_text')


class OrgMiniSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Org
        fields = ('url', 'org_name')


class OrgSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Org
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    skill = SkillMiniSerializer(many=True)

    class Meta:
        model = Project
        # fields = '__all__'
        fields = (
            'project_name',
            'start_time',
            'end_time',
            'description',
            'impact',
            'take_away',
            'skill'
        )


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    skill = SkillMiniSerializer(many=True)
    company_name = OrgMiniSerializer(many=True)

    class Meta:
        model = Position
        fields = [
            'position_name',
            'team',
            'company_name',
            'start_time',
            'end_time',
            'skill',
            'description',
        ]


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
