from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .bot_logic import handle_message, show_main_menu, BotState
from .models import Dialog, Message
import json

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')
        session = request.session
        
        # Инициализация состояния
        if 'bot_state' not in session:
            session['bot_state'] = BotState.MENU
            session.save()
        
        # Обработка сообщения
        response_text, new_state = handle_message(
            user_message, 
            session['bot_state']
        )
        
        # Обновление состояния
        session['bot_state'] = new_state
        session.save()
        
        return JsonResponse({'response': response_text})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def chat_page(request):
    return render(request, 'bot/chat.html')