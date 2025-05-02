from kavenegar import *
from django.conf import settings
from django.http import HttpResponse
from celery import shared_task

@shared_task(queue='sms')
def send_welcome_sms(receptor):
    try:
        api= KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params= {'sender': '2000660110', 'receptor': receptor, 'message' :'به کلاسور خوش آمدید!' }
        api.sms_send(params)
    except APIException as e:
        return HttpResponse(f"API Exception: {e}")