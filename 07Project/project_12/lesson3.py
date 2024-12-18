    
import streamlit as st
import pandas as pd
import requests
import random
import matplotlib.pyplot as plt
import os
import tempfile

# URL вашего веб-приложения (Apps Script URL)
WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbw0CPfgmyqLYLRrbo9SohnVk0vhRBG3_cMsDjJETP-3BKiP9bRHAjk8TAFY5caEdNSs/exec'

# Инициализация сессии
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

if 'decisions' not in st.session_state:
    st.session_state.decisions = []

if 'user_name' not in st.session_state:
    st.session_state.user_name = None

# Ввод имени и согласие
if st.session_state.user_name is None:
    st.title("Добро пожаловать в Финансовую игру!")
    st.write("""
    **Правила игры:**
    - Вам будет предложено несколько финансовых ситуаций.
    - Ваша задача — решить, является ли это "Активом" или "Пассивом".
    - Посмотрите, какой будет ваш финансовый результат в конце!
    """)
    
    user_name = st.text_input("Введите ваше имя, чтобы начать игру", key="user_name_input")
    
    consent = st.checkbox(
        "Нажимая кнопку «Отправить», я даю свое согласие на обработку моих персональных данных, в соответствии с Федеральным законом от 27.07.2006 года №152-ФЗ «О персональных данных», на условиях и для целей, определенных в Согласии на обработку персональных данных *",
        value=False,
        key="consent_checkbox"
    )
    
    if st.button("Начать"):
        if not user_name:
            st.error("Пожалуйста, введите ваше имя!")
        elif not consent:
            st.error("Необходимо дать согласие на обработку персональных данных.")
        else:
            st.session_state.user_name = user_name

