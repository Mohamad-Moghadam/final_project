from kavenegar import *
from django.conf import settings
from django.http import HttpResponse
from celery import shared_task



@shared_task(queue='informing_sms')
def send_informing_SMS(receptor):
    try:
        api= KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params= {'sender': '2000660110', 'receptor': receptor, 'message' : f"پاسخی برای سوال شما ارسال شد" }
        api.sms_send(params)
    except APIException as e:
        return HttpResponse(f"API Exception: {e}")