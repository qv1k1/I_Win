
import streamlit as st


# Заголовок приложения
st.title('Добро пожаловать в мое приложение!')

# Поля ввода
name = st.text_input('Ваше имя:')
age = st.number_input('Ваш возраст:', min_value=1, max_value=120, value=18)

# Кнопка для отправки
if st.button('Отправить'):
    st.success(f'Привет, {name}! Тебе {age} лет.')

# Начальный баланс и список событий
START_BALANCE = 200000
events = [
    {'day': 1, 'description': 'Купили порошок со скидкой', 'amount': 1399},
    {'day': 2, 'description': 'Купили новые ботинки', 'amount': 3000},
    {'day': 3, 'description': 'Заказали еду на дом', 'amount': 1000},
    {'day': 4, 'description': 'Посетили кинотеатр', 'amount': 800},
    {'day': 5, 'description': 'Купили продукты на неделю', 'amount': 3500},
    {'day': 6, 'description': 'Оплатили интернет', 'amount': 500},
    {'day': 7, 'description': 'Заправили автомобиль', 'amount': 2500},
    {'day': 8, 'description': 'Посетили салон красоты', 'amount': 2000},
    {'day': 9, 'description': 'Купили новую книгу', 'amount': 600},
    {'day': 10, 'description': 'Посетили тренажерный зал', 'amount': 1000},
    {'day': 11, 'description': 'Оплатили подписку на сервис', 'amount': 399},
    {'day': 12, 'description': 'Поездка на такси', 'amount': 700},
    {'day': 13, 'description': 'Заказали ужин с доставкой', 'amount': 1200},
    {'day': 14, 'description': 'Посетили кафе с друзьями', 'amount': 1500},
    {'day': 15, 'description': 'Купили спортивную одежду', 'amount': 5000},
    {'day': 16, 'description': 'Оплатили страхование автомобиля', 'amount': 15000},
    {'day': 17, 'description': 'Оплатили коммунальные услуги', 'amount': 4500},
    {'day': 18, 'description': 'Посетили курсы по программированию', 'amount': 20000},
    {'day': 19, 'description': 'Оплатили услуги стоматолога', 'amount': 7000},
    {'day': 20, 'description': 'Купили бытовую технику', 'amount': 25000},
    {'day': 21, 'description': 'Купили подарки друзьям', 'amount': 5000},
    {'day': 22, 'description': 'Сделали пожертвование в благотворительный фонд', 'amount': 1000},
    {'day': 23, 'description': 'Купили новую одежду', 'amount': 8000},
    {'day': 24, 'description': 'Оплатили кредит', 'amount': 10000},
    {'day': 25, 'description': 'Заказали билеты на концерт', 'amount': 2500},
    {'day': 26, 'description': 'Посетили ресторан на выходных', 'amount': 4000},
    {'day': 27, 'description': 'Обновили смартфон', 'amount': 50000},
    {'day': 28, 'description': 'Сделали ремонт в квартире', 'amount': 100000},
    {'day': 29, 'description': 'Оплатили курсы английского языка', 'amount': 20000},
    {'day': 30, 'description': 'Купили велосипед', 'amount': 30000},
    {'day': 31, 'description': 'Организовали вечеринку', 'amount': 15000},
]

# Инициализация состояния
if 'balance' not in st.session_state:
    st.session_state.balance = START_BALANCE
if 'day' not in st.session_state:
    st.session_state.day = 0

if st.session_state.day < len(events):
    event = events[st.session_state.day]
    st.write(f"### День {event['day']}: {event['description']}")
    st.write(f"💰 Цена: {event['amount']} руб.")
    st.write(f"Ваш текущий баланс: {st.session_state.balance} руб.")

    # Кнопки для принятия решения
    if st.button('✔️ Участвую', key='participate'):
        st.session_state.balance -= event['amount']
        st.session_state.day += 1

    if st.button('❌ Не участвую', key='skip'):
        st.session_state.day += 1

    # st.experimental_rerun()  # Можно убрать этот вызов
else:
    st.write("## Игра завершена!")
    st.write(f"Ваш итоговый баланс: {st.session_state.balance} руб.")
    if st.button('Начать сначала'):
        st.session_state.balance = START_BALANCE
        st.session_state.day = 0
        # st.experimental_rerun()  # Этот метод тоже можно убрать





# from flask import Flask, render_template_string, request, redirect, url_for, session

# import streamlit as st

# # Заголовок приложения
# st.title('Добро пожаловать в мое приложение!')

# # Поля ввода
# name = st.text_input('Ваше имя:')
# age = st.number_input('Ваш возраст:', min_value=1, max_value=120, value=18)

