from django.http import JsonResponse
from django.conf import settings
from gigachat import GigaChat
from gigachat.models import Chat, ChatCompletion, Choices, Messages, MessagesRole

# Create your views here.
def main(request):
    return JsonResponse({"message": "Hello World"})

def get_prompt(request):
    prompt = request.GET.get('prompt', '')
    with  GigaChat(credentials=settings.GIGACHAT_API_KEY, verify_ssl_certs=False) as giga:
        giga.stream()
        response = giga.chat(Chat(
            messages=[
                Messages(
                    role=MessagesRole.SYSTEM,
                    content='Ты — Василий Кандинский'
                ),
                Messages(
                    role=MessagesRole.USER,
                    content=prompt
                )
            ],
            function_call='auto'
        ))
        # response = giga.chat(ChatCompletion(
        #     choices=[
        #         Choices(message=Messages(
        #             role=MessagesRole.USER,
        #             content=prompt
        #         ))
        #     ]
        # ))
        return JsonResponse({
            "message": response.choices[0].message.content
        })

