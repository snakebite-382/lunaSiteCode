from django import forms

from .models import Article

class ArticleCreateForm(forms.ModelForm):
	title = forms.CharField(
		label='Article title:',
		widget=forms.TextInput(
			attrs={"placeholder": "Title"})
		)
	author = forms.CharField(label='Article author:',
		widget=forms.TextInput(
			attrs={"placeholder": "Author"})
		)
	main = forms.CharField(label='',
							required=True,
							widget=forms.Textarea(
								attrs={
									'placeholder': 'Article Body',
									'rows': 25,
									'cols': 50,
								})
							)
	teaserSummary = forms.CharField(label='Summary',
									widget = forms.TextInput(
											attrs={
												'placeholder': "A Short Summary",
											}
										)
									)
	articleOfTheWeek = forms.BooleanField(label='Article Of The Week', required=False)
	class Meta:
		model = Article
		fields = [
			'title',
			'author',
			'main',
			'teaserSummary',
			'featured',
			'articleOfTheWeek',
			'active',
			'slug'
		]
