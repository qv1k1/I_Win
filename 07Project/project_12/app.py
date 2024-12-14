import streamlit as st
import requests

# 🟢 Вставьте сюда URL из вашего Google Apps Script
WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbx_m-8lsZCBR4MsQ9EgmEYkfoWXkRw59EjWhwQfkdIjCYnsK7gnoHHlAGjUlwaqW-2w/exec'

# ✅ Логика приложения
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''  

if 'balance' not in st.session_state:
    st.session_state['balance'] = 200000  

if 'day' not in st.session_state:
    st.session_state['day'] = 0  

if not st.session_state['user_name']:  
    st.title('👋 Добро пожаловать в наше приложение!')
    name = st.text_input('Введите ваше имя:', key='name_input')

    if st.button('Начать опрос'):
        if name.strip():  
            st.session_state['user_name'] = name
            st.success(f'Привет, {name}! Давайте начнем игру!')
        else:
            st.error('Имя не может быть пустым!')

else:
    st.title(f'Привет, {st.session_state["user_name"]}!')

    # Список всех возможных событий
    events = [
        {'day': 1, 'description': 'Купили порошок со скидкой', 'amount': 1399},
        {'day': 2, 'description': 'Купили новые ботинки', 'amount': 3000},
        {'day': 3, 'description': 'Заказали еду на дом', 'amount': 1000},
        {'day': 12, 'description': 'Оплата кредита', 'amount': 15000, 'mandatory': True},
        {'day': 17, 'description': 'Оплата коммунальных услуг', 'amount': 4500, 'mandatory': True},
        {'day': 25, 'description': 'Оплата подписки на сервис', 'amount': 1000, 'mandatory': True},
        {'day': 29, 'description': 'Оплата курсов английского языка', 'amount': 20000, 'mandatory': True},
        {'day': 4, 'description': 'Посетили кинотеатр', 'amount': 800},
        {'day': 5, 'description': 'Купили продукты на неделю', 'amount': 3500},
        {'day': 6, 'description': 'Оплатили интернет', 'amount': 500},
        {'day': 7, 'description': 'Заправили автомобиль', 'amount': 2500},
        {'day': 8, 'description': 'Посетили салон красоты', 'amount': 2000},
        {'day': 9, 'description': 'Купили новую книгу', 'amount': 600},
        {'day': 10, 'description': 'Посетили тренажерный зал', 'amount': 1000},
        {'day': 11, 'description': 'Оплатили подписку на сервис', 'amount': 399},
        {'day': 13, 'description': 'Заказали ужин с доставкой', 'amount': 1200},
        {'day': 14, 'description': 'Посетили кафе с друзьями', 'amount': 1500},
        {'day': 15, 'description': 'Купили спортивную одежду', 'amount': 5000},
        {'day': 16, 'description': 'Оплатили страхование автомобиля', 'amount': 15000},
        {'day': 18, 'description': 'Посетили курсы по программированию', 'amount': 20000},
        {'day': 19, 'description': 'Оплатили услуги стоматолога', 'amount': 7000},
        {'day': 20, 'description': 'Купили бытовую технику', 'amount': 25000},
        {'day': 21, 'description': 'Купили подарки друзьям', 'amount': 5000},
        {'day': 22, 'description': 'Сделали пожертвование в благотворительный фонд', 'amount': 1000},
        {'day': 23, 'description': 'Купили новую одежду', 'amount': 8000},
        {'day': 24, 'description': 'Оплатили кредит', 'amount': 10000},
        {'day': 26, 'description': 'Посетили ресторан на выходных', 'amount': 4000},
        {'day': 27, 'description': 'Обновили смартфон', 'amount': 50000},
        {'day': 28, 'description': 'Сделали ремонт в квартире', 'amount': 100000},
        {'day': 30, 'description': 'Купили велосипед', 'amount': 30000},
        {'day': 31, 'description': 'Организовали вечеринку', 'amount': 15000},
    ]

    if st.session_state['day'] < len(events):
        event = events[st.session_state['day']]
        st.write(f"### День {event['day']}: {event['description']}")
        st.write(f"💰 Цена: {event['amount']} руб.")
        st.write(f"Ваш текущий баланс: {st.session_state['balance']} руб.")
        
        if event.get('mandatory', False):
            st.warning('Это обязательное списание, отказаться нельзя.')
            if st.button('Понятно'):
                st.session_state['balance'] -= event['amount']
                st.session_state['day'] += 1
        else:
            if st.button('✔️ Участвую'):
                st.session_state['balance'] -= event['amount']
                st.session_state['day'] += 1

            if st.button('❌ Не участвую'):
                st.session_state['day'] += 1

    else:
        st.write("## Игра завершена!")
        st.write(f"Ваш итоговый баланс: {st.session_state['balance']} руб.")

        # 🟢 Отправляем данные в Google Apps Script
        new_data = {
            'user_name': st.session_state['user_name'], 
            'day': st.session_state['day'], 
            'balance': st.session_state['balance']
        }
        
        try:
            response = requests.post(WEB_APP_URL, json=new_data)
            if response.status_code == 200:
                st.success("✅ Данные успешно отправлены в Google Sheets!")
            else:
                st.error(f'Ошибка отправки данных: {response.status_code}')
        except Exception as e:
            st.error(f'Ошибка: {e}')

        if st.button('Начать сначала'):
            st.session_state['balance'] = 200000
            st.session_state['day'] = 0
            st.session_state['user_name'] = ''  
            st.experimental_rerun()




