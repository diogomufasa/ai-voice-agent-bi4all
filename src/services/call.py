from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Connect
from src.config import ACCOUNT_SID, AUTH_TOKEN, PHONE_NUMBER

def get_call_status(call_sid):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls(call_sid).fetch()
    return call.status

def make_call(phone_number=None):
    if phone_number is None:
        return None

    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        call = client.calls.create(
            to=phone_number,
            from_=PHONE_NUMBER,
            twiml= twiml_response()
        )

        print(f"Voice call initiated successfully!")
        return call
    

    except Exception as e:
        print(f"Error making call: {e}")
        return None
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        return None



def twiml_response():
    response = VoiceResponse()
    connect = Connect()
    connect.virtual_agent(
        connector_name="Dialogflow_CX_BI4ALL_test",
        # status_callback="your_status_callback_url"
    )
    response.append(connect)
    return response