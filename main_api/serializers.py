
from rest_framework import serializers

from .models import Hobbies, Org, Position, WhoAmI, Skill, Project, Event


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
    skill = SkillMiniSerializer(many=True)
    org = OrgMiniSerializer(many=True)

    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_date',
            'description',
            'skill',
            'org',
            'project'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    skill = SkillMiniSerializer(many=True)
    position = PositionSerializer(many=True)

    class Meta:
        model = Project
        # fields = '__all__'
        fields = (
            'project_name',
            'position',
            'start_time',
            'end_time',
            'description',
            'impact',
            'take_away',
            'skill'
        )


class HobbiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobbies
        fields = '__all__'


class WhoAmISerializer(serializers.ModelSerializer):
    skill_set = SkillMiniSerializer(many=True)
    orgs = OrgSerializer(many=True)
    hobbies = HobbiesSerializer(many=True)

    class Meta:
        model = WhoAmI
        fields = [
            'full_name',
            'profile_img_url',
            'sex',
            'birth_day',
            'location',
            'hobbies',
            'description',
            'git_url',
            'ig_url',
            'mail',
            'skill_set',
            'orgs'
        ]
