from django.contrib.auth.forms import forms
from .models import Post



class CreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'file',)