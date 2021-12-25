import random
import math
import hashlib
import json
from django.core.validators import validate_email
from django.utils import timezone

class Helper:

    def getRandom(self):
        return math.ceil(random.random() * 1000000)

    def passwordEncrypt(self, password):
        return hashlib.sha256(str(password).encode("utf-8")).hexdigest()

    def isEmailValid(self, email):
        valid_email = False
        try:
            validate_email(email)
            valid_email = True
        except:
            valid_email = False
        return valid_email
    
    def parseJson(self, request):
         return json.loads(request.decode("utf-8"))

    
    def getDateTime(self):
        return timezone.datetime.now()

    def empty(self, text):
        return not str(text)

    def vistor_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip