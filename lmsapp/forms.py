from django import forms
from .models import AndyModel
from .models import InstModel
from .models import LerModel


class AndyForm(forms.ModelForm):
	class Meta:
		model = AndyModel
		fields = "__all__"

class InstForm(forms.ModelForm):
	class Meta:
		model = InstModel
		fields = "__all__"

class LerForm(forms.ModelForm):
	class Meta:
		model = LerModel
		fields = "__all__"