from django.shortcuts import render, redirect
import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


__all__ = (
    'send_sms',
)

def send_sms(request):
    # set api key, api secret
    if request.method == 'POST':
        text = request.POST.get('text')
        number = request.POST.get('number')

        api_key = "NCSGLMHSQ2FTVZUA"
        api_secret = "6SJTTSSM27RIGTG3ERVXKFLKVWVEUHFI"

        params = dict()
        params['from'] = '01044321237'  # Sender number
        params['to'] = number  # Recipients Number '01000000000,01000000001'
        params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
        params['text'] = text  # Message

        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

    return render(request, 'send/sms.html')
        # next_path = request.POST.get('next-path', 'sms:send-sms')
        # return redirect(next_path)
