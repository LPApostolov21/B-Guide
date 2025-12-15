# app.py

from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sHq1wYwXk3ZpB6rT9vD2mJ4nL7fE0aC8iU5oG7hI9jK0lM2nO4pQ6rS8tV1uW3xY5z'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'lpapostolov27@gmail.com'
app.config['MAIL_PASSWORD'] = 'ukug nkxl sklo gyqc'
app.config['MAIL_DEFAULT_SENDER'] = 'lpapostolov27@gmail.com'

mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/b-guide')
def b_guide():
    return render_template('b-guide.html')


@app.route('/contact', methods=['POST'])
def handle_contact():
    if request.method == 'POST':
        sender_name = request.form.get('name')
        sender_email = request.form.get('email')
        message_content = request.form.get('message')

        recipient_email = 'lpapostolov27@gmail.com'

        msg = Message(
            subject=f"Ново Съобщение от Burgas Overview | Подател: {sender_name} ({sender_email})",
            recipients=[recipient_email],
            body=f"Име на подателя: {sender_name}\nИмейл на подателя: {sender_email}\n\nСъобщение:\n{message_content}"
        )

        try:
            mail.send(msg)
            flash('Вашето съобщение беше успешно изпратено!', 'success')
            print(f"Имейлът беше успешно изпратен от {sender_name} ({sender_email}).")
        except Exception as e:
            flash(f'Грешка при изпращане на имейл. Моля, опитайте по-късно. (Детайл: {e})', 'danger')
            print(f"ГРЕШКА при изпращане на имейл: {e}")

        return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)