from django import template
register = template.Library()

@register.filter(name='times')
def times(number):
  number = int(number)
  return range(number)