# # Кнопка для отправки
# if st.button('Отправить'):
#     st.success(f'Привет, {name}! Тебе {age} лет.')

# app = Flask(__name__)
# app.secret_key = 'super_secret_key'  # Нужен для работы сессии, замените на более сложный ключ

# # Начальный баланс и список событий
# START_BALANCE = 200000
# events = [
#     {'day': 1, 'description': 'Купили порошок со скидкой', 'amount': 1399},
#     {'day': 2, 'description': 'Купили новые ботинки', 'amount': 3000},
#     {'day': 3, 'description': 'Заказали еду на дом', 'amount': 1000},
#     {'day': 4, 'description': 'Посетили кинотеатр', 'amount': 800},
#     {'day': 5, 'description': 'Купили продукты на неделю', 'amount': 3500},
#     {'day': 6, 'description': 'Оплатили интернет', 'amount': 500},
#     {'day': 7, 'description': 'Заправили автомобиль', 'amount': 2500},
#     {'day': 8, 'description': 'Посетили салон красоты', 'amount': 2000},
#     {'day': 9, 'description': 'Купили новую книгу', 'amount': 600},
#     {'day': 10, 'description': 'Посетили тренажерный зал', 'amount': 1000},
#     {'day': 11, 'description': 'Оплатили подписку на сервис', 'amount': 399},
#     {'day': 12, 'description': 'Поездка на такси', 'amount': 700},
#     {'day': 13, 'description': 'Заказали ужин с доставкой', 'amount': 1200},
#     {'day': 14, 'description': 'Посетили кафе с друзьями', 'amount': 1500},
#     {'day': 15, 'description': 'Купили спортивную одежду', 'amount': 5000},
#     {'day': 16, 'description': 'Оплатили страхование автомобиля', 'amount': 15000},
#     {'day': 17, 'description': 'Оплатили коммунальные услуги', 'amount': 4500},
#     {'day': 18, 'description': 'Посетили курсы по программированию', 'amount': 20000},
#     {'day': 19, 'description': 'Оплатили услуги стоматолога', 'amount': 7000},
#     {'day': 20, 'description': 'Купили бытовую технику', 'amount': 25000},
#     {'day': 21, 'description': 'Купили подарки друзьям', 'amount': 5000},
#     {'day': 22, 'description': 'Сделали пожертвование в благотворительный фонд', 'amount': 1000},
#     {'day': 23, 'description': 'Купили новую одежду', 'amount': 8000},
#     {'day': 24, 'description': 'Оплатили кредит', 'amount': 10000},
#     {'day': 25, 'description': 'Заказали билеты на концерт', 'amount': 2500},
#     {'day': 26, 'description': 'Посетили ресторан на выходных', 'amount': 4000},
#     {'day': 27, 'description': 'Обновили смартфон', 'amount': 50000},
#     {'day': 28, 'description': 'Сделали ремонт в квартире', 'amount': 100000},
#     {'day': 29, 'description': 'Оплатили курсы английского языка', 'amount': 20000},
#     {'day': 30, 'description': 'Купили велосипед', 'amount': 30000},
#     {'day': 31, 'description': 'Организовали вечеринку', 'amount': 15000},
# ]


# @app.route('/')
# def start_game():
#     """Начинаем игру с нуля"""
#     session['balance'] = START_BALANCE
#     session['day'] = 0
#     return redirect(url_for('game'))


# @app.route('/game')
# def game():
#     """Главный экран игры"""
#     day = session.get('day', 0)
#     balance = session.get('balance', START_BALANCE)
    
#     if day >= len(events):
#         return redirect(url_for('finish'))
    
#     event = events[day]
#     return render_template_string('''
#         <h1>День {{ event['day'] }}</h1>
#         <p>{{ event['description'] }}</p>
#         <p>Цена: {{ event['amount'] }} руб.</p>
#         <p>Ваш текущий баланс: {{ balance }} руб.</p>
#         <a href="{{ url_for('game_action', action='participate') }}">✔️ Участвую</a>
#         <a href="{{ url_for('game_action', action='skip') }}">❌ Не участвую</a>
#     ''', event=event, balance=balance)


# @app.route('/game/<action>')
# def game_action(action):
#     """Обрабатываем действия пользователя (участвует или нет)"""
#     day = session.get('day', 0)
#     balance = session.get('balance', START_BALANCE)
#     event = events[day]
    
#     if action == 'participate':
#         balance -= event['amount']
    
#     session['balance'] = balance
#     session['day'] = day + 1
#     return redirect(url_for('game'))


