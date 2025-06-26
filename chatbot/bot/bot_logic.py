class BotState:
    MENU = 0
    PROJECTS = 1
    APPOINTMENT = 2
    CONTACTS = 3

def handle_message(user_message, current_state):
    user_message = user_message.lower().strip()
    
    if current_state == BotState.MENU:
        if "проект" in user_message:
            return "Наши проекты:\n1. ЖК 'Ромашка'\n2. ЖК 'Солнечный'\n3. ЖК 'Лесной'", BotState.PROJECTS
        elif "запись" in user_message:
            return "Введите ваше имя и телефон:", BotState.APPOINTMENT
        elif "контакт" in user_message:
            return "Наши контакты:\nТелефон: +7 (495) 123-45-67\nEmail: info@example.com", BotState.CONTACTS
        else:
            return show_main_menu(), BotState.MENU
    
    elif current_state == BotState.APPOINTMENT:
        # Здесь можно сохранить данные в БД
        return f"Спасибо! Данные '{user_message}' сохранены. Чем еще помочь?\n" + show_main_menu(), BotState.MENU
    
    return show_main_menu(), BotState.MENU

def show_main_menu():
    return (
        "Добро пожаловать! Выберите опцию:\n"
        "1. Наши проекты\n"
        "2. Запись на консультацию\n"
        "3. Контакты"
    )