else:
    st.title(f"Привет, {st.session_state.user_name}! Начинаем игру 🚀")
    
    situations = [
    # 7 активов
    {'description': 'Купить квартиру и сдавать её в аренду. Первый взнос 200 000 руб, а каждый месяц от аренды можно получать 15 000 руб.', 
     'initial_payment': 200000, 'monthly_cashflow': 15000, 'type': 'Актив'},

    {'description': 'Присоединиться к инвестиционному проекту на ранней стадии. Вложение 100 000 руб с прогнозируемой доходностью 7-12% годовых.', 
     'initial_payment': 100000, 'monthly_cashflow': round(100000 * 0.1 / 12), 'type': 'Актив'},

    {'description': 'Купить акции с дивидендами. Стоимость пакета 50 000 руб. Дивидендная доходность — 10 000 руб в год.', 
     'initial_payment': 50000, 'monthly_cashflow': round(10000 / 12), 'type': 'Актив'},

    {'description': 'Купить коммерческую недвижимость и сдавать её в аренду. Вложение 150 000 руб, ежемесячный доход 18 000 руб.', 
     'initial_payment': 150000, 'monthly_cashflow': 18000, 'type': 'Актив'},

    {'description': 'Инвестировать 80 000 руб в фонд ETF с доходностью 10% в год. Прогнозируемый доход — 8 000 руб ежегодно.', 
     'initial_payment': 80000, 'monthly_cashflow': round(8000 / 12), 'type': 'Актив'},

    {'description': 'Купить гараж за 100 000 руб и сдавать его в аренду. Ежемесячный доход составит 5 000 руб.', 
     'initial_payment': 100000, 'monthly_cashflow': 5000, 'type': 'Актив'},

    {'description': 'Купить долю в прибыльном интернет-магазине за 50 000 руб. Доход в месяц составит 4 000 руб.', 
     'initial_payment': 50000, 'monthly_cashflow': 4000, 'type': 'Актив'},

    # # 10 пассивов (выглядят как заманчивые предложения)
    {'description': 'Ваш идеальный автомобиль! Первый взнос всего 150 000 руб и далее каждый месяц 12 000 руб на погашение кредита.', 
     'initial_payment': 150000, 'monthly_cashflow': -12000, 'type': 'Пассив'},

    {'description': 'Ваши друзья уже купили электросамокат? Присоединяйтесь! Первый взнос 10 000 руб и потом всего 2 000 руб в месяц.', 
     'initial_payment': 10000, 'monthly_cashflow': -2000, 'type': 'Пассив'},

    {'description': 'Стильный ноутбук для работы и учебы. Первый взнос 20 000 руб и потом каждый месяц по 3 000 руб.', 
     'initial_payment': 20000, 'monthly_cashflow': -3000, 'type': 'Пассив'},

    {'description': 'Купить новый диван в рассрочку. Первый взнос 15 000 руб и затем по 1 500 руб в месяц.', 
     'initial_payment': 15000, 'monthly_cashflow': -1500, 'type': 'Пассив'},

    {'description': 'Пора обновить кухню! Новый кухонный гарнитур в рассрочку. Первый взнос 40 000 руб и 2 500 руб ежемесячно.', 
     'initial_payment': 40000, 'monthly_cashflow': -2500, 'type': 'Пассив'},

    {'description': 'Станьте частью модной тусовки! Супер-часы за 30 000 руб, первый взнос 10 000 руб и далее по 2 000 руб в месяц.', 
     'initial_payment': 10000, 'monthly_cashflow': -2000, 'type': 'Пассив'},

    {'description': 'Стильный тренажёр для дома! Первый взнос 20 000 руб и далее по 1 800 руб ежемесячно.', 
     'initial_payment': 20000, 'monthly_cashflow': -1800, 'type': 'Пассив'},

    {'description': 'Купить путёвку на море мечты! Ваша поездка за 70 000 руб, с возможностью оплаты частями по 3 000 руб в месяц.', 
     'initial_payment': 20000, 'monthly_cashflow': -3000, 'type': 'Пассив'},

    {'description': 'Станьте владельцем элитной коллекционной вещи. Первый взнос 50 000 руб и последующие выплаты по 2 500 руб.', 
     'initial_payment': 50000, 'monthly_cashflow': -2500, 'type': 'Пассив'},

    {'description': 'Купить новый iPhone по подписке! Первый взнос 15 000 руб, затем 4 000 руб в месяц.', 
     'initial_payment': 15000, 'monthly_cashflow': -4000, 'type': 'Пассив'},


    # 3 двусмысленные ситуации
    {'description': 'Инвестировать в стартап за 50 000 руб с возможной доходностью от 0 до 20 000 руб ежемесячно.', 
     'initial_payment': 50000, 'monthly_cashflow': random.choice([-5000, 5000, 10000]), 'type': 'Пассив'},

    {'description': 'Участвовать в кооперативе. Взнос 70 000 руб и возможный доход от 5 000 руб.', 
     'initial_payment': 70000, 'monthly_cashflow': 5000, 'type': 'Актив'},

    {'description': 'Станьте владельцем эксклюзивной криптомонеты за 90 000 руб. Будет ли доход? Никто не знает.', 
     'initial_payment': 90000, 'monthly_cashflow': 0, 'type': 'Пассив'}    
    ]
    
    current_index = st.session_state.current_index

    if current_index < len(situations):
        situation = situations[current_index]
        
        st.markdown(f"### 🔄 Вопрос {current_index + 1} из {len(situations)}")
        st.write(situation['description'])
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Инвестировать (Купить)'):
                st.session_state.decisions.append({
                    'Название актива': situation['description'] if situation['type'] == 'Актив' else '',
                    'Сумма актива': situation['initial_payment'] if situation['type'] == 'Актив' else 0,
                    'Ежемесячный денежный поток': situation['monthly_cashflow'],
                    'Название пассива': situation['description'] if situation['type'] == 'Пассив' else '',
                    'Сумма пассива': situation['initial_payment'] if situation['type'] == 'Пассив' else 0
                })
                st.session_state.current_index += 1
                st.rerun()
        
        with col2:
            if st.button('Пропустить (Отказаться)'):
                st.session_state.current_index += 1
                st.rerun()
    
    else:
        st.markdown("## 🏆 Финальный экран")
        
        if len(st.session_state.decisions) == 0:
            st.write("Вы отказались от всех возможностей. Иногда это тоже правильное решение, но в жизни важно не упускать шансы!")
        
        else:
            df = pd.DataFrame(st.session_state.decisions)
            
            if not df.empty:
                df = df[['Название актива', 'Сумма актива', 'Ежемесячный денежный поток', 'Название пассива', 'Сумма пассива']]
                
                df.fillna(0, inplace=True)
                df[['Сумма актива', 'Ежемесячный денежный поток', 'Сумма пассива']] = df[['Сумма актива', 'Ежемесячный денежный поток', 'Сумма пассива']].astype(int)
                
                st.markdown("### 📊 Ваши активы и пассивы")
                st.dataframe(df.style.format(
                    {'Сумма актива': "{:,.0f}", 'Ежемесячный денежный поток': "{:,.0f}", 'Сумма пассива': "{:,.0f}"}
                ))
                
                total_assets = int(df['Сумма актива'].sum())
                total_liabilities = int(df['Сумма пассива'].sum())
                total_cashflow = int(df['Ежемесячный денежный поток'].sum())
                
                st.markdown(f"**Общая стоимость активов:** {total_assets:,.0f} руб")
                st.markdown(f"**Общая стоимость пассивов:** {total_liabilities:,.0f} руб")
                st.markdown(f"**Ежемесячный денежный пото:** {total_cashflow:,.0f} руб/мес")
                
                fig, ax = plt.subplots(figsize=(12, 4))
                ax.axis('off')
                table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
                table.auto_set_font_size(False)
                table.set_fontsize(10)
                table.auto_set_column_width(col=list(range(len(df.columns))))
                
                temp_dir = tempfile.gettempdir()  
                image_path = os.path.join(temp_dir, 'table.png')
                plt.savefig(image_path, bbox_inches='tight', dpi=300)
                plt.close(fig)

                with open(image_path, "rb") as file:
                    st.download_button(label="📥 Скачать таблицу в виде изображения", 
                                    data=file, 
                                    file_name="финансовая_таблица.png", 
                                    mime="image/png")
                    
            # Данные для отправки
            payload = {
                'user_name': st.session_state.user_name,
                'question_responses': df.to_dict(orient='records'),
                'total_assets': total_assets,
                'total_liabilities': total_liabilities,
                'total_cashflow': total_cashflow
            }
            
            if total_cashflow > 0:
                st.success(f"Поздравляем, {st.session_state.user_name}! Вы отлично справились, и ваш итоговый денежный поток составил **{total_cashflow:,.0f} руб/мес**.")
                st.balloons()
                # st.image('gold_medal.png', caption='Золотая медаль!', width=150)
            else:
                st.error(f"{st.session_state.user_name}, ваш итоговый денежный поток составил **{total_cashflow:,.0f} руб/мес**. Попробуйте пересмотреть свои инвестиционные решения.")
    
    
            # Отправка данных
            try:
                response = requests.post(WEB_APP_URL, json=payload)
                
                if response.status_code == 200:
                    st.success("✅ Данные успешно отправлены в Google таблицу!")
                else:
                    st.error(f"❌ Ошибка при отправке данных. Код ошибки: {response.status_code}")
            
            except Exception as e:
                st.error(f"❌ Произошла ошибка при отправке данных: {e}")
        