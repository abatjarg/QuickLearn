from django.forms import ModelForm, Textarea
from django import forms
from django.core.exceptions import ValidationError

from models import Card

class CardForm(ModelForm):
	class Meta():
		model = Card
		fields = ['front','back']
		widgets = {
            'front': Textarea(attrs={'cols': 70, 'rows': 10}),
            'back': Textarea(attrs={'cols': 70, 'rows': 10}),
        }
