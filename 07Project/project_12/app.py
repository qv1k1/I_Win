import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 📁 Название файла для хранения данных
FILE_NAME = 'user_data.csv'

# 📤 Загрузка данных из CSV
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=['Имя'])
    df.to_csv(FILE_NAME, index=False)

try:
    df = pd.read_csv(FILE_NAME)
except Exception as e:
    st.error(f'Ошибка загрузки файла: {e}')
    df = pd.DataFrame(columns=['Имя'])

# Инициализация состояния пользователя
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''  # Имя пользователя
if 'balance' not in st.session_state:
    st.session_state['balance'] = 200000  # Начальный баланс
if 'day' not in st.session_state:
    st.session_state['day'] = 0  # Текущий день игры

# ✅ 1️⃣ Экран приветствия и ввода имени
if not st.session_state['user_name']:  
    st.title('👋 Добро пожаловать в наше приложение!')

    name = st.text_input('Введите ваше имя:', key='name_input')

    if st.button('Начать опрос'):
        if name.strip():  # Проверяем, что имя не пустое
            st.session_state['user_name'] = name  # Сохраняем имя в session_state

            # Добавляем имя пользователя в CSV
            new_data = {'Имя': name}
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_csv(FILE_NAME, index=False)

            st.success(f'Привет, {name}! Давайте начнем игру!')

        else:
            st.error('Имя не может быть пустым!')

# ✅ 2️⃣ Логика игры
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

if st.session_state['user_name'] and st.session_state['day'] < len(events):
    event = events[st.session_state['day']]
    st.write(f"### День {event['day']}: {event['description']}")
    st.write(f"💰 Цена: {event['amount']} руб.")
    st.write(f"Ваш текущий баланс: {st.session_state['balance']} руб.")

    # Кнопки для принятия решения
    if st.button('✔️ Участвую', key=f'participate_{st.session_state["day"]}'):
        st.session_state['balance'] -= event['amount']
        st.session_state['day'] += 1

    if st.button('❌ Не участвую', key=f'skip_{st.session_state["day"]}'):
        st.session_state['day'] += 1

else:
    if st.session_state['user_name']:
        st.write("## Игра завершена!")
        st.write(f"Ваш итоговый баланс: {st.session_state['balance']} руб.")
        if st.button('Начать сначала'):
            st.session_state['balance'] = 200000
            st.session_state['day'] = 0
            st.experimental_rerun()

# ✅ 3️⃣ Статистика пользователей и визуализация
st.title('📊 Статистика пользователей')

try:
    df = pd.read_csv(FILE_NAME)
except Exception as e:
    st.error(f'Ошибка загрузки файла: {e}')
    df = pd.DataFrame(columns=['Имя'])

st.write('Всего пользователей:', len(df))
st.write('📂 Данные пользователей из файла user_data.csv:', df)

