from django import forms

from .models import Review

class ReviewCreateForm(forms.ModelForm):
	product = forms.CharField(label='Product Name:', widget=forms.TextInput(
		attrs = {
			"placeholder": "Product Name"
		}
		))
	author = forms.CharField(label='Author:', widget=forms.TextInput(
		attrs = {
			"placeholder": "Author Name"
		}
		))
	rating = forms.Select()
	body = forms.CharField(label='Review', widget=forms.Textarea(
		attrs={
			"placeholder": "Review"
		}
		))
	featured = forms.BooleanField(label="Featured Review:")
	active = forms.BooleanField(label="Actively Displayed:")

	class Meta:
		model = Review
		fields = [
			'product',
			'author',
			'rating',
			'body',
			'featured',
			'active'
		]