# @app.route('/finish')
# def finish():
#     """Финальный экран"""
#     balance = session.get('balance', START_BALANCE)
#     return render_template_string('''
#         <h1>Игра завершена!</h1>
#         <p>Ваш итоговый баланс: {{ balance }} руб.</p>
#         <a href="{{ url_for('start_game') }}">Начать сначала</a>
#     ''', balance=balance)


# if __name__ == '__main__':
#     app.run(debug=True)







# import streamlit as st

# # Заголовок приложения
# st.title('Добро пожаловать в мое приложение!')

# # Поля ввода
# name = st.text_input('Ваше имя:')
# age = st.number_input('Ваш возраст:', min_value=1, max_value=120, value=18)

# # Кнопка для отправки
# if st.button('Отправить'):
#     st.success(f'Привет, {name}! Тебе {age} лет.')

# # Начальный баланс и список событий
# START_BALANCE = 200000
# events = [
#     {'day': 1, 'description': 'Купили порошок со скидкой', 'amount': 1399},
#     {'day': 2, 'description': 'Купили новые ботинки', 'amount': 3000},
#     {'day': 3, 'description': 'Заказали еду на дом', 'amount': 1000},
#     {'day': 4, 'description': 'Посетили кинотеатр', 'amount': 800},
#     {'day': 5, 'description': 'Купили продукты на неделю', 'amount': 3500},
#     {'day': 6, 'description': 'Оплатили интернет', 'amount': 500},
#     {'day': 7, 'description': 'Заправили автомобиль', 'amount': 2500},
#     {'day': 8, 'description': 'Посетили салон красоты', 'amount': 2000},
#     {'day': 9, 'description': 'Купили новую книгу', 'amount': 600},
#     {'day': 10, 'description': 'Посетили тренажерный зал', 'amount': 1000},
#     {'day': 11, 'description': 'Оплатили подписку на сервис', 'amount': 399},
#     {'day': 12, 'description': 'Поездка на такси', 'amount': 700},
#     {'day': 13, 'description': 'Заказали ужин с доставкой', 'amount': 1200},
#     {'day': 14, 'description': 'Посетили кафе с друзьями', 'amount': 1500},
#     {'day': 15, 'description': 'Купили спортивную одежду', 'amount': 5000},
#     {'day': 16, 'description': 'Оплатили страхование автомобиля', 'amount': 15000},
#     {'day': 17, 'description': 'Оплатили коммунальные услуги', 'amount': 4500},
#     {'day': 18, 'description': 'Посетили курсы по программированию', 'amount': 20000},
#     {'day': 19, 'description': 'Оплатили услуги стоматолога', 'amount': 7000},
#     {'day': 20, 'description': 'Купили бытовую технику', 'amount': 25000},
#     {'day': 21, 'description': 'Купили подарки друзьям', 'amount': 5000},
#     {'day': 22, 'description': 'Сделали пожертвование в благотворительный фонд', 'amount': 1000},
#     {'day': 23, 'description': 'Купили новую одежду', 'amount': 8000},
#     {'day': 24, 'description': 'Оплатили кредит', 'amount': 10000},
#     {'day': 25, 'description': 'Заказали билеты на концерт', 'amount': 2500},
#     {'day': 26, 'description': 'Посетили ресторан на выходных', 'amount': 4000},
#     {'day': 27, 'description': 'Обновили смартфон', 'amount': 50000},
#     {'day': 28, 'description': 'Сделали ремонт в квартире', 'amount': 100000},
#     {'day': 29, 'description': 'Оплатили курсы английского языка', 'amount': 20000},
#     {'day': 30, 'description': 'Купили велосипед', 'amount': 30000},
#     {'day': 31, 'description': 'Организовали вечеринку', 'amount': 15000},
# ]

# # Логика игры
# if 'balance' not in st.session_state:
#     st.session_state.balance = START_BALANCE
# if 'day' not in st.session_state:
#     st.session_state.day = 0

# if st.session_state.day < len(events):
#     event = events[st.session_state.day]
#     st.write(f"### День {event['day']}: {event['description']}")
#     st.write(f"💰 Цена: {event['amount']} руб.")
#     st.write(f"Ваш текущий баланс: {st.session_state.balance} руб.")

#     participate = st.button('✔️ Участвую')
#     skip = st.button('❌ Не участвую')

#     if participate:
#         st.session_state.balance -= event['amount']
#         st.session_state.day += 1
#         st.experimental_rerun()

#     if skip:
#         st.session_state.day += 1
#         st.experimental_rerun()
# else:
#     st.write("## Игра завершена!")
#     st.write(f"Ваш итоговый баланс: {st.session_state.balance} руб.")
#     if st.button('Начать сначала'):
#         st.session_state.balance = START_BALANCE
#         st.session_state.day = 0
#         st.experimental_rerun()
