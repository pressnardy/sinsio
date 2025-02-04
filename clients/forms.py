from django import forms
from clients.models import Client
from django.contrib.auth.models import User

# instantiated form for editing the client model and the required fields
class ClientForm(forms.ModelForm):

	class Meta:
		model = Client

		fields = [
			"id", "name", "policy_number", "registration_number", "phone_number",
			"start_date", "end_date", "renewal_date", "amount", 'created_by',
	  	]

		#adding CSS classes and IDs for forms fields for use in front end
		widgets = {
			
			"name": forms.TextInput(attrs={
				'class': 'input-text',
				'id': 'client-name',
			}),
			"policy_number": forms.TextInput(attrs={
				'class': 'input-text',
				'id': 'policy-number',
			}),
			"registration_number": forms.TextInput(attrs={
				'class': 'input-text',
				'id': 'registration-number',
			}),
			
			"start_date": forms.TextInput(attrs={
				'type': 'date', 'class': 'input-date',
				'id': 'start-date',
			}),
			"end_date": forms.TextInput(attrs={
				'type': 'date', 'class': 'input-date', 'id': 'end-date',
			}),
			"renewal_date": forms.TextInput(attrs={
				'type': 'date', 'class': 'input-date', 'id': 'renewal-date',
			}),
			"amount": forms.TextInput(attrs={
				'class': 'input-text', 'id': 'amount',
			}),
			"created_by": forms.TextInput(attrs={
				'class': 'input-text', 'placeholder': 'Amount', 'id': 'amount',
			}),
			"phone_number": forms.TextInput(attrs={
				'class': 'input-text',
				'id': 'phone-number',
			}),
		}


class SearchForm(forms.Form):
	CATEGORY_CHOICES = [
		('name', 'Name'),
		('policy_number', 'Policy Number'),
		('registration_number', 'Registration Number'),
	]
	category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)
	query = forms.CharField(max_length=50, required=True, min_length=1,
		widget=forms.TextInput(attrs={
			'class': 'query', 'id': 'query', 'placeholder': 'query'
		}))


class EditClient(forms.ModelForm):
	class Meta:
		model = Client
		fields = '__all__'