# import streamlit as st
# import requests

# # 🟢 Вставьте сюда URL из вашего Google Apps Script
# WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbx_m-8lsZCBR4MsQ9EgmEYkfoWXkRw59EjWhwQfkdIjCYnsK7gnoHHlAGjUlwaqW-2w/exec'

# # ✅ Логика приложения
# if 'user_name' not in st.session_state:
#     st.session_state['user_name'] = ''  

# if 'balance' not in st.session_state:
#     st.session_state['balance'] = 200000  

# if 'day' not in st.session_state:
#     st.session_state['day'] = 0  

# if not st.session_state['user_name']:  
#     st.title('👋 Добро пожаловать в наше приложение!')
#     name = st.text_input('Введите ваше имя:', key='name_input')

#     if st.button('Начать опрос'):
#         if name.strip():  
#             st.session_state['user_name'] = name
#             st.success(f'Привет, {name}! Давайте начнем игру!')
#         else:
#             st.error('Имя не может быть пустым!')

# else:
#     st.title(f'Привет, {st.session_state["user_name"]}!')

#     events = [
#         {'day': 1, 'description': 'Купили порошок со скидкой', 'amount': 1399},
#         {'day': 2, 'description': 'Купили новые ботинки', 'amount': 3000},
#         {'day': 3, 'description': 'Заказали еду на дом', 'amount': 1000},
#         {'day': 4, 'description': 'Посетили кинотеатр', 'amount': 800},
#         {'day': 5, 'description': 'Купили продукты на неделю', 'amount': 3500},
#         {'day': 6, 'description': 'Оплатили интернет', 'amount': 500},
#         {'day': 7, 'description': 'Заправили автомобиль', 'amount': 2500},
#         {'day': 8, 'description': 'Посетили салон красоты', 'amount': 2000},
#         {'day': 9, 'description': 'Купили новую книгу', 'amount': 600},
#         {'day': 10, 'description': 'Посетили тренажерный зал', 'amount': 1000},
#         {'day': 11, 'description': 'Оплатили подписку на сервис', 'amount': 399},
#         {'day': 12, 'description': 'Поездка на такси', 'amount': 700},
#         {'day': 13, 'description': 'Заказали ужин с доставкой', 'amount': 1200},
#         {'day': 14, 'description': 'Посетили кафе с друзьями', 'amount': 1500},
#         {'day': 15, 'description': 'Купили спортивную одежду', 'amount': 5000},
#         {'day': 16, 'description': 'Оплатили страхование автомобиля', 'amount': 15000},
#         {'day': 17, 'description': 'Оплатили коммунальные услуги', 'amount': 4500},
#         {'day': 18, 'description': 'Посетили курсы по программированию', 'amount': 20000},
#         {'day': 19, 'description': 'Оплатили услуги стоматолога', 'amount': 7000},
#         {'day': 20, 'description': 'Купили бытовую технику', 'amount': 25000},
#         {'day': 21, 'description': 'Купили подарки друзьям', 'amount': 5000},
#         {'day': 22, 'description': 'Сделали пожертвование в благотворительный фонд', 'amount': 1000},
#         {'day': 23, 'description': 'Купили новую одежду', 'amount': 8000},
#         {'day': 24, 'description': 'Оплатили кредит', 'amount': 10000},
#         {'day': 25, 'description': 'Заказали билеты на концерт', 'amount': 2500},
#         {'day': 26, 'description': 'Посетили ресторан на выходных', 'amount': 4000},
#         {'day': 27, 'description': 'Обновили смартфон', 'amount': 50000},
#         {'day': 28, 'description': 'Сделали ремонт в квартире', 'amount': 100000},
#         {'day': 29, 'description': 'Оплатили курсы английского языка', 'amount': 20000},
#         {'day': 30, 'description': 'Купили велосипед', 'amount': 30000},
#         {'day': 31, 'description': 'Организовали вечеринку', 'amount': 15000},
#     ]

#     if st.session_state['day'] < len(events):
#         event = events[st.session_state['day']]
#         st.write(f"### День {event['day']}: {event['description']}")
#         st.write(f"💰 Цена: {event['amount']} руб.")
#         st.write(f"Ваш текущий баланс: {st.session_state['balance']} руб.")

