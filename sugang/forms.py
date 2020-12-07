from django.forms import inlineformset_factory
from sugang.models import Subject, Apply

SubjectInlineFormSet = inlineformset_factory(Subject, Apply, fields=['name', 'number', 'major'], extra=2)
