from captcha.widgets import ReCaptchaV2Checkbox
from captcha.fields import ReCaptchaField
from django.forms import forms
from app import settings
from captcha import widgets


class BaseForm(forms.Form):
    re_captcha = ReCaptchaField(
        public_key=settings.RECAPTCHA_PUBLIC_KEY,
        private_key=settings.RECAPTCHA_PRIVATE_KEY,
        widget=widgets.ReCaptchaV2Checkbox(
            attrs={'data-theme': 'dark'},
            api_params={'hl': 'fa'}
        ),
        error_messages={
            'required': 'لطفا تصویر امنیتی را تأیید کنید'
        }
    )
