from django.core import validators

from utilities.Base.BaseForms import BaseForm
from django import forms


# region " Contact Us Form "

class ContactUsForm(BaseForm):
    """ Contant Us form """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد'),
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ],
    )

    name = forms.CharField(
        label='نام و نام خانوادگی',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(120, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 120 باشد'),
        ]
    )

    mobile = forms.CharField(
        label='شماره تلفن همراه',
        validators=[
            validators.MinLengthValidator(11, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 11 باشد'),
            validators.MaxLengthValidator(13, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 13 باشد'),
        ]
    )

    topic = forms.CharField(

        label='موضوع',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(120, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 120 باشد'),
        ]
    )

    message = forms.CharField(
        label='پیام',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(1000, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 1000 باشد'),
        ],
        widget=forms.Textarea
    )

    # endregion " END Contact Us Form "
