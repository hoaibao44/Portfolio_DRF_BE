from asyncio import events
from audioop import maxpp
from codecs import backslashreplace_errors
from decimal import MAX_EMAX
from turtle import position
from django.db import models


# Create your models here.


class Skill(models.Model):
    '''Model definition for Skill.'''

    skill_name = models.CharField(max_length=100)
    exp_years = models.IntegerField(null=True)
    level = models.CharField(max_length=100, null=True)
    learning_method = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)

    class Meta:
        '''Meta definition for Skill.'''

        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'

    def __str__(self):
        return self.skill_name

    def exp_years_as_text(self):
        return f'{self.exp_years} years'


class Org(models.Model):
    '''Model definition for Org.'''

    org_name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    class Meta:
        '''Meta definition for Org.'''

        verbose_name = 'Org'
        verbose_name_plural = 'Orgs'

    def __str__(self):
        return self.org_name


class Position(models.Model):
    '''Model definition for Position.'''

    position_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    company_name = models.ManyToManyField(
        Org, related_name="p_org", blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    skill = models.ManyToManyField(
        Skill, related_name="ps_skill", blank=True)
    description = models.TextField(max_length=100, null=True)

    class Meta:
        '''Meta definition for Position.'''

        verbose_name = 'Position'
        verbose_name_plural = 'Position'

    def __str__(self):
        return f'{self.position_name} //from {self.start_time} to {self.end_time}'


class Project(models.Model):
    '''Model definition for Project.'''

    project_name = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()
    description = models.TextField(max_length=500)
    impact = models.CharField(max_length=100)
    skill = models.ManyToManyField(
        Skill, related_name="pj_skill", blank=True)
    position = models.ManyToManyField(
        Position, related_name="pj_position", blank=True)
    take_away = models.TextField(max_length=500)

    class Meta:
        '''Meta definition for Project.'''

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name


class Event(models.Model):
    '''Model definition for Event.'''

    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField(max_length=500)
    skill = models.ManyToManyField(
        Skill, related_name="e_skill", blank=True)
    org = models.ManyToManyField(
        Org, related_name="org", blank=True)
    project = models.ManyToManyField(Project, related_name="prj", blank=True)

    class Meta:
        '''Meta definition for Event.'''

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.event_name


class Hobbies(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class WhoAmI(models.Model):
    '''Model definition for WhoAmI.'''
    full_name = models.CharField(max_length=100)
    profile_img_url = models.CharField(max_length=500, blank=True)
    sex = models.CharField(max_length=100)
    birth_day = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    hobbies = models.ManyToManyField(
        Hobbies, related_name='hobbies', blank=True)
    description = models.TextField(max_length=500)

    git_url = models.CharField(max_length=500, blank=True)
    ig_url = models.CharField(max_length=500, blank=True)
    mail = models.CharField(max_length=500, blank=True)

    skill_set = models.ManyToManyField(
        Skill, related_name="skill", blank=True)

    orgs = models.ManyToManyField(Org, related_name='main_org', blank=True)

    class Meta:
        '''Meta definition for WhoAmI.'''

        verbose_name = 'WhoAmI'
        verbose_name_plural = 'WhoAmIs'

    def __str__(self):
        return self.full_name
