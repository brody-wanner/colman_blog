from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text', 'image', 'youtube_video')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
			'text': forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off'}),
			'youtube_video': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Paste YouTube URL here...'})
		}

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('text',)
		widgets = {
		    'text': forms.TextInput(attrs={'placeholder': 'Add a comment here...', 'class': 'form-control', 'autocomplete': 'off'}),
		}