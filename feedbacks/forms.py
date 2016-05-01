from django import forms
from feedbacks.models import Feedback
import datetime

class FeedbackForm(forms.ModelForm):
    
	create_date = forms.DateTimeField(initial=datetime.datetime.now, widget = forms.DateTimeInput(attrs={'readonly':'readonly'}))

   
	class Meta:
		model = Feedback
        #exclude = ('create_date',)