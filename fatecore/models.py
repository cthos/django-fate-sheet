from django.db import models

# Create your models here.

class FateCharacter(models.Model):

  name = models.CharField(max_length = 255)

  refresh = models.IntegerField()

  physical_stress_boxes = models.IntegerField()
  mental_stress_boxes = models.IntegerField()

class FateAspect(models.Model):

  description = models.TextField()
  character = models.ForeignKey(FateCharacter)

class FateStunt(models.Model):

  name = models.CharField(max_length = 255)
  description = models.TextField()
  character = models.ForeignKey(FateCharacter)

class FateSkill(models.Model):
  skills = (
    ('Athletics', 'Athletics'),
    ('Burglery', 'Burglery'),
    ('Contacts', 'Contacts'),
    ('Crafts', 'Crafts'),
    ('Deceive', 'Deceive'),
    ('Drive', 'Drive'),
    ('Empathy', 'Empathy'),
    ('Fight', 'Fight'),
    ('Investigate', 'Investigate'),
    ('Lore', 'Lore'),
    ('Notice', 'Notice'),
    ('Physique', 'Physique'),
    ('Provoke', 'Provoke'),
    ('Rapport', 'Rapport'),
    ('Resources', 'Resources'),
    ('Shoot', 'Shoot'),
    ('Stealth', 'Stealth'),
    ('Will', 'Will')
  )

  skill_levels = (
    ('1', 'Average (+1)'),
    ('2', 'Fair (+2)'),
    ('3', 'Good (+3)'),
    ('4', 'Great (+4)'),
  )

  name = models.CharField(max_length = 255, choices = skills)
  level = models.CharField(max_length = 255, choices = skill_levels)
  character = models.ForeignKey(FateCharacter)
