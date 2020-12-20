from django import forms
from django.core import validators
from account_app.services.Userservice import UserService
from utilities.Base.BaseForms import BaseForm


userService = UserService()


# region " Register Form "
class RegisterForm(BaseForm):
    """ Register form """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد'),
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={}),
        label='رمز عبور',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={}),
        label='تکرار رمز عبور',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )

    def clean_email(self):
        """ Check Email Exist """
        email = self.cleaned_data.get('email')
        is_email_exist = userService.is_exists_user_by_email(email)
        if is_email_exist:
            raise forms.ValidationError('با این ایمیل قبلا ثبت نام شده است')

        return email

    def clean_re_password(self):
        """ Compare Password And Repassword """
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


# endregion " END Eegister Form "

# region " Login Form "
class LoginForm(BaseForm):
    """ Login Form """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد'),
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={}),
        label='رمز عبور',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )

    def clean_email(self):
        """ Check User Exist """
        email = self.cleaned_data.get('email')
        is_exists_user = userService.is_exists_user_by_email(email)
        if not is_exists_user:
            raise forms.ValidationError('کاربری با چنین مشخصاتی وجود ندارد')

        return email


# endregion " END Login Form "

# region " Forget Password Form "
class ForgetPassword(BaseForm):
    """ Forget Password Form """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={}),
        label='ایمیل',
        validators=[
            validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد'),
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )


# endregion " END Forget Password Form "

# region " Reset Password Form "
class ResetPasswordForm(BaseForm):
    """ Reset Password Form """
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={}),
        label='رمز عبور جدید شما',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={}),
        label='تکرار رمز عبور جدید',
        validators=[
            validators.MinLengthValidator(5, 'تعداد کاراکترهای وارد شده نمیتواند کمتر از 5 باشد'),
            validators.MaxLengthValidator(255, 'تعداد کاراکترهای وارد شده نمیتواند بیشتر از 255 باشد'),
        ]
    )

    active_code = forms.CharField(widget=forms.HiddenInput())
# endregion " END Reset Password Form "
