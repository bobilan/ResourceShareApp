from django import forms


class PostResourceForm(forms.Form):
    title = forms.CharField()
    link = forms.URLField()
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )

    category = forms.ChoiceField(
        widget=forms.Select,
        choices=[
            ('Python', 'Python'),
            ('HTML', 'HTML'),
            ('SQL', 'SQL'),
            ('API', 'API'),
        ]
    )

    tags = forms.ChoiceField(
        widget=forms.SelectMultiple,
        choices=[
            ('Beginner', 'Beginner'),
            ('Senior', 'Senior'),
            ('Middle', 'Middle'),
        ]
    )