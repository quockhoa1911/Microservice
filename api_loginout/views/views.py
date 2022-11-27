import json

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..serializer import MyTokenSerializers
from api_user.models import Accounts, Accounts_Roles, Roles, Payment_type
from api_user.serializer import Accounts_serializers, Account_Role_serializers
from django.contrib.auth.hashers import check_password, make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

jwt_authenticator = JWTAuthentication()

from api_base.services import Multi_Thread, Send_Mail_Service
import string
import random
from email_template.html_parse import Htmlfilter

# Rabbitmq
from rabbit_mq import publish, publish_history


# if import function in file, python complite the file and use function for hanlde

# Create your views here.


class LoginoutViews(ModelViewSet):
    serializer_class = MyTokenSerializers
    scopes_view = {
        'active_deactive_account_role': 'admin:update',
        'change_password': 'admin:update',
        'change_password_with_role_admin': 'admin:update',
        'change_password': 'admin:update,shop:update,user:update',
        'forgot_password': None
    }

    @action(methods=['POST'], detail=True, name='login')
    def login(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class
        try:
            if pk is None:
                return Response(data="Invalid type role login", status=status.HTTP_400_BAD_REQUEST)
            username = request.data.get("username")
            password = request.data.get("password")
            account_role = Accounts_Roles.objects.filter(
                Q(account__username=username) & Q(role__name=pk.lower()) & Q(is_active=True))
            if account_role.exists():
                account_role = account_role.first()
                account = account_role.account
                if not check_password(password, account.password):
                    return Response("is incorrect password", status=status.HTTP_400_BAD_REQUEST)

                string_html = Htmlfilter.parse_html_text()
                multi_thread = Multi_Thread(html=string_html, target=Send_Mail_Service.send_mail,
                                            content_main_body='Content_main_body', header='Welcome to Shopbee',
                                            from_email='',
                                            to_emails=[account.profile.email])
                multi_thread.start()
                body = {
                    "account": account.id.hex,
                    "descriptions": f"action:{self.action},role:{pk}"
                }
                publish_history(method=self.action, body=json.dumps(body), routing_key=self.action)
                return Response(serializer.get_token(account_role.account, account_role.role),
                                status=status.HTTP_200_OK)
            return Response('not account in database', status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            raise Exception
            return Response("data is not valid", status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PUT'], detail=True, name='change_password_with_role_admin')
    def change_password_with_role_admin(self, request, pk, *args, **kwargs):
        data = request.data
        account = Accounts.objects.filter(pk=pk).first()
        password = data.get('password', None)
        old_password = data.get('old_password', None)
        if password and old_password:
            account.password(make_password(password))
            account.save()
            profile = account.profile[0]

            multi_thread = Multi_Thread(target=Send_Mail_Service.send_mail,
                                        html=f"password is {data.get('password')}",
                                        header='change password success',
                                        content_main_body='Password already change',
                                        to_emails=[profile.email])
            multi_thread.start()
            return Response(data='change password success', status=status.HTTP_200_OK)

    @action(methods=['PUT'], detail=False, name='change_password', url_path='me/change_password')
    def change_password(self, request, *args, **kwargs):
        pk = request.user.id.hex
        password = request.data.get('password', None)
        old_password = request.data.get('old_password', None)
        if password and old_password:
            account = Accounts.objects.filter(pk=pk)
            if account.exists():
                account = account.first()
                assert check_password(old_password, account.password)
                account.password = make_password(password)
                account.save()
                multi_thread = Multi_Thread(target=Send_Mail_Service.send_mail,
                                            html=f"password is {password}",
                                            header='change password success',
                                            content_main_body='Password already change',
                                            to_emails=[account.profile.email])
                multi_thread.start()
                return Response(data='change_password_success', status=status.HTTP_200_OK)
            return Response(data='data is not in database', status=status.HTTP_400_BAD_REQUEST)
        return Response(data='please send full fields require', status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True, name='active_deactive_account_role')
    def active_deactive_account_role(self, request, pk=None, *args, **kwargs):
        account_role = Accounts_Roles.objects.filter(pk=pk)
        if len(account_role):
            account_role = account_role.first()
            account_role.is_active = not account_role.is_active
            account_role.save()
            publish(method='login',
                    body=json.dumps({'message': json.dumps(Account_Role_serializers(instance=account_role).data)}),
                    routing_key='Active_deactive_account_role' + pk + 'User')
            return Response('update account_role success', status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False, name='forgot_password')
    def forgot_password(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        certificate = data.get('certificate')
        account = Accounts.objects.filter(
            Q(username=username) & Q(profile__email=email) & Q(profile__certificate=certificate))
        if account.exists():
            account = account.first()
            letters = string.ascii_letters
            rand_number = random.choice(range(8, 15))
            pass_rand = ''
            for i in range(rand_number):
                pass_rand += random.choice(letters)
            password = make_password(pass_rand)
            account.password = password
            account.save()
            multi_thread = Multi_Thread(target=Send_Mail_Service.send_mail,
                                        html=f"password is {pass_rand} ",
                                        header='change password success',
                                        content_main_body='Password already change',
                                        to_emails=[f"{email}"])
            multi_thread.start()
            return Response(data='password already reset,check email to get new password', status=status.HTTP_200_OK)
        return Response(data='data is not correct,please check data', status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, name='decode_token')
    def decode_token(self, request, *args, **kwargs):
        response = jwt_authenticator.authenticate(request=request)
        user, token = response
        print(token.payload)
        return Response(data="Ok", status=status.HTTP_200_OK)
