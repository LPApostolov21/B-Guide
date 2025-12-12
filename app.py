# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

# Инициализация на Flask приложението
app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Пример за Gmail
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True  # Използване на TLS
app.config['MAIL_USERNAME'] = 'lpapostolov27@gmail.com'  # <-- ВАШИЯТ ИЗХОДЯЩ ИМЕЙЛ
app.config['MAIL_PASSWORD'] = '#'  # <-- ВАШАТА ПАРОЛА/APP PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = 'lpapostolov27@gmail.com'  # <-- ВАШИЯТ ИЗХОДЯЩ ИМЕЙЛ

mail = Mail(app)



# Дефиниране на маршрута за началната страница (Home Page)
@app.route('/')
def home():
    return render_template('home.html')


# Дефиниране на маршрут за страницата B-Guide (ако вече е създадена)
@app.route('/b-guide')
def b_guide():
    return render_template('b-guide.html')

# Дефиниране на маршрут за обработка на формата за контакти
@app.route('/contact', methods=['POST'])
def handle_contact():
    """
    Обработва формата за контакти и изпраща имейл.
    Данните НЕ се запазват в база данни.
    """
    if request.method == 'POST':
        # 1. Вземане на данните от формата
        sender_email = request.form.get('email')
        message_content = request.form.get('message')

        recipient_email = 'lpapostolov27@gmail.com'

        # 2. Създаване на имейл съобщението
        msg = Message(
            subject=f"Ново Съобщение от Burgas Overview | Подател: {sender_email}",
            recipients=[recipient_email],  # Имейлът, до който се изпраща съобщението
            body=f"Имейл на подателя: {sender_email}\n\nСъобщение:\n{message_content}"
        )

        # 3. Изпращане на имейла
        try:
            mail.send(msg)
            print(f"Имейлът беше успешно изпратен до {recipient_email} от {sender_email}.")
            # Можете да добавите Flash съобщение за успех тук, ако използвате Flash
        except Exception as e:
            print(f"ГРЕШКА при изпращане на имейл: {e}")
            # Можете да добавите Flash съобщение за грешка тук

        # 4. Пренасочване обратно към началната страница
        return redirect(url_for('home'))


@app.route('/about')
def about():
    return render_template('about.html')


# Стартиране на приложението
if __name__ == '__main__':
    app.run(debug=True)