from django import forms

from mainpage.models import Application, Course


class ApplyForm(forms.Form):
	name = forms.CharField(label='Ваши фаимилия и имя',
						   widget=forms.TextInput(attrs={'class': 'custom-input', 'style': 'width: 100%'}))
	phone = forms.CharField(label='Телефон',
							widget=forms.TextInput(attrs={'class': 'custom-input'}))
	program = forms.ModelChoiceField(queryset=Course.objects.all(), required=True,
									 widget=forms.Select(attrs={'class': 'select-styled'}),
									 label='Программа')

	class Meta:
		model = Application
		fields = ('name', 'phone')
