from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from registration.registrationapi.serializers import RMSIndia2019Serializer
from registration.models import RMSIndia2019
from mailCode import send_email
import config


@csrf_exempt
@api_view(['POST'])
def create_profile(request):
    """

    :param request:
    :return:
    """

    try:
        data = request.data
        post_data_list = ['fname' , 'lname' , 'email_id' , 'designation' , 'mobile_number' , 'is_student' ,
                          'organization' , ]

        for post_data in post_data_list:
            if post_data not in data:
                return Response(post_data + ' ' + 'information is missing' ,
                                status=status.HTTP_406_NOT_ACCEPTABLE)

        record = dict()
        record['fname'] = data['fname']
        record['lname'] = data['lname']
        record['email_id'] = data['email_id']
        record['designation'] = data['designation']
        record['mobile_number'] = data['mobile_number']
        record['is_student'] = data['is_student']
        record['organization'] = data['organization']

        check_email = RMSIndia2019.objects.filter(email_id=data['email_id'])

        if check_email.exists():
            return Response("This is email is already being used for another user,"
                            " please change your email ID" ,
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = RMSIndia2019Serializer(data=record)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            code = "testing code"
            to_addr = data['email_id']
            body = """ 
                Greetings!

                You are receiving this email because you just registered for the RMS Tour of India 2019 Event. 
                To complete this registration, please click on the link provided below: \n
                """ + code + """ 
                Thank you! 
                - Team Name

                P.S.: If you did not register for this event, please ignore this email. 
                """
            subject = "test"

            send_email(config.username , config.password , to_addr , body, subject)

            return Response(serializer.data ,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors ,
                            status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print("exception" , e)
        return Response("exception" ,
                        status=status.HTTP_417_EXPECTATION_FAILED)

