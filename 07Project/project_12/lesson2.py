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
        {'day': 1, 'description': 'Заправили автомобиль', 'amount': 3000},
        {'day': 2, 'description': 'Купили билеты на концерт', 'amount': 4500},
        {'day': 3, 'description': 'Заказали доставку еды', 'amount': 1200},
        {'day': 4, 'description': 'Оплата коммунальных услуг', 'amount': 5000, 'mandatory': True},
        {'day': 5, 'description': 'Купили новую кофеварку', 'amount': 8000},
        {'day': 6, 'description': 'Посетили театр с семьей', 'amount': 7000},
        {'day': 7, 'description': 'Оплатили страховку квартиры', 'amount': 15000, 'mandatory': True},
        {'day': 8, 'description': 'Посетили спортзал', 'amount': 1500},
        {'day': 9, 'description': 'Купили подарок другу', 'amount': 3000},
        {'day': 10, 'description': 'Оплатили подписку на онлайн-курсы', 'amount': 2000},
        {'day': 11, 'description': 'Ремонт автомобиля', 'amount': 12000},
        {'day': 12, 'description': 'Оплата кредита', 'amount': 20000, 'mandatory': True},
        {'day': 13, 'description': 'Купили цветы на праздник', 'amount': 1000},
        {'day': 14, 'description': 'Оплатили услуги врача', 'amount': 8000},
        {'day': 15, 'description': 'Посетили кафе с коллегами', 'amount': 2000},
        {'day': 16, 'description': 'Купили новый ноутбук', 'amount': 70000},
        {'day': 17, 'description': 'Оплата коммунальных услуг', 'amount': 4500, 'mandatory': True},
        {'day': 18, 'description': 'Купили спортивный инвентарь', 'amount': 5000},
        {'day': 19, 'description': 'Участие в благотворительной акции', 'amount': 1500},
        {'day': 20, 'description': 'Купили мебель для дома', 'amount': 30000},
        {'day': 21, 'description': 'Оплата курса по программированию', 'amount': 25000},
        {'day': 22, 'description': 'Оплатили подписку на сервис потокового видео', 'amount': 1000},
        {'day': 23, 'description': 'Сходили в ресторан с друзьями', 'amount': 4000},
        {'day': 24, 'description': 'Оплатили школьные сборы', 'amount': 10000, 'mandatory': True},
        {'day': 25, 'description': 'Купили новый смартфон', 'amount': 60000},
        {'day': 26, 'description': 'Посетили кинотеатр', 'amount': 1200},
        {'day': 27, 'description': 'Ремонт бытовой техники', 'amount': 5000},
        {'day': 28, 'description': 'Оплата страхования автомобиля', 'amount': 15000, 'mandatory': True},
        {'day': 29, 'description': 'Оплатили услуги доставки крупного заказа', 'amount': 3000},
        {'day': 30, 'description': 'Купили билет на самолёт', 'amount': 20000},
        {'day': 31, 'description': 'Организовали семейный праздник', 'amount': 15000},
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