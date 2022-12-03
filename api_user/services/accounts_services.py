from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import json
from api_user.models import Roles, Profiles, Accounts
from api_user.serializer import Accounts_write_serializers, Accounts_serializers
from django.db.models import Q
from api_base.services import Send_Mail_Service
from api_base.services import Multi_Thread
from email_template.html_parse import Htmlfilter


class Accounts_services:
    @classmethod
    def register_with_roles(cls, pk, data, *args, **kwargs):
        from rabbit_mq import publish
        if pk is not None:
            role = Roles.objects.filter(name=pk)
            if not role.exists():
                return Response(data="Role not in database", status=status.HTTP_400_BAD_REQUEST)
            role = role.first()
            username = data.get("username", None)
            password = data.get("password", None)
            email = data['profile'].get("email", None)
            certificate = data['profile'].get('certificate', None)
            if username and password:
                if Accounts.objects.filter(username=username).exists():
                    return Response(data="username already in database", status=status.HTTP_400_BAD_REQUEST)
            if email and certificate:
                if Profiles.objects.filter(Q(email=email) | Q(certificate=certificate)).exists():
                    return Response(data="email or certificate already in database", status=status.HTTP_400_BAD_REQUEST)

            data['roles'] = role.id.hex
            data['password'] = make_password(password)
            account_serializer = Accounts_write_serializers(data=data)
            if account_serializer.is_valid(raise_exception=True):
                account = account_serializer.save()

                multi_thread = Multi_Thread(html=Htmlfilter.parse_html_text(), target=Send_Mail_Service.send_mail,
                                            content_main_body='Sign up success welcome to shopbbe,'
                                                              'website:https://shopbee.loca.lt/',
                                            header='Sign up success!!!',
                                            from_email='', to_emails=[data['profile'].get('email')])
                multi_thread.start()
                account_serializers = Accounts_serializers(instance=account)
                try:
                    publish(method='register', body=json.dumps(
                        {
                            'message': json.dumps(account_serializers.data)
                        }), routing_key='Register' + pk.title() + 'Event')
                except:
                    print('Re push data to consumer')
                    publish(method='register', body=json.dumps(
                        {
                            'message': json.dumps(account_serializers.data)
                        }), routing_key='Register' + pk.title() + 'Event')

                return Response(data=account_serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def upload_file(cls, file):
        fs = FileSystemStorage()
        current_date = datetime.now()
        file_name = fs.save(name=current_date.strftime("%m_%d_%Y,%H_%M_%S_") + file.name, content=file)
        return fs.url(file_name)
