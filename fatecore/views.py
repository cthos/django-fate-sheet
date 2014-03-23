from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.views import generic

from django.forms.models import inlineformset_factory

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from fatecore.models import *
from fatecore.forms import FateCharacterForm

# Create your views here.
class CharCreate(CreateView):
  model = FateCharacter

def index(request):
  # Limit to 10 characters
  character_list = FateCharacter.objects.order_by('id')[:10]
  template = loader.get_template('fatecore/index.html')
  context = RequestContext(request, {
      'characters_list': character_list,
  })
  return HttpResponse(template.render(context))

def new(request):
  charform = FateCharacterForm(request.POST)
  aspect_formset = inlineformset_factory(FateCharacter, FateAspect, can_delete = False, extra = 5)
  stunt_formset = inlineformset_factory(FateCharacter, FateStunt, can_delete = False, extra = 2)
  skill_formset = inlineformset_factory(FateCharacter, FateSkill, can_delete = False, extra = 5)

  if request.method == 'POST':
    if charform.is_valid() and aspect_formset(request.POST).is_valid():
      character = charform.save()

      aspect_formset(request.POST, instance = character).save()

      return HttpResponse("Yeah!")

  return TemplateResponse(request, 'fatecore/new.html', {
    'form': charform,
    'aspect_form': aspect_formset,
    'stunt_form' : stunt_formset,
    'skill_form' : skill_formset,
  })

class CharacterDetailView(generic.DetailView):
  model = FateCharacter
  template_name = 'fatecore/view.html'
  context_object_name = 'character'
