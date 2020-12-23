from django import forms
from django.core import validators

from polls_app.utilities.Base.BaseForms import BaseForm


class CommentsForm(BaseForm):
    """ Comments form """
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا نظر خود را وارد کنید'}),
        label='افزودن دیدگاه',
        validators=[
            validators.MinLengthValidator(3, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 3 باشد'),
        ]
    )
    parent_id = forms.CharField(widget=forms.HiddenInput(), required=False)



