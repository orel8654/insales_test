# from serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from service.settings import EMAIL_HOST_USER
from django.shortcuts import render

class CreateUserAPI(APIView):

    permission_classes = [AllowAny,]

    def get(self, request):
        param_id = request.GET.get('insales_id', None)
        param_shop = request.GET.get('shop', None)
        param_email = request.GET.get('user_email', None)
        param_user_id = request.GET.get('user_id', None)
        param_token = request.GET.get('token', None)
        print('token: ', param_token)
        print('user_id: ', param_user_id)
        print('email: ', param_email)
        print('insales_id: ', param_id)
        print('shop: ', param_shop)
        send_mail(
            'Tester//Insales',
            f'Token: {param_token}\nUser_ID: {param_user_id}\nEMAIL: {param_email}\nINSALES_ID: {param_id}\nSHOP: {param_shop}\n',
            EMAIL_HOST_USER,
            ['egorao@mail.ru'],
        )
        return Response({'status': 'OK'})

def index(request):
    return render(request, template_name='restapi/index.html', context={})