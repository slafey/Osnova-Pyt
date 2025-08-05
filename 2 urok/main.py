from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib
import os


def main():
    load_dotenv()

    msg = MIMEMultipart()

    msg["From"] = os.environ['EMAIL_FROM']
    msg["To"] = os.environ['EMAIL_TO']
    msg["Subject"] = 'Тестовое письмо'
    password = os.environ['PASSWORD']

    progress_modules = ['Основый Python', 'GitHub', 'Api']
    completed_modules = ['Командная строка', 'Введение Python', 'Введение JS', 'WEB-разработка']
    time = '3 месяца'

    if completed_modules:
        message_text = f'Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. В процессе я выполнил модули: {completed_modules}! Сейчас я работаю над модулями {progress_modules}. Обучение мне нравится, я получил море знаний!'
    else:
        message_text = f'Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями {progress_modules}. Пока что я улучшаю свои навыки и узнаю много нового!'

    msg.attach(MIMEText(message_text, 'plain'))

    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(msg["From"], password)
    server.sendmail(msg["From"], msg["To"], msg.as_string())


if __name__ == '__main__':
    main()
