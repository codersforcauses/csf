from django import forms

from .models import Team

class CreateTeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name',)



class JoinTeamForm(forms.Form):
    join_code = forms.CharField(required=True, label='Enter Join Code')

    # Can put validation here