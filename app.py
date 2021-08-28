import streamlit as st
import pandas as pd

import datetime
import time
import pytz

from PIL import Image
from googleapiclient.discovery import build
from google.oauth2 import service_account



SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = 'keys.json'
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()



tz = pytz.timezone('Europe/Moscow')

LogoPath =  'logoYldiz.png'

Img_1 = '1.jpg'
Img_2 = '2.jpg'
Img_3 = '3.jpg'
Img_4 = '4.jpg'
Img_5 = '5.jpg'
Img_6 = '6.jpg'
Img_7 = '7.jpg'
Img_8 = '8.png'

col1, col2, col3 = st.beta_columns(3)
with col2:
    image = Image.open(LogoPath)
    st.image(image, width=200)


option_names = ["Шаг 1", "Шаг 2", "Шаг 3", "Шаг 4", "Шаг 5", "Шаг 6"]
    
container_1 = st.empty()
container_2 = st.empty()
container_3 = st.empty()
container_4 = st.empty()
container_5 = st.empty()
container_6 = st.empty()
container_7 = st.empty()
container_8 = st.empty()
container_9 = st.empty()

if 'radio_option' not in st.session_state:
    st.session_state.radio_option = 'Шаг 1'
    
if 'count' not in st.session_state:
    st.session_state.count = 0
    
if 'ObjectType' not in st.session_state:
    st.session_state.ObjectType = str()
    
if 'Area' not in st.session_state:
    st.session_state.Area = str()

if 'CleanType' not in st.session_state:
    st.session_state.CleanType = str()
    
if 'Windows' not in st.session_state:
    st.session_state.Windows = str()
    
if 'Chemic' not in st.session_state:
    st.session_state.Chemic = str()
    
if 'Extra' not in st.session_state:
    st.session_state.Extra = str()

if 'Name' not in st.session_state:
    st.session_state.Name = str()
    
if 'Phone' not in st.session_state:
    st.session_state.Phone = str()
    
if 'Date' not in st.session_state:
    st.session_state.Date = str()

if st.session_state.count <= 3:
    
    col1, col2, col3 = st.beta_columns(3)
    with col2:    
        next = st.button("👉 Далее")
else:
    pass
        
if next:
    st.session_state.count += 1
    if st.session_state["radio_option"] == 'Шаг 1':
        st.session_state.radio_option = 'Шаг 2'
    elif st.session_state["radio_option"] == 'Шаг 2':
        st.session_state.radio_option = 'Шаг 3'
    elif st.session_state["radio_option"] == 'Шаг 3':
        st.session_state.radio_option = 'Шаг 4'
    elif st.session_state["radio_option"] == 'Шаг 4':
        st.session_state.radio_option = 'Шаг 5'
    elif st.session_state["radio_option"] == 'Шаг 5':
        st.session_state.radio_option = 'Шаг 6'
    else:
        st.session_state.radio_option = 'Шаг 1'

# option = st.sidebar.radio("Навигация", option_names , key="radio_option")
# st.session_state
option = st.session_state.radio_option


if option == 'Шаг 1':
    
    container_1.title('Вас приветствует *Юлдыз-Клининг!* 👋')
  
    image = Image.open(Img_5)
    container_2.image(image, width=300)
    
    container_3.write('Для экономии Вашего времени мы предлагаем воспользоваться онлайн заявкой. Чтобы продолжить нажмите *Далее*.')


elif option == 'Шаг 2':
    
    container_1.title('Расскажите нам про Ваш объект :house:')

    image = Image.open(Img_2)
    container_2.image(image, width=300)
    
    col1, col2 = st.beta_columns(2)
    with col1:
        st.session_state.ObjectType = container_3.radio("Выберите тип помещения:",['Квартира', 'Дом', 'Коммерческое помещение'])
    with col2:
        st.session_state.Area = container_4.number_input('Какая у Вас площадь?', min_value=0, max_value=1000, value=0, step=1)
    
    col1, col2 = container_5.beta_columns(2)
    with col1:
         st.session_state.CleanType = container_6.radio("Выберите тип уборки:",('Поддерживающая', 'Генеральная', 'Послестроительная'))

elif option == 'Шаг 3':
    
    container_1.title('Какие у Вас будут еще пожелания?')
    
    image = Image.open(Img_3)
    container_2.image(image, width=300)
    container_3.write('Выберите один или несколько вариантов из дополнительных услуг:')
    
    col1, col2 = st.beta_columns(2)
    with col1:
        st.session_state.Windows = container_4.checkbox('Мойка окн', value = False)
        st.session_state.Chemic = container_5.checkbox('Химчистка мебели', value = False)
        st.session_state.Extra = container_6.checkbox('Помыть что-то еще, например, духовую печь или холодильник...', value = False)

elif option == 'Шаг 4':
    
    container_1.title('Укажите дату и Ваши контакты')
    
    # image = Image.open(Img_7)
    # container_2.image(image, width=300)
    
    col1, col2 = st.beta_columns(2)
    with col1:
        st.session_state.Name = container_3.text_input(label='Укажите Ваше имя 😊', help='Нам важно знать как к Вам обращаться :smile:')  
    with col2:
        st.session_state.Phone = container_4.text_input('Укажите свой номер телефона ☎️', help='Мы перезвоним Вам по вашему номеру :smile:')
        
    st.session_state.Date = container_5.date_input("Выберите удобный для Вас день:", datetime.datetime.now(tz))

    
elif option == 'Шаг 5':
    
    image = Image.open(Img_6)
    container_1.image(image, width=300)
    
    st.balloons()
    time.sleep(1.5)

    container_2.success('Мы получили Вашу заявку!:smile:')
    container_3.success('В ближайщее время с Вами свяжется наш менеджер. Оставайтесь на связи!')
    
    df0 = pd.DataFrame({'Статус': ['Сформирована'],
                        'Дата формирования': [datetime.datetime.now(tz).strftime("%d-%b-%Y")],
                        'Время формирования': [datetime.datetime.now(tz).strftime("%H:%M:%S")],
                        'Дата исполнения': [st.session_state.Date.strftime("%d-%b-%Y")],
                        'Имя': [str(st.session_state.Name)],
                        'Телефон': [str(st.session_state.Phone)],
                        'Тип помещения': [str(st.session_state.ObjectType)], 
                        'Площадь': [str(st.session_state.Area)],
                        'Тип уборки': [str(st.session_state.CleanType)],
                        'Окна': [str(st.session_state.Windows)],
                        'Химчистка': [str(st.session_state.Chemic)],
                        'Дополнительно': [str(st.session_state.Extra)]})
    
    SPREADSHEET_ID = '1a3TiqsFRgeVF0Sw8WYCUPdFfCrgLa5K_dcbkCIVM6j8'
    data = [df0.iloc[0].to_list()]
    request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range='Sheet1!A1:DZ', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={'values':data})
    response = request.execute()
    
    # container_4.write(df0)
    
elif option == 'Шаг 6':
    image = Image.open(Img_8)
    container_1.title('Желаем Вам хорошего дня!')
    container_2.image(image, width=300)
    
