from .IContactUsService import IContactUsService
from contactus_app import models


class ContactUsService(IContactUsService):
    def send_message_from_contact_us(self, email, name, mobile, topic, message):
        models.ContactUs.objects.create(email=email, name=name, mobile=mobile, topic=topic, message=message)