# 📈 Визуализация графиков
if not df.empty:
    # ✅ 1️⃣ Гистограмма частоты имён
    st.subheader('📊 Гистограмма частоты имён')
    fig, ax = plt.subplots()
    sns.countplot(y='Имя', data=df, order=df['Имя'].value_counts().index, palette='viridis', ax=ax)
    ax.set_title('Частота имен пользователей')
    st.pyplot(fig)
    plt.close(fig)

    # ✅ 2️⃣ Круговая диаграмма
    st.subheader('📈 Круговая диаграмма имён')
    name_counts = df['Имя'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(name_counts, labels=name_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Распределение имен пользователей')
    st.pyplot(fig)
    plt.close(fig)

    # ✅ 3️⃣ Динамика добавления пользователей
    st.subheader('📉 Динамика добавления пользователей')
    df['Время'] = pd.date_range(start='2024-01-01', periods=len(df), freq='D')
    fig, ax = plt.subplots()
    sns.lineplot(x=df['Время'], y=range(len(df)), marker='o', ax=ax)
    ax.set_title('Динамика добавления пользователей')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    plt.close(fig)
else:
    st.warning('Данных для отображения графиков пока нет.')




# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os

# # 📁 Название файла для хранения данных
# FILE_NAME = 'user_data.csv'

# # Если файла не существует — создаём его
# if not os.path.exists(FILE_NAME):
#     df = pd.DataFrame(columns=['Имя'])  # Создаём пустую таблицу с колонкой "Имя"
#     df.to_csv(FILE_NAME, index=False)  # Сохраняем файл

# # 📤 Загрузка данных из CSV
# try:
#     df = pd.read_csv(FILE_NAME)
# except Exception as e:
#     st.error(f'Ошибка загрузки файла: {e}')
#     df = pd.DataFrame(columns=['Имя'])

# # ✅ Используем session_state, чтобы хранить имя пользователя
# if 'user_name' not in st.session_state:
#     st.session_state['user_name'] = ''  # Имя пользователя по умолчанию пустое

# # 📌 Приветствие и ввод имени
# if not st.session_state['user_name']:  # Если имя пользователя не введено, показываем приветствие
#     st.title('👋 Добро пожаловать в наш опрос!')
#     st.write('Введите своё имя, чтобы начать.')

#     name = st.text_input('Введите ваше имя:', key='name_input')

#     if st.button('Начать опрос'):
#         if name.strip():  # Проверяем, что имя не пустое
#             st.session_state['user_name'] = name  # Сохраняем имя в session_state
#             new_data = {'Имя': name}
            
#             try:
#                 df = pd.read_csv(FILE_NAME)  # Чтение существующего файла
#             except Exception as e:
#                 st.error(f'Ошибка загрузки файла: {e}')
#                 df = pd.DataFrame(columns=['Имя'])
            
#             df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)  # Добавляем новую запись
#             df.to_csv(FILE_NAME, index=False)  # Сохраняем файл
#             st.success(f'Привет, {name}! Давайте начнем опрос!')
#         else:
#             st.error('Имя не может быть пустым!')

# # ✅ После ввода имени показываем первый вопрос
# if st.session_state['user_name']:
#     st.title(f'Привет, {st.session_state["user_name"]}! Давайте начнём опрос 🎉')
    
#     # 🔥 Пример первого вопроса
#     st.subheader('Вопрос 1️⃣: Какой ваш любимый цвет?')
#     color = st.radio(
#         "Выберите один из вариантов:",
#         options=['Красный', 'Зелёный', 'Синий', 'Жёлтый', 'Другой']
#     )

#     if st.button('Далее'):
#         st.write(f'Вы выбрали: {color} 🎉')

# # 📊 Статистика пользователей
# st.title('📊 Статистика пользователей')
# try:
#     df = pd.read_csv(FILE_NAME)  # Чтение обновлённых данных
# except Exception as e:
#     st.error(f'Ошибка загрузки файла: {e}')
#     df = pd.DataFrame(columns=['Имя'])

# st.write('Всего пользователей:', len(df))  # Показываем общее количество пользователей
# st.write('📂 Данные пользователей из файла user_data.csv:', df)  # Показываем содержимое файла

# # 📈 Визуализация графиков
# st.title('Визуализация данных')

# if df.empty:
#     st.warning('Данных для отображения графиков пока нет. Добавьте хотя бы одного пользователя.')
# else:
#     # ✅ 1️⃣ Гистограмма частоты имён
#     st.subheader('📊 Гистограмма частоты имён')
#     fig, ax = plt.subplots()
#     sns.countplot(y='Имя', data=df, order=df['Имя'].value_counts().index, palette='viridis', ax=ax)
#     ax.set_title('Частота имен пользователей')
#     ax.set_xlabel('Количество')
#     st.pyplot(fig)
#     plt.close(fig)

#     # ✅ 2️⃣ Круговая диаграмма
#     st.subheader('📈 Круговая диаграмма имён')
#     name_counts = df['Имя'].value_counts()
#     fig, ax = plt.subplots()
#     ax.pie(name_counts, labels=name_counts.index, autopct='%1.1f%%', startangle=90)
#     ax.set_title('Распределение имен пользователей')
#     st.pyplot(fig)
#     plt.close(fig)

#     # ✅ 3️⃣ График числа пользователей с течением времени (фиктивный)
#     st.subheader('📉 Динамика добавления пользователей')
#     df['Время'] = pd.date_range(start='2024-01-01', periods=len(df), freq='D')
#     fig, ax = plt.subplots()
#     sns.lineplot(x='Время', y=range(len(df)), data=df, marker='o', ax=ax)
#     ax.set_title('Динамика добавления пользователей')
#     plt.xticks(rotation=45)
#     st.pyplot(fig)
#     plt.close(fig)



# import streamlit as st


# # Заголовок приложения
# st.title('Добро пожаловать в мое приложение!')

# # Поля ввода
# name = st.text_input('Ваше имя:')


# # Кнопка для отправки
# if st.button('Отправить'):
#     st.success(f'Привет, {name}!')

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

# # Инициализация состояния
# if 'balance' not in st.session_state:
#     st.session_state.balance = START_BALANCE
# if 'day' not in st.session_state:
#     st.session_state.day = 0

# if st.session_state.day < len(events):
#     event = events[st.session_state.day]
#     st.write(f"### День {event['day']}: {event['description']}")
#     st.write(f"💰 Цена: {event['amount']} руб.")
#     st.write(f"Ваш текущий баланс: {st.session_state.balance} руб.")

#     # Кнопки для принятия решения
#     if st.button('✔️ Участвую', key='participate'):
#         st.session_state.balance -= event['amount']
#         st.session_state.day += 1

#     if st.button('❌ Не участвую', key='skip'):
#         st.session_state.day += 1

#     # st.experimental_rerun()  # Можно убрать этот вызов
# else:
#     st.write("## Игра завершена!")
#     st.write(f"Ваш итоговый баланс: {st.session_state.balance} руб.")
#     if st.button('Начать сначала'):
#         st.session_state.balance = START_BALANCE
#         st.session_state.day = 0
#         # st.experimental_rerun()  # Этот метод тоже можно убрать


