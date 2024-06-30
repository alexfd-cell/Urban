
def send_email(message, recipient, sender="university.help@gmail.com"):
# 1. Блок проверки символа @ в наименовании адреса эл. почты получателя и отправителя
    for i in range(len(recipient)):
        if recipient[i] != '@':
            check_recipient = False
        else:
            check_recipient = True
            break
    for i in range(len(sender)):
        if sender[i] != '@':
            check_sender = False
        else:
            check_sender = True
            break
# --------------------------------------------------------------------------------
# 2. Блок проверки адреса эл. почты получателя и отправителя на наличие .com, .ru, .net
    dot = recipient.rfind('.')
    if (recipient[dot:len(recipient)] == '.com'
            or recipient[dot:len(recipient)] == '.ru'
            or recipient[dot:len(recipient)] == '.net'):
        check_recipient = True
    else:
        check_recipient = False
    dot = sender.rfind('.')
    if (sender[dot:len(sender)] == '.com'
            or sender[dot:len(sender)] == '.ru'
            or sender[dot:len(sender)] == '.net'):
        check_sender = True
    else:
        check_sender = False
# --------------------------------------------------------------------------------
# 3. Блок проверки эквивалентности адреса эл. почты отправителя и получателя
    if recipient == sender:
        checkRS = False
    else:
        checkRS = True
# --------------------------------------------------------------------------------
# 4. Блок подведения итогов
    if check_recipient == False or check_sender == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if checkRS == False:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
# --------------------------------------------------------------------------------

message = input('Введите текст сообщения: ')
recipient = input('Введите адрес электронной почты получателя: ')
user_input = input("По умолчанию задан адрес электронной почты university.help@gmail.com\n"
                   "Желаете отправить сообщение с другого адреса эл. почты? 1-да/0-нет (1/0): ")
if user_input.lower() == "1":
    sender = input('Введите адрес электронной почты отправителя: ')
    send_email(message, recipient, sender)
else:
    send_email(message, recipient)