import streamlit as st
import requests

# 🟢 Вставьте сюда URL из вашего Google Apps Script
WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbxuw_ZL7D7nC7_q-skOGuPp3q6EHlBEaMUQ5Tk4Lt2bjOvxCIk2oJfCUm84CJd6kkL1cg/exec'

# ✅ Логика приложения
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = None  # Устанавливаем начальное значение None


if 'consent_given' not in st.session_state:
    st.session_state['consent_given'] = False  # Флаг для согласия

if 'balance' not in st.session_state:
    st.session_state['balance'] = 200000  

if 'day' not in st.session_state:
    st.session_state['day'] = 0  

# 🟢 Экран приветствия с вводом имени и согласием на обработку данных
if st.session_state['user_name'] is None or not st.session_state['consent_given']:
    st.title("👋 Добро пожаловать в упражнение №2!")
    st.write("""
    **Правила игры:**
    - У вас 31 день!
    - Каждый день это новая ситуация.
    - Вы решаете, как поступить в каждом из дней.
    - Успехов!
    """)

    user_name = st.text_input("Введите ваше имя, чтобы начать игру", key="user_name_input")

    consent = st.checkbox(
        "Нажимая кнопку «Начать», я даю свое согласие на обработку моих персональных данных, в соответствии с Федеральным законом от 27.07.2006 года №152-ФЗ «О персональных данных»",
        value=False,
        key="consent_checkbox"
    )

    if st.button("Начать"):
        if not user_name:
            st.error("Пожалуйста, введите ваше имя!")
        elif not consent:
            st.error("Необходимо дать согласие на обработку персональных данных.")
        else:
            st.session_state['user_name'] = user_name
            st.session_state['consent_given'] = True
            # st.experimental_rerun()
            st.rerun()

else:
    st.title(f'Привет, {st.session_state["user_name"]}!')

    # Список всех возможных событий
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
        {'day': 12, 'description': 'Оплата кредита', 'amount': 15000, 'mandatory': True},
        {'day': 13, 'description': 'Заказали ужин с доставкой', 'amount': 1200},
        {'day': 14, 'description': 'Посетили кафе с друзьями', 'amount': 1500},
        {'day': 15, 'description': 'Купили спортивную одежду', 'amount': 5000},
        {'day': 16, 'description': 'Оплатили страхование автомобиля', 'amount': 15000},
        {'day': 17, 'description': 'Оплата коммунальных услуг', 'amount': 4500, 'mandatory': True},
        {'day': 18, 'description': 'Посетили курсы по программированию', 'amount': 20000},
        {'day': 19, 'description': 'Оплатили услуги стоматолога', 'amount': 7000},
        {'day': 20, 'description': 'Купили бытовую технику', 'amount': 25000},
        {'day': 21, 'description': 'Купили подарки друзьям', 'amount': 5000},
        {'day': 22, 'description': 'Сделали пожертвование в благотворительный фонд', 'amount': 1000},
        {'day': 23, 'description': 'Купили новую одежду', 'amount': 8000},
        {'day': 24, 'description': 'Оплатили кредит', 'amount': 10000},
        {'day': 25, 'description': 'Оплата подписки на сервис', 'amount': 1000, 'mandatory': True},
        {'day': 26, 'description': 'Посетили ресторан на выходных', 'amount': 4000},
        {'day': 27, 'description': 'Обновили смартфон', 'amount': 50000},
        {'day': 28, 'description': 'Сделали ремонт в квартире', 'amount': 100000},
        {'day': 29, 'description': 'Оплата курсов английского языка', 'amount': 20000, 'mandatory': True},
        {'day': 30, 'description': 'Купили велосипед', 'amount': 30000},
        {'day': 31, 'description': 'Организовали вечеринку', 'amount': 15000},
    ]

    if st.session_state['day'] < len(events):
        event = events[st.session_state['day']]
        st.write(f"### День {event['day']}: {event['description']}")
        st.write(f"💰 Цена: {event['amount']} руб.")
        st.write(f"Ваш текущий баланс: {st.session_state['balance']} руб.")

        # Проверяем, обязательный ли это день
        if 'mandatory' in event and event['mandatory'] is True:
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
            # st.experimental_rerun()
            st.rerun()