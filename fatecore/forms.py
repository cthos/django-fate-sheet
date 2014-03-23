from django.forms import ModelForm
from fatecore.models import FateCharacter

class FateCharacterForm(ModelForm):
  class Meta:
    model = FateCharacter
    
