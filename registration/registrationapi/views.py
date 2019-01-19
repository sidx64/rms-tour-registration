from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from registration.registrationapi.serializers import RMSIndia2019Serializer
from registration.models import RMSIndia2019
from mailCode import send_email
import config
from tokens import account_activation_token
from datetime import datetime


@csrf_exempt
@api_view(['POST'])
def create_profile(request):
    """

    :param request:
    :return:
    """

    try:
        data = request.data
        post_data_list = ['fname', 'lname', 'email_id', 'designation', 'mobile_number', 'is_student',
                          'organization', ]

        for post_data in post_data_list:
            if post_data not in data:
                return Response(post_data + ' ' + 'information is missing',
                                status=status.HTTP_406_NOT_ACCEPTABLE)

        record = dict()
        record['fname'] = data['fname']
        record['lname'] = data['lname']
        record['email_id'] = data['email_id']
        record['designation'] = data['designation']
        record['mobile_number'] = data['mobile_number']
        record['is_student'] = data['is_student']
        record['organization'] = data['organization']
        code = account_activation_token.make_token(data['email_id'])
        record['verification_code'] = code

        check_email = RMSIndia2019.objects.filter(email_id=data['email_id'])

        if check_email.exists():
            return Response("This is email is already being used for another user,"
                            " please change your email ID",
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = RMSIndia2019Serializer(data=record)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            to_addr = data['email_id']
            link = "http://localhost:9000/api/verify/" + code
            body = """ 
                Greetings!

                You are receiving this email because you just registered for the RMS Tour of India 2019 Event. 
                To complete this registration, please click on the link provided below: \n
                """ + link + """ 
                Thank you! 
                - Team Name

                P.S.: If you did not register for this event, please ignore this email. 
                """
            subject = "RMS tour of 2019 - Confirm your registration"

            send_email(config.username, config.password, to_addr, body, subject)

            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print("exception", e)
        return Response("exception",
                        status=status.HTTP_417_EXPECTATION_FAILED)


@api_view(['GET', 'POST'])
def email_confirmation(request, code=None):
    try:
        print("code", code)
        if RMSIndia2019.objects.filter(verification_code=code).exists():
            RMSIndia2019.objects.filter(verification_code=code).update(is_verified=True,
                                                                       verification_time=datetime.now(),
                                                                       modified_datetime=datetime.now())

            to_addr = RMSIndia2019.objects.filter(verification_code=code).get().email_id
            body = """ 
                            Greetings!

                            You have successfully verified your email ID. 
                            Thank you for registering for the event. 
                             
                            - Team Name

                            P.S.: If you did not register for this event, please ignore this email. 
                            """
            subject = "RMS tour of 2019 - Confirm your registration"

            send_email(config.username, config.password, to_addr, body, subject)
            return Response("Confirmed Successfully",
                            status=status.HTTP_202_ACCEPTED)

        else:
            return Response("Invalid URL",
                            status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print("exception", e)
        return Response("exception",
                        status=status.HTTP_417_EXPECTATION_FAILED)
