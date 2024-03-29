from django import forms
from .models import Post
from .models import Category


#choices = [('coding','coding'),('sports',),('entertainment','entertainment'),]
choices = Category.objects.all().values_list("name", "name")
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'title_tag','author','category', 'body','image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'elder','type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control','placeholder':choices}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'elder'}),
            'category':forms.Select (choices=choice_list, attrs={"class":"form-control"}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            
        }

        