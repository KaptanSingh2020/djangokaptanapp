from django.forms import ModelForm
from .models import Sentence


class SentenceForm(ModelForm):
    class Meta:
        model = Sentence
        fields = ['text', 'tense_choice']