#         if st.button('✔️ Участвую'):
#             st.session_state['balance'] -= event['amount']
#             st.session_state['day'] += 1

#         if st.button('❌ Не участвую'):
#             st.session_state['day'] += 1

#     else:
#         st.write("## Игра завершена!")
#         st.write(f"Ваш итоговый баланс: {st.session_state['balance']} руб.")

#         # 🟢 Отправляем данные в Google Apps Script
#         new_data = {
#             'user_name': st.session_state['user_name'], 
#             'day': st.session_state['day'], 
#             'balance': st.session_state['balance']
#         }
        
#         try:
#             response = requests.post(WEB_APP_URL, json=new_data)
#             if response.status_code == 200:
#                 st.success("✅ Данные успешно отправлены в Google Sheets!")
#             else:
#                 st.error(f'Ошибка отправки данных: {response.status_code}')
#         except Exception as e:
#             st.error(f'Ошибка: {e}')

#         if st.button('Начать сначала'):
#             st.session_state['balance'] = 200000
#             st.session_state['day'] = 0
#             st.session_state['user_name'] = ''  
#             st.experimental_rerun()




# import streamlit as st
# import pandas as pd
# import gspread
# from google.oauth2.service_account import Credentials

# # 📁 Название файла и листа Google Sheets
# SPREADSHEET_NAME = 'user_data'
# WORKSHEET_NAME = 'Лист1'

# # 🔑 Аутентификация через Streamlit Secrets
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
# client = gspread.authorize(creds)

# # Открываем Google таблицу
# try:
#     sheet = client.open(SPREADSHEET_NAME).worksheet(WORKSHEET_NAME)
# except Exception as e:
#     st.error(f'Ошибка при подключении к Google Sheets: {e}')


# # ✅ Логика приложения
# if 'user_name' not in st.session_state:
#     st.session_state['user_name'] = ''  

# if 'balance' not in st.session_state:
#     st.session_state['balance'] = 200000  

# if 'day' not in st.session_state:
#     st.session_state['day'] = 0  

# if not st.session_state['user_name']:  
#     st.title('👋 Добро пожаловать в наше приложение!')
#     name = st.text_input('Введите ваше имя:', key='name_input')

#     if st.button('Начать опрос'):
#         if name.strip():  
#             st.session_state['user_name'] = name
#             st.success(f'Привет, {name}! Давайте начнем игру!')
#         else:
#             st.error('Имя не может быть пустым!')

# else:
#     st.title(f'Привет, {st.session_state["user_name"]}!')
#     events = [
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

#     if st.session_state['day'] < len(events):
#         event = events[st.session_state['day']]
#         st.write(f"### День {event['day']}: {event['description']}")
#         st.write(f"💰 Цена: {event['amount']} руб.")
#         st.write(f"Ваш текущий баланс: {st.session_state['balance']} руб.")

#         if st.button('✔️ Участвую'):
#             st.session_state['balance'] -= event['amount']
#             st.session_state['day'] += 1

#         if st.button('❌ Не участвую'):
#             st.session_state['day'] += 1

#     else:
#         st.write("## Игра завершена!")
#         st.write(f"Ваш итоговый баланс: {st.session_state['balance']} руб.")

#         # Добавляем данные в Google таблицу
#         new_data = [st.session_state['user_name'], st.session_state['day'], st.session_state['balance']]
#         try:
#             sheet.append_row(new_data)
#             st.success("✅ Данные успешно сохранены в Google таблицу!")
#         except Exception as e:
#             st.error(f'Ошибка записи в Google Sheets: {e}')

#         if st.button('Начать сначала'):
#             st.session_state['balance'] = 200000
#             st.session_state['day'] = 0
#             st.session_state['user_name'] = ''  
#             st.experimental_rerun()


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os

# # 📁 Название файла для хранения данных
# FILE_NAME = 'user_data.csv'

# # 🔍 Проверяем, существует ли файл
# if not os.path.exists(FILE_NAME):
#     df = pd.DataFrame(columns=['Имя', 'День', 'Баланс'])
#     df.to_csv(FILE_NAME, index=False)

# try:
#     df = pd.read_csv(FILE_NAME)
# except Exception as e:
#     st.error(f'Ошибка загрузки файла: {e}')
#     df = pd.DataFrame(columns=['Имя', 'День', 'Баланс'])

# # ✅ Инициализация session_state (для управления состоянием пользователя)
# if 'user_name' not in st.session_state:
#     st.session_state['user_name'] = ''  
# if 'balance' not in st.session_state:
#     st.session_state['balance'] = 200000  
# if 'day' not in st.session_state:
#     st.session_state['day'] = 0  

