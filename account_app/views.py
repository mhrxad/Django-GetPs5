from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from account_app import forms, models
from account_app.services.Userservice import UserService

user_service = UserService()


def register_user(request):
    """ Register User """
    if request.user.is_authenticated:
        return redirect(reverse('home:home'))

    register_form: forms.RegisterForm = forms.RegisterForm(request.POST or None)

    if register_form.is_valid():
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user_service.register_user(email=email, password=password)
        messages.add_message(
            request,
            messages.SUCCESS,
            'ثبت نام شما با موفقیت انجام شد. ایمیلی جهت فعالسازی حساب کاربری برای شما ارسال گردید.'
        )
        return redirect(reverse('account:login'))

    context = {
        'page_title': 'ثبت نام',
        'register_form': register_form
    }
    return render(request, 'Register.html', context)


def login_user(request):
    """ Loging User """
    if request.user.is_authenticated:
        return redirect(reverse('home:home'))

    login_form: forms.LoginForm = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        remember_me = login_form.cleaned_data.get('remember_me')
        user = user_service.get_user_for_login(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                messages.add_message(request, messages.SUCCESS, 'شما با موفقیت وارد شدید')
                return redirect(reverse('home:home'))
            else:
                login_form.add_error('email', 'حساب کاربری شما فعال نمیباشد')
        else:
            login_form.add_error('email', 'کاربری با چنین مشخصاتی وجود ندارد')

    context = {
        'page_title': 'ورود',
        'login_form': login_form
    }
    return render(request, 'Login.html', context)


@login_required()
def logout_user(request):
    """ Logout User """
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'شما با موفقیت خارج شدید')
    return redirect(reverse('account:login'))


def activate_account(request, *args, **kwargs):
    """ Active User Account """
    if request.user.is_authenticated:
        return redirect(reverse('home:home'))

    activate_code = kwargs.get('activate_code')
    if activate_code:
        try:
            user = user_service.get_user_by_activate_code(activate_code)
        except models.User.DoesNotExist:
            raise Http404
        if user is not None:
            user_service.activate_user(user)
            messages.add_message(request, messages.SUCCESS, 'حساب کاربری شما با موفقیت فعال شد')
            return redirect('/login')

    return redirect(reverse('home:home'))


def forget_password(request):
    if request.user.is_authenticated:
        return redirect('/')

    # ------------------- Change Password form -------------------#
    forget_password_form: forms.ForgetPassword = forms.ForgetPassword(request.POST or None)
    if forget_password_form.is_valid():
        email = forget_password_form.cleaned_data.get('email')
        user = user_service.get_user_by_email(email)
        if user is not None:
            if user.is_active:
                user_service.send_reset_password(email=email)
                messages.add_message(request, messages.SUCCESS, 'ایمیلی جهت تایید پسورد جدید برای شما ارسال گردید')
            else:
                forget_password_form.add_error('email', 'حساب کاربری شما فعال نمیباشد')
        else:
            forget_password_form.add_error('email', 'کاربری با این ایمیل وجود ندارد')
    context = {
        'page_title': 'فراموشی رمز عبور',
        'forget_password_form': forget_password_form
    }
    return render(request, 'ForgetPassword.html', context)


def reset_password(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect(reverse('home:home'))

    selected_active_code = kwargs['activate_code']
    reset_password_form: forms.ResetPasswordForm = forms.ResetPasswordForm(request.POST or None,
                                                                           initial={
                                                                               'active_code': selected_active_code}
                                                                           )

    if reset_password_form.is_valid():
        new_password = reset_password_form.cleaned_data.get('password')
        old_active_code = reset_password_form.cleaned_data.get('active_code')
        user = user_service.get_user_by_activate_code(old_active_code)
        if user is not None:
            user_service.update_password(user=user, new_password=new_password)
            # user_service.create_new_active_code(user=user)
            messages.add_message(request, messages.SUCCESS, 'رمز عبور شما تغییر کرد')
            return redirect(reverse('account:login'))

    context = {
        'page_title': 'تغییر رمز عبور',
        'reset_password_form': reset_password_form
    }
    return render(request, 'ResetPassword.html', context)
