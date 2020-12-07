from django.forms import inlineformset_factory
from photo1.models import Album1, Photo1

PhotoInlineFormSet = inlineformset_factory(Album1, Photo1, fields=['image', 'album', 'description'], extra=2)
