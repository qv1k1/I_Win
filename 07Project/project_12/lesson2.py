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
        {'day': 1, 'description': 'Сломалась стиральная машина. Нужно срочно купить новую. Стоимость – 12000 рублей.', 'amount': 12000, 'mandatory': True},
        {'day': 2, 'description': 'Посетите концерт вашего любимого артиста. Билеты заканчиваются!', 'amount': 4500},
        {'day': 3, 'description': 'Закажите вкуснейшую пиццу в честь ленивого вечера с бесплатной доставкой.', 'amount': 1200},
        {'day': 4, 'description': 'Оплата коммунальных услуг за месяц.', 'amount': 5000, 'mandatory': True},
        {'day': 5, 'description': 'Успейте купить стильный и удобный диван со скидкой 20%!', 'amount': 30000},
        {'day': 6, 'description': 'Захватывающая премьера в кинотеатре. Смотрите первыми!', 'amount': 7000},
        {'day': 7, 'description': 'Оплатите страхование автомобиля. Это обязательное требование для продления.', 'amount': 15000, 'mandatory': True},
        {'day': 8, 'description': 'Начните заниматься в зале – пробное занятие фитнеса за 1500 рублей.', 'amount': 1500},
        {'day': 9, 'description': 'Подарите радость другу! Купите шикарный подарок на его день рождения.', 'amount': 3000},
        {'day': 10, 'description': 'Не упустите возможность – запишитесь на курсы с 50% скидкой.', 'amount': 2000},
        {'day': 11, 'description': 'Сломался кондиционер? Срочный ремонт сегодня сэкономит 30%.', 'amount': 12000},
        {'day': 12, 'description': 'Последний день для погашения кредита без штрафных санкций.', 'amount': 20000, 'mandatory': True},
        {'day': 13, 'description': 'Украсьте свой день – купите роскошный букет любимых цветов.', 'amount': 1000},
        {'day': 14, 'description': 'Позаботьтесь о здоровье: лечение зубов со скидкой на первый прием.', 'amount': 8000},
        {'day': 15, 'description': 'Уютный вечер с друзьями: вкусный кофе и десерт в новой кофейне.', 'amount': 2000},
        {'day': 16, 'description': 'Обновите рабочее пространство: новый эргономичный офисный стул.', 'amount': 15000},
        {'day': 17, 'description': 'В квартире прорвало трубу. Срочный ремонт уже выполнен.', 'amount': 4500, 'mandatory': True},
        {'day': 18, 'description': 'Начните заниматься йогой: приобретите лучший коврик по акции.', 'amount': 5000},
        {'day': 19, 'description': 'Поддержите благотворительный фонд и помогите детям.', 'amount': 1500},
        {'day': 20, 'description': 'Купите красивый и удобный обеденный стол со скидкой 15%.', 'amount': 25000},
        {'day': 21, 'description': 'Шаг в будущее: оплатите продвинутый курс по программированию.', 'amount': 25000},
        {'day': 22, 'description': 'Наслаждайтесь любимыми фильмами – месячная подписка на кинотеатр.', 'amount': 1000},
        {'day': 23, 'description': 'Устройте приятный ужин в ресторане. Вкусная еда и уютная атмосфера.', 'amount': 4000},
        {'day': 24, 'description': 'Ваша квартплата за месяц. Без нее не обойтись.', 'amount': 10000, 'mandatory': True},
        {'day': 25, 'description': 'Уникальная акция! Новый смартфон с отличной камерой.', 'amount': 60000},
        {'day': 26, 'description': 'Приятный вечер: билеты на новый фильм и попкорн для компании.', 'amount': 1200},
        {'day': 27, 'description': 'Купите современный холодильник, который экономит электроэнергию.', 'amount': 50000},
        {'day': 28, 'description': 'Продлите страхование вашей квартиры. Это важно для защиты имущества.', 'amount': 15000, 'mandatory': True},
        {'day': 29, 'description': 'Сделайте приятный заказ: купите коробку свежих экзотических фруктов.', 'amount': 3000},
        {'day': 30, 'description': 'Спланируйте поездку мечты! Купите билет в Париж.', 'amount': 20000},
        {'day': 31, 'description': 'Отметьте важное событие в кругу семьи – закажите праздничный ужин.', 'amount': 15000},
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
                st.success("✅ Данные успешно отправлены!")
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