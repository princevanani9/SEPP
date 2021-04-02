from django import forms
from django.db.models import fields
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model=Candidate
        fields = ['name','Description','image','election_type']

