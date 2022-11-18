from django import forms
from .models import PostCategory, Post, Comment


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = PostCategory
        fields = ['category']
        labels = {'category': 'Category'}
        widgets = {'category': forms.TextInput(attrs={'class': 'form-control'})}

    def save(self, commit=True):
        try:
            category = super(NewCategoryForm, self).save(commit=False)
            category.category = self.cleaned_data['category']
        except Exception as e:
            print(e)
            messages = e
            return messages
        if commit:
            category.save()
        return category


class NewPostForm(forms.Form):
    category = forms.ModelChoiceField(queryset=PostCategory.objects.all(),
                                      widget=forms.Select(attrs={'class': 'input-category'}))
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input-title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-content'}))

    class Meta:
        model = Post
        fields = ['category', 'title', 'content']
        labels = {'category': 'Categoria', 'title': 'Título', 'content': 'Conteúdo'}
        widgets = {'category': forms.Select(attrs={'class': 'input-category'}),
                   'title': forms.TextInput(attrs={'class': 'input-title'}),
                   'content': forms.Textarea(attrs={'class': 'input-content'})}

    def save(self, commit=True):
        try:
            post = super(NewPostForm, self).save(commit=False)
            post.category = self.cleaned_data['category']
            post.title = self.cleaned_data['title']
            post.content = self.cleaned_data['content']
        except Exception as e:
            print(e)
            messages = e
            return messages
        if commit:
            post.save()
        return post
