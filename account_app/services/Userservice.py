from account_app.services.IUserService import IUserService
from account_app import models
from polls_app.utilities.services.MailService import EmailService
import uuid


class UserService(IUserService):
    """ User Service"""

    # region " Register User "
    def register_user(self, email, password) -> models.User:
        email_active_code = uuid.uuid4()
        user = models.User.objects.create_user(
            email=email,
            password=password,
            is_active=False,
            email_active_code=email_active_code,
        )

        EmailService.send_email(
            subject='فالسازی حساب کاربری',
            context={'user': user},
            template_address='Emails/confirmation_email.html',
            to=email
        )

    # endregion " END Register User "

    def user_update_password(self, user_id, old_password, new_password) -> models.User:
        user = models.User.objects.get_queryset().get(id=user_id)
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
        else:
            return 'پسورد قدیمی شما اشتباه است'

    def user_update_data(self, user_id, avatar, gender, website, phone, address, last_name, first_name) -> models.User:
        user = models.User.objects.get_queryset().get(id=user_id)
        if avatar:
            user.avatar = avatar
        if website:
            user.website = website
        if gender:
            user.gender = gender
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if phone:
            user.phone = phone
        if address:
            user.address = address
        user.save()

    def get_user_by_id(self, user_id) -> models.User:
        return models.User.objects.get_queryset().prefetch_related('order_set').get(id=user_id)

    def get_user_by_email(self, email) -> models.User:
        return models.User.objects.get_queryset().get(email=email)

    def is_exists_user_by_username(self, username) -> models.User:
        return models.User.objects.filter(username=username).exists()

    def is_exists_user_by_password(self, password) -> models.User:
        return models.User.objects.filter(password=password).exists()

    def is_exists_user_by_email(self, email) -> models.User:
        return models.User.objects.filter(email=email).exists()

    def get_user_for_login(self, email, password) -> models.User or None:
        user_model = models.User
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_all_users(self):
        return models.User.objects.all()

    def get_user_by_activate_code(self, activate_code: str) -> models.User or None:
        user = models.User.objects.get_queryset().get(email_active_code=activate_code)
        if user is not None:
            return user
        else:
            return None

    def activate_user(self, user: models.User) -> models.User:
        user.is_active = True
        user.email_active_code = uuid.uuid4()
        user.save()
        return user

    def get_user_by_email_for_change_pass(self, email):
        user_model = models.User
        try:
            return user_model.objects.get_queryset().get(email=email)
        except user_model.DoesNotExist:
            return None
        else:
            return None

    def send_reset_password(self, email):
        user = self.get_user_by_email(email)
        EmailService.send_email(
            subject='Forgot password',
            context={'user': user},
            template_address='Emails/change_password.html',
            to=email
        )

    def create_new_active_code(self, user):
        user.email_active_code = uuid.uuid4()
        user.save()
        return user

    def update_password(self, user, new_password):
        user.set_password(new_password)
        self.create_new_active_code(user=user)
        user.save()
