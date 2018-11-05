from django import template
from django.conf import settings
register = template.Library()

@register.filter
def sort_models(models):
    count = len(models)
    models.sort(
        key = lambda x:
            settings.APP_MODEL_ORDER.index(x['name'])
            if x['name'] in settings.APP_MODEL_ORDER
            else count
    )
    return models