# # ✅ 1️⃣ Экран приветствия и ввода имени
# if not st.session_state['user_name']:  
#     st.title('👋 Добро пожаловать в наше приложение!')
#     name = st.text_input('Введите ваше имя:', key='name_input')

#     if st.button('Начать опрос'):
#         if name.strip():  
#             st.session_state['user_name'] = name

#             if name not in df['Имя'].values:
#                 new_data = {'Имя': name, 'День': 0, 'Баланс': 200000}
#                 df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#                 df.to_csv(FILE_NAME, index=False)
#             st.success(f'Привет, {name}! Давайте начнем игру!')
#         else:
#             st.error('Имя не может быть пустым!')

# else:
#     st.title(f'Привет, {st.session_state["user_name"]}!')
#     events = [
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
    
#     if st.session_state['day'] < len(events):
#         event = events[st.session_state['day']]
#         st.write(f"### День {event['day']}: {event['description']}")
#         st.write(f"💰 Цена: {event['amount']} руб.")
#         st.write(f"Ваш текущий баланс: {st.session_state['balance']} руб.")

#         if st.button('✔️ Участвую'):
#             st.session_state['balance'] -= event['amount']
#             st.session_state['day'] += 1

#         if st.button('❌ Не участвую'):
#             st.session_state['day'] += 1

#     else:
#         st.write("## Игра завершена!")
#         st.write(f"Ваш итоговый баланс: {st.session_state['balance']} руб.")

#         new_data = {'Имя': st.session_state['user_name'], 'День': st.session_state['day'], 'Баланс': st.session_state['balance']}
#         df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#         df.to_csv(FILE_NAME, index=False)

#         st.download_button(
#             label="📥 Скачать данные CSV",
#             data=df.to_csv(index=False),
#             file_name="user_data.csv",
#             mime="text/csv",
#         )

#         if st.button('Начать сначала'):
#             st.session_state['balance'] = 200000
#             st.session_state['day'] = 0
#             st.session_state['user_name'] = ''  
#             st.experimental_rerun()



# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os

# # 📁 Название файла для хранения данных
# FILE_NAME = 'user_data.csv'

# # 📤 Загрузка данных из CSV
# if not os.path.exists(FILE_NAME):
#     df = pd.DataFrame(columns=['Имя'])
#     df.to_csv(FILE_NAME, index=False)

# try:
#     df = pd.read_csv(FILE_NAME)
# except Exception as e:
#     st.error(f'Ошибка загрузки файла: {e}')
#     df = pd.DataFrame(columns=['Имя'])

# # ✅ Инициализация session_state (для управления состоянием пользователя)
# if 'user_name' not in st.session_state:
#     st.session_state['user_name'] = ''  # Имя пользователя
# if 'balance' not in st.session_state:
#     st.session_state['balance'] = 200000  # Начальный баланс
# if 'day' not in st.session_state:
#     st.session_state['day'] = 0  # Текущий день игры

# # ✅ 1️⃣ Экран приветствия и ввода имени
# if not st.session_state['user_name']:  # Показываем экран приветствия только если имени нет
#     st.title('👋 Добро пожаловать в наше приложение!')

#     name = st.text_input('Введите ваше имя:', key='name_input')

#     if st.button('Начать опрос'):
#         if name.strip():  # Проверяем, что имя не пустое
#             st.session_state['user_name'] = name  # Сохраняем имя в session_state

#             # Добавляем имя пользователя в CSV
#             new_data = {'Имя': name}
#             df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
#             df.to_csv(FILE_NAME, index=False)

#             st.success(f'Привет, {name}! Давайте начнем игру!')

#         else:
#             st.error('Имя не может быть пустым!')

# # ✅ 2️⃣ Логика игры (если введено имя)
# else:
#     st.title(f'Привет, {st.session_state["user_name"]}!')
    
#     events = [
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

#     if st.session_state['day'] < len(events):  # Если ещё остались события
#         event = events[st.session_state['day']]
#         st.write(f"### День {event['day']}: {event['description']}")
#         st.write(f"💰 Цена: {event['amount']} руб.")
#         st.write(f"Ваш текущий баланс: {st.session_state['balance']} руб.")

#         # Кнопки для принятия решения
#         if st.button('✔️ Участвую', key=f'participate_{st.session_state["day"]}'):
#             st.session_state['balance'] -= event['amount']
#             st.session_state['day'] += 1

#         if st.button('❌ Не участвую', key=f'skip_{st.session_state["day"]}'):
#             st.session_state['day'] += 1

#     else:
#         st.write("## Игра завершена!")
#         st.write(f"Ваш итоговый баланс: {st.session_state['balance']} руб.")
#         if st.button('Начать сначала'):
#             st.session_state['balance'] = 200000
#             st.session_state['day'] = 0
#             st.session_state['user_name'] = ''  # Сбрасываем имя пользователя
#             st.experimental_rerun()