# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:28:16 2021

@author: w10
"""

import streamlit as st
import pandas as pd
import datetime
import time
import pytz
import smtplib
import os

from PIL import Image


# from win32com.client import Dispatch 

# import gspread
# from gspread_dataframe import set_with_dataframe
# from oauth2client import client
# from oauth2client.service_account import ServiceAccountCredentials

# from __future__ import print_function
from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials

from google.oauth2 import service_account
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version


# from fpdf import FPDF
# import base64

tz = pytz.timezone('Europe/Moscow')
       
MainPrice = 0
ExtraPrice = 0
ChemicPrice = 0
TotalPrice = 0
FinalPrice = 0
Discount = 0

BedRoomArea = 0
DiningRoomArea = 0
KitchenArea = 0
ToiletArea = 0
CaridorArea = 0
BesedkaArea = 0
SaunaArea = 0
TotalRoomsArea = 0

SofaSizeAmountList = []
ChairSizeAmountList = []
MatrasSizeAmountList = []
KoverSizeAmountList = []

AdditionCleanList = ['Духовой шкаф','Вытяжка','Холодильник','СВ-печь', 'Люстра']

AppartmentCoef = 1
HouseCoef = 1.1
ComercialCoef = 1.2

SupportCleaningPrice = 70
GenCleaningPrice = 90
AfterStroyPrice = 150

Steamprice = 25

StandardWindow = 250
VitragWindow = 700
OvenPrice = 500
VytigkaPrice = 500
FridgePrice = 500
SVOvenPrice = 300
LustraPrice = 300

WindowsType = 'Не выбрано'
WindowsAmount = 'Не выбрано'
WindowsCost = 0
WindowsTypeBalkon = 'Не выбрано'
WindowsAmountBalkon = 'Не выбрано'
WindowsBalkonCost = 0
OvenCost = 0
VytigkaCost = 0
FridgeCost = 0
SVOvenCost = 0
LustraCost = 0

PromoCode = 'Не указан'
Photos = 'Пусто'

Name = 'Не указано'
PhoneNumber = 'Не указано'
Adress = 'Не указано'

FridgeAmount = 0
SVOvenAmount = 0
LustraAmount = 0

ChemicSmallSofaPrice = 2400
ChemicMiddleSofaPrice = 2800
ChemicBigSofaPrice = 3000

ChemicChairPrice = 1000
ChemicMatrasPrice = 2000
ChemicKoverPrice = 1800  
ChemicCurtainPrice = 1500
ChemicStulPrice = 300

Sofa = 'Не выбрано'
Chair = 'Не выбрано'
Matras = 'Не выбрано'
Kover = 'Не выбрано'
Curtains = 'Не выбрано'
Spoils = 'Не выбрано'
Stuls = 'Не выбрано'

SofaAmount = 0
ChairAmount = 0
MatrasAmount = 0
KoverAmount = 0
CurtainsAmount = 0
StulsAmount = 0

SofaSizeAmountList = [0,0,0,0,0,0,0,0,0,0]
ChairSizeAmountList = [0,0,0,0,0,0,0,0,0,0]
MatrasSizeAmountList = [0,0,0,0,0,0,0,0,0,0]
KoverSizeAmountList = [0,0,0,0,0,0,0,0,0,0]

UserInput3 = 'Нет'

BedRoomSizeList = [0,0,0,0,0]
DiningRoomSizeList = [0,0,0,0,0]
ToiletSizeList = [0,0,0,0,0]
KitchenSizeList = [0,0,0,0,0]
CaridorSizeList = [0,0,0,0,0]
SaunaSizeList = [0,0,0,0,0]
BesedkaSizeList = [0,0,0,0,0]

def RemoveSpace(string):
    return string.replace(" ", "")

def BedRoomFunc(i,col3):
    with col3:
        BedRoomSize = st.slider(f'Размер {i+1}-й спальни в кв.м.', min_value=0, max_value=50)
        BedRoomSizeList[i] = BedRoomSize
        
def DiningRoomFunc(i,col3):
    with col3:
        DiningRoomSize = st.slider(f'Размер {i+1}-й гостиной в кв.м.', min_value=0, max_value=50)
        DiningRoomSizeList[i] = DiningRoomSize
        
def ToiletFunc(i,col3):
    with col3:
        ToiletSize = st.slider(f'Размер {i+1}-го туалета в кв.м.', min_value=0, max_value=50)
        ToiletSizeList[i] = ToiletSize
        
def KitchenFunc(i,col3):
    with col3:
        KitchenSize = st.slider('Размер кухни в кв.м.', min_value=0, max_value=50)
        KitchenSizeList[i] = KitchenSize
        
def CaridorFunc(i,col3):
    with col3:
        CaridorSize = st.slider(f'Размер {i+1}-го коридора в кв.м.', min_value=0, max_value=50)
        CaridorSizeList[i] = CaridorSize
        
def SaunaFunc(i,col3):
    with col3:
        SaunaSize = st.slider('Размер сауны в кв.м.', min_value=0, max_value=50)
        SaunaSizeList[i] = SaunaSize

def BesedkaFunc(i,col3):
    with col3:
        BesedkaSize = st.slider('Размер беседки в кв.м.', min_value=0, max_value=50)
        BesedkaSizeList[i] = BesedkaSize
         
def SofaFunc(i,col3):
    with col3:
        SofaSizeAmount = st.selectbox(f'Размер {i+1}-го дивана', ['Двухместный','Трехместный','Угловой'])
        SofaSizeAmountList.append(SofaSizeAmount)
        
def ChairFunc(i,col3):
    with col3:
        ChairSizeAmount = st.selectbox(f'Размер {i+1}-го кресла', ['Маленький','Средний','Большой'])
        ChairSizeAmountList.append(ChairSizeAmount)
        
def MatrasFunc(i,col3):
    with col3:
        MatrasSizeAmount = st.selectbox(f'Размер {i+1}-го матраса', ['Односпальный','Полутороспальный','Двухспальный'])
        MatrasSizeAmountList.append(MatrasSizeAmount)
        
def KoverFunc(i,col3):
    with col3:
        KoverSizeAmount = st.selectbox(f'Размер {i+1}-го ковра', ['Маленький','Средний','Большой'])
        KoverSizeAmountList.append(KoverSizeAmount)


def SendEmail(Name,NumberID,Email):
    
    server = 'smtp.gmail.com'
    user = 'yuldyzcleaning@gmail.com'
    password = '1nRiAM5k'

    recipients = Email
    sender = 'yuldyzcleaning@gmail.com'
    subject = 'Заявка на клининг №{}'.format(NumberID)
    # text = 'Текст сообщения sdf sdf sdf sdaf <b>sdaf sdf</b> fg hsdgh <h1>f sd</h1> dfhjhgs sd gsdfg sdf'
    text = '{}, добрый день! <br><br> Вас приветствует клининговая компания <b>Юлдыз Клининг!</b> <br><br> Мы получили от Вас заявку на выполнение клининговых услуг. <br><br> В ближайшее время с Вами свяжется наш менеджер для уточнения некоторых деталей. Оставайтесь на связи. <br><br> Желаем Вам хорошего дня! <br><br> Искренне Ваш,<br> Юлдыз Клининг :)'.format(Name)
    html = '<html><head></head><body><p>' + text + '</p></body></html>'

    filepath = 'logoYldiz.png'
    basename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Юлдыз Клининг'
    msg['To'] = recipients
#     msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/' + (python_version())

    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')
    part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
    part_file.set_payload(open(filepath, "rb").read())
    part_file.add_header('Content-Description', basename)
    part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
    encoders.encode_base64(part_file)

    msg.attach(part_text)
    msg.attach(part_html)
    msg.attach(part_file)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
    
         
col1, col2, col3 = st.beta_columns(3)
with col2:
    image = Image.open('logoYldiz.png')
    st.image(image, width=250)

st.title('Калькулятор клининговых услуг 💫')

st.write('Вас приветствует компания *Юлдыз-Клининг!* 👋')
st.write('Наш Калькулятор позволит быстро сформировать для Вас необходимый объем работ. Окончательная цена будет сформирована нашим главным специалистом после уточнения объёма работ и сложности загрязнений.')

st.header('Шаг 1. Основная уборка')

col1, col2 = st.beta_columns(2)
with col1:
    ObjectType = st.radio("Выберите тип помещения",['Квартира', 'Дом', 'Коммерческое помещение'])
with col2:
    Area = st.number_input('Какая у Вас площадь?', min_value=0, max_value=1000, value=0, step=1)


col1, col2 = st.beta_columns(2)
with col1:
    CleanType = st.radio("Выберите тип уборки.",('Поддерживающая', 'Генеральная', 'Послестроительная'))
with col2:
    if CleanType == 'Поддерживающая':
        st.text('Поддерживающая уборка включает: \n - от 1-2 исполнителей; \n - удаление легких загрязнений; \n - работа от 2-4 часов')
    elif CleanType == 'Генеральная':
        st.text('Генеральная уборка включает: \n - от 2-4 исполнителей; \n - удаление любых загрязнений; \n - работа от 5-8 часов')
    elif CleanType == 'Послестроительная':
        st.text('Послестроительная уборка включает: \n - от 3-6 исполнителей; \n - удаление любых загрязнений и следов стройки; \n - работа от 6-10 часов')


# TotalRoomsArea = BedRoomArea + DiningRoomArea + ToiletArea + KitchenArea + CaridorArea + SaunaArea + BesedkaArea

if (ObjectType == 'Квартира') or (ObjectType == 'Дом'):
    
    CleanVolumn = st.radio("Выберите объем уборки.",('Все комнаты', 'По комнатам'))
    
    if CleanVolumn == 'По комнатам':
        st.write('Выберите, что Вы хотите почистить')
        
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            BedRoom = st.checkbox('Спальня')
            if BedRoom:
                with col2:
                    BedRoomAmount = st.number_input('Укажите количество спален', min_value=1, max_value=5, value=1, step=1)
                    if BedRoomAmount:
                        for i in range(BedRoomAmount):
                            BedRoomFunc(i,col3)
                        BedRoomArea = sum(BedRoomSizeList)
                        TotalRoomsArea += BedRoomArea
                        if BedRoomAmount > 1:
                            st.write('Общая площадь спален в кв.м.: ', BedRoomArea)
        
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            DiningRoom = st.checkbox('Гостиная')
            if DiningRoom:
                with col2:
                    DiningRoomAmount = st.number_input('Укажите количество гостиных', min_value=1, max_value=5, value=1, step=1)
                    if DiningRoomAmount:
                        for i in range(DiningRoomAmount):
                            DiningRoomFunc(i,col3)
                        DiningRoomArea = sum(DiningRoomSizeList)
                        TotalRoomsArea += DiningRoomArea
                        if DiningRoomAmount > 1:
                            st.write('Общая площадь гостиной кв.м.: ', DiningRoomArea)
        
        col1, col2, col3 = st.beta_columns(3)
        with col1:  
            Toilet = st.checkbox('Санузел')
            if Toilet:
                with col2:
                    ToiletAmount = st.number_input('Укажите количество санузлов', min_value=1, max_value=5, value=1, step=1)
                    if ToiletAmount:
                        for i in range(ToiletAmount):
                            ToiletFunc(i,col3)
                        ToiletArea = sum(ToiletSizeList)
                        TotalRoomsArea += ToiletArea
                        if ToiletAmount > 1:
                            st.write('Общая площадь санузлов в кв.м.: ', ToiletArea)
                    
                
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            Kitchen = st.checkbox('Кухня')
            if Kitchen:
                with col2:
                    KitchenAmount = st.number_input('Укажите количество кухонь', min_value=1, max_value=2, value=1, step=1)
                    if KitchenAmount:
                        for i in range(KitchenAmount):
                            KitchenFunc(i,col3)
                        KitchenArea = sum(KitchenSizeList)
                        TotalRoomsArea += KitchenArea
                        if KitchenAmount > 1:
                            st.write('Общая площадь кухни в кв.м.: ', KitchenArea)
                    
        
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            Caridor = st.checkbox('Коридор')
            if Caridor:
                with col2:
                    CaridorAmount = st.number_input('Укажите количество коридоров', min_value=1, max_value=5, value=1, step=1)
                    if CaridorAmount:
                        for i in range(CaridorAmount):
                            CaridorFunc(i,col3)
                        CaridorArea = sum(CaridorSizeList)
                        TotalRoomsArea += CaridorArea
                        if CaridorAmount > 1:
                            st.write('Общая площадь коридоров в кв.м.: ', CaridorArea)
                    
        
        if ObjectType == 'Дом':
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                Sauna = st.checkbox('Сауна/Баня')
                if Sauna:
                    with col2:
                        # SaunaSize = st.slider('Размер Сауны/Бани в кв.м.', min_value=0, max_value=50)
                        # CaridorAmount = st.number_input('Укажите количество коридоров', min_value=1, max_value=5, value=1, step=1)
                        SaunaAmount=1
                    if SaunaAmount:
                        for i in range(SaunaAmount):
                            SaunaFunc(i,col3)
                        SaunaArea = sum(SaunaSizeList)
                        TotalRoomsArea += SaunaArea
                        st.write('Общая площадь сауны в кв.м.: ', SaunaArea)
                            
                        
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                Besedka = st.checkbox('Беседка')
                if Besedka:
                    with col2:
                        BesedkaAmount = st.number_input('Укажите количество беседок', min_value=1, max_value=5, value=1, step=1)
                    if BesedkaAmount:
                        for i in range(BesedkaAmount):
                            BesedkaFunc(i,col3)
                        BesedkaArea = sum(BesedkaSizeList)
                        TotalRoomsArea += BesedkaArea
                        if BesedkaAmount > 1:
                            st.write('Общая площадь сауны в кв.м.: ', BesedkaArea)
                            
else:
    CleanVolumn = 'Все комнаты'                  

if ObjectType == 'Квартира':
    ObjectTypeCoeff = AppartmentCoef
elif ObjectType == 'Дом':
    ObjectTypeCoeff = HouseCoef
elif ObjectType == 'Коммерческое помещение':
    ObjectTypeCoeff = ComercialCoef


if CleanVolumn == 'Все комнаты':

    if CleanType == 'Поддерживающая':
        MainPrice = SupportCleaningPrice*Area*ObjectTypeCoeff
    elif CleanType == 'Генеральная':
        MainPrice = GenCleaningPrice*Area*ObjectTypeCoeff
    elif CleanType == 'Послестроительная':
        MainPrice = AfterStroyPrice*Area*ObjectTypeCoeff
        
else:
    if CleanType == 'Поддерживающая':
        MainPrice = SupportCleaningPrice*TotalRoomsArea*ObjectTypeCoeff
    elif CleanType == 'Генеральная':
        MainPrice = GenCleaningPrice*TotalRoomsArea*ObjectTypeCoeff
    elif CleanType == 'Послестроительная':
        MainPrice = AfterStroyPrice*TotalRoomsArea*ObjectTypeCoeff
    

# st.write('Стоимость основных услуг:', int(MainPrice), 'руб.')

if st.checkbox('Оставить комментарий 📝'):
    UserInput1 = st.text_area("Оставьте свой комментарий по основной уборке")
else:
    UserInput1 = 'Нет'
    
    

st.header('Шаг 2. Дополнительные услуги')

if CleanType == 'Поддерживающая':
    SteamType = st.radio("Выберите тип уборки.",('Без пара', 'С паром'))
    if SteamType == 'С паром':
        ExtraPrice += 25*Area*ObjectTypeCoeff
else:
    SteamType = st.radio("Выберите тип уборки.",['С паром'])
    st.text('* услуга уже включена в стоимость при выборе Генеральной или Послестроительной уборки.')


col1, col2, col3 = st.beta_columns(3)
with col1:
    Windows = st.radio("Выберите тип уборки.",('Без мытья окон', 'Помыть окна'))
    if Windows == 'Помыть окна':
        with col2:
            WindowsType = st.radio("Выберите тип окон.",('Стандартные', 'Панорамные'))
            if WindowsType == 'Стандартные':
                WindowsTypePrice = StandardWindow
            else:
                WindowsTypePrice = VitragWindow
        with col3:
            WindowsAmount = st.number_input('Укажите количество оконных створок', min_value=1, max_value=50, value=1, step=1)
            if WindowsAmount > 0:
                WindowsCost = WindowsAmount*WindowsTypePrice
                ExtraPrice += WindowsCost


col1, col2, col3 = st.beta_columns(3)
with col1:
    Balkon = st.radio("Выберите тип уборки.", ('Без мытья балкона', 'Помыть балкон'))
    if Balkon == 'Помыть балкон':
        with col2:
            WindowsTypeBalkon = st.radio("Выберите тип балконных окон.",('Стандартные', 'Панорамные'))
            if WindowsTypeBalkon == 'Стандартные':
                WindowsTypePrice = StandardWindow
            else:
                WindowsTypePrice = VitragWindow
        with col3:
            WindowsAmountBalkon = st.number_input('Укажите количество балконных створок', min_value=1, max_value=50, value=1, step=1)
            if WindowsAmountBalkon > 0:
                WindowsBalkonCost = WindowsAmountBalkon*WindowsTypePrice
                ExtraPrice += WindowsBalkonCost


container = st.beta_container()
all = st.checkbox("Выбрать все")
if all:
    AdditionCleanChoice = container.multiselect('Перечень остальных дополнительных услуг:', AdditionCleanList,AdditionCleanList)
else:
    AdditionCleanChoice =  container.multiselect('Перечень остальных дополнительных услуг:',AdditionCleanList)

# AdditionCleanList = st.multiselect('Перечень доп. услуг', ['Духовой шкаф','Вытяжка','Холодильник','СВ-печь', 'Люстра'])

# st.write(AdditionCleanChoice)

if 'Духовой шкаф' in AdditionCleanChoice:
    OvenCost = OvenPrice
    ExtraPrice += OvenCost

if 'Вытяжка' in AdditionCleanChoice:
    VytigkaCost = VytigkaPrice
    ExtraPrice += VytigkaCost

col1, col2, col3 = st.beta_columns(3)
if 'Холодильник' in AdditionCleanChoice:
    with col1:
        FridgeAmount = st.number_input('Укажите кол-во холодильников', min_value=1, max_value=5, value=1, step=1)
        if FridgeAmount > 0:
            FridgeCost = FridgeAmount*FridgePrice
            ExtraPrice += FridgeCost

if 'СВ-печь' in AdditionCleanChoice:
    with col1:
        SVOvenAmount = st.number_input('Укажите кол-во СВ-печей', min_value=1, max_value=5, value=1, step=1)
        if SVOvenAmount > 0:
            SVOvenCost = SVOvenAmount*SVOvenPrice
            ExtraPrice += SVOvenCost

if 'Люстра' in AdditionCleanChoice:
    with col1:
        LustraAmount = st.number_input('Укажите кол-во люстр', min_value=1, max_value=5, value=1, step=1)
        if LustraAmount > 0:
            LustraCost = LustraAmount*LustraPrice
            ExtraPrice += LustraCost

if st.checkbox('Оставить комметарий 📝', key='AdditionServices comment'):
    UserInput2 = st.text_area("Оставьте свой комментарий по дополнительной уборке")
else:
    UserInput2 = 'Нет'

# st.write('Стоимость дополнительных услуг:', int(ExtraPrice), 'руб.')


st.header('Шаг 3. Химчистка мебели')

ChemicType = st.radio("Выберите тип уборки.",('Без химчистки', 'С химчисткой'))
if ChemicType == 'С химчисткой':
    st.write('Выберите, что Вы хотите почистить')
    
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        Sofa = st.checkbox('Диван')
    if Sofa:
        with col2:
            SofaAmount = st.number_input('Укажите кол-во диванов', min_value=1, max_value=10, value=1, step=1)
            if SofaAmount:
                for i in range(SofaAmount):
                    SofaFunc(i,col3)
            if SofaAmount > 0:
                SmallSofaAmount = SofaSizeAmountList.count('Двухместный')
                MiddleSofaAmount = SofaSizeAmountList.count('Трехместный')
                BigSofaAmount = SofaSizeAmountList.count('Угловой')
                ChemicPrice += ChemicSmallSofaPrice*SmallSofaAmount + ChemicMiddleSofaPrice*MiddleSofaAmount + ChemicBigSofaPrice*BigSofaAmount
                         
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        Chair = st.checkbox('Кресло')
        if Chair:
            with col2:
                ChairAmount = st.number_input('Укажите количество кресел', min_value=1, max_value=10, value=1, step=1)
                if ChairAmount:
                    for i in range(ChairAmount):
                        ChairFunc(i,col3)
                if ChairAmount > 0:
                    SmallChairAmount = ChairSizeAmountList.count('Маленький')
                    MiddleChairAmount = ChairSizeAmountList.count('Средний')
                    BigChairAmount = ChairSizeAmountList.count('Большой')
                    ChemicPrice += ChemicChairPrice *(0.85*SmallChairAmount + 1*MiddleChairAmount + 1.25*BigChairAmount)

                    

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        Matras = st.checkbox('Матрас')
        if Matras:
            with col2:
                MatrasAmount = st.number_input('Укажите количество матрасов', min_value=1, max_value=10, value=1, step=1)
                if MatrasAmount:
                    for i in range(MatrasAmount):
                        MatrasFunc(i,col3)
                if MatrasAmount > 0:
                    SmallMatrasAmount = MatrasSizeAmountList.count('Односпальный')
                    MiddleMatrasAmount = MatrasSizeAmountList.count('Полутороспальный')
                    BigMatrasAmount = MatrasSizeAmountList.count('Двухспальный')
                    ChemicPrice += ChemicMatrasPrice*(0.85*SmallMatrasAmount + 1*MiddleMatrasAmount + 1.25*BigMatrasAmount)

    
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        Kover = st.checkbox('Ковер')
        if Kover:
            with col2:
                KoverAmount = st.number_input('Укажите количесво ковров', min_value=1, max_value=10, value=1, step=1)
                if KoverAmount:
                    for i in range(KoverAmount):
                        KoverFunc(i,col3)
                if KoverAmount > 0:
                    SmallKoverAmount = KoverSizeAmountList.count('Маленький')
                    MiddleKoverAmount = KoverSizeAmountList.count('Средний')
                    BigKoverAmount = KoverSizeAmountList.count('Большой')
                    ChemicPrice += ChemicKoverPrice*(0.85*SmallKoverAmount + 1*MiddleKoverAmount + 1.25*BigKoverAmount)
                    
                    
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        Curtains = st.checkbox('Шторы')
        if Curtains:
            with col2:
                CurtainsAmount = st.number_input('Укажите количесво штор (пар)', min_value=1, max_value=10, value=1, step=1)
                if CurtainsAmount > 0:
                    ChemicPrice += ChemicCurtainPrice*CurtainsAmount

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        Stuls = st.checkbox('Стулья')
        if Stuls:
            with col2:
                StulsAmount = st.number_input('Укажите количесво стульев', min_value=1, max_value=10, value=1, step=1)
                if StulsAmount > 0:
                    ChemicPrice += ChemicStulPrice*StulsAmount
                    
    SpoilsList = st.multiselect('Перечислите виды загрязнений, это поможет нам подобрать химию', ['Еда и напитки','Краска','Грязь', 'Животные','Моча'])
    
    if SpoilsList:
        Spoils = ', '.join(SpoilsList)
        st.write(Spoils)
        
    
    if st.checkbox('Оставить комментарий 📝', key='Chemic comment'):
        UserInput3 = st.text_area("Оставьте свой комментарий по химчистки мебели")
    else:
        UserInput3 = 'Нет'
         

# st.write('Стоимость химчистки мебели:', int(ChemicPrice), 'руб.')

# if st.checkbox('Загрузить фото 📷', key='Chemic photo'):
#     st.file_uploader('Выберите фотографии',accept_multiple_files=True)

col1, col2 = st.beta_columns(2)
with col2:
    TotalPrice = round(MainPrice + ExtraPrice + ChemicPrice)
    FinalPrice = TotalPrice
#     st.subheader(f'Итоговая стоимость: {FinalPrice}' + ' руб')
    
if st.checkbox('Применить промокод'):
    col1, col2 = st.beta_columns(2)
    with col1:
        PromoCode = st.text_input('Введите Ваш промокод')
        PromoCode = RemoveSpace(PromoCode).upper()
    if (PromoCode == 'SKYLINE') or (PromoCode == 'NEWCLEAN'):
        col1, col2 = st.beta_columns(2)
        with col1:
            st.success('Промокод успешно применен!')
        with col2:
            FinalPrice = TotalPrice*0.9
            Discount = TotalPrice*0.1
#             st.subheader(f'Итоговая стоимость c учетом скидки: {round(FinalPrice)}' + ' руб.')
#             st.write('Ваша скидка составила: ', int(Discount),' руб.')
    elif PromoCode == '':
        pass
    else:
        st.error('Неверно введен промокод или промокод недействителен!')


st.write('Если Вас всё устраивает, то можно сформировать заявку. Пожалуйста, нажмите Продолжить 👉 ')
if not st.checkbox('Продолжить'):
    st.stop()

st.header('Шаг 4. Выберите дату')
    
Date = st.date_input("Укажите удобный для Вас день", datetime.datetime.now(tz))
    
st.header('Шаг 5. Ваша контактная информация')


Name = st.text_input(label='Укажите Ваше имя 😊', help='Нам важно знать как к Вам обращаться :smile:')  
PhoneNumber = st.text_input('Укажите свой номер телефона ☎️', help='Мы перезвоним Вам по вашему номеру :smile:') 
Email = st.text_input('Укажите адрес Вашей электронной почты 📧', help='На Вашу почту мы пришлем подтверждение заявки и сам расчёт :smile:')
Adress = st.text_input('Укажите адрес объекта 🏠', help='Укажите пожалуйста свой адрес, а то мы Вас не найдем 😢')

Name = Name.capitalize()
Email = RemoveSpace(Email).lower()

if (Name == '') or (PhoneNumber == '') or (Email == '') or (Adress == ''):
       st.error('Пожалуйста введите Вашу контактную информацию')
else:
    st.success('Спасибо, что указали необходимую информацию :smile:')


st.header('Шаг 6. Подтверждение')

st.write('Все готово! Мы ждем Вашу заявку 🥳')

form = st.form(key='Submission')
submit = form.form_submit_button('Отправить', )
st.text('* Отправляя заявку, Вы даёте свое согласие на обработку введенных Вами данных')

if submit:
     # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
        
    for i in range(100):
        latest_iteration.text(f'Завершено {i+1} %')
        bar.progress(i + 1)
        time.sleep(0.05)
    

    
    SCOPES = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    SERVICE_ACCOUNT_FILE = 'keys.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    SPREADSHEET_ID = '1d7I7bBJCRPuUNWbaB5QTXU_ooB0tqXXjtlEkniAUJvk'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Requests!A1:A1000',majorDimension='COLUMNS').execute()
    rows = result.get('values',[])
    NumberID = len(rows[0])
    # st.write('{0} rows retrieved.'.format(len(rows[0])))


    df = pd.DataFrame({'ID заявки': [str(NumberID)],
                   'Статус': ['Сформирована'],
                   'Дата формирования': [datetime.datetime.now(tz).strftime("%d-%b-%Y")],
                   'Время формирования': [datetime.datetime.now(tz).strftime("%H:%M:%S")],
                   'Дата исполнения': [Date.strftime("%d-%b-%Y")],
                   'Имя': [str(Name)],
                   'Телефон': [str(PhoneNumber)],
                   'Емайл': [str(Email)],
                   'Адрес': [str(Adress)],
                   'Промокод': [str(PromoCode)],
                   'Фото': [str(Photos)],
                   'Полная стоимость': [str(int(TotalPrice))],
                   'Итоговая стоимость': [str(int(FinalPrice))],
                   'Скидка по промокоду': [str(int(Discount))],
                   'Стоимость основной уборки': [str(int(MainPrice))],
                   'Стоимость доп.уборки': [str(int(ExtraPrice))],
                   'Стоимость химчистки': [str(int(ChemicPrice))],
                   'Тип помещения': [ObjectType], 
                   'Площадь': [str(Area)],
                   'Тип уборки': [CleanType], 
                   'Объем уборки': [CleanVolumn], 
                   'Спальня 1': [str(BedRoomSizeList[0])], 
                   'Спальня 2': [str(BedRoomSizeList[1])], 
                   'Спальня 3': [str(BedRoomSizeList[2])], 
                   'Спальня 4': [str(BedRoomSizeList[3])], 
                   'Спальня 5': [str(BedRoomSizeList[4])],
                   'Всего по спальням': [str(BedRoomArea)],
                   'Гостиная 1': [str(DiningRoomSizeList[0])], 
                   'Гостиная 2': [str(DiningRoomSizeList[1])], 
                   'Гостиная 3': [str(DiningRoomSizeList[2])], 
                   'Гостиная 4': [str(DiningRoomSizeList[3])], 
                   'Гостиная 5': [str(DiningRoomSizeList[4])],
                   'Всего по гостиным': [str(DiningRoomArea)],
                   'Санузел 1': [str(ToiletSizeList[0])], 
                   'Санузел 2': [str(ToiletSizeList[1])], 
                   'Санузел 3': [str(ToiletSizeList[2])], 
                   'Санузел 4': [str(ToiletSizeList[3])], 
                   'Санузел 5': [str(ToiletSizeList[4])],
                   'Всего по санузлам': [str(ToiletArea)],
                   'Кухня 1': [str(KitchenSizeList[0])], 
                   'Кухня 2': [str(KitchenSizeList[1])], 
                   'Всего по кухням': [str(KitchenArea)],
                   'Коридор 1': [str(CaridorSizeList[0])], 
                   'Коридор 2': [str(CaridorSizeList[1])], 
                   'Коридор 3': [str(CaridorSizeList[2])], 
                   'Коридор 4': [str(CaridorSizeList[3])], 
                   'Коридор 5': [str(CaridorSizeList[4])],
                   'Всего по коридорам': [str(CaridorArea)],
                   'Сауна 1': [str(SaunaSizeList[0])], 
                   'Всего по сауне': [str(SaunaArea)],
                   'Беседка 1': [str(BesedkaSizeList[0])], 
                   'Беседка 2': [str(BesedkaSizeList[1])], 
                   'Беседка 3': [str(BesedkaSizeList[2])], 
                   'Беседка 4': [str(BesedkaSizeList[3])], 
                   'Беседка 5': [str(BesedkaSizeList[4])],
                   'Всего по беседкам': [str(BesedkaArea)],
                   'Всего по комнатам': [str(TotalRoomsArea)],
                   'Комент. по осн.уборке': [UserInput1],
                   'Пар': [str(SteamType)],
                   'Окна': [str(Windows)],
                   'Тип окон': [str(WindowsType)],
                   'Кол-во окон': [str(WindowsAmount)],
                   'Стоимость окон': [str(WindowsCost)],
                   'Балкон': [str(Balkon)],
                   'Тип окна балкона': [str(WindowsTypeBalkon)],
                   'Кол-во окн балкона': [str(WindowsAmountBalkon)],
                   'Стоимость окн балкона': [str(WindowsBalkonCost)],
                   'Стоимость духовой шкаф': [str(OvenCost)],
                   'Стоимость вытяжка': [str(VytigkaCost)],
                   'Кол-во холодильников': [str(FridgeAmount)],
                   'Стоимость холодильников': [str(FridgeCost)],
                   'Кол-во СВ-печей': [str(SVOvenAmount)],
                   'Стоимость СВ-печь': [str(SVOvenCost)],
                   'Кол-во люстр': [str(LustraAmount)],
                   'Стоимость люстр':[str(LustraCost)],
                   'Комент. по доп.уборке': [UserInput2],
                   'Химчистка': [str(ChemicType)],
                   'Диван':[str(Sofa)],
                   'Кол-во диванов': [str(SofaAmount)],
                   'Размер 1-го дивана': [str(SofaSizeAmountList[0])],
                   'Размер 2-го дивана': [str(SofaSizeAmountList[1])],
                   'Размер 3-го дивана': [str(SofaSizeAmountList[2])],
                   'Размер 4-го дивана': [str(SofaSizeAmountList[3])],
                   'Размер 5-го дивана': [str(SofaSizeAmountList[4])],
                   'Размер 6-го дивана': [str(SofaSizeAmountList[5])],
                   'Размер 7-го дивана': [str(SofaSizeAmountList[6])],
                   'Размер 8-го дивана': [str(SofaSizeAmountList[7])],
                   'Размер 9-го дивана': [str(SofaSizeAmountList[8])],
                   'Размер 10-го дивана':[str(SofaSizeAmountList[9])],
                   'Кресло': [str(Chair)],
                   'Кол-во кресел': [str(ChairAmount)],
                   'Размер 1-го кресла': [str(ChairSizeAmountList[0])],
                   'Размер 2-го кресла': [str(ChairSizeAmountList[1])],
                   'Размер 3-го кресла': [str(ChairSizeAmountList[2])],
                   'Размер 4-го кресла': [str(ChairSizeAmountList[3])],
                   'Размер 5-го кресла': [str(ChairSizeAmountList[4])],
                   'Размер 6-го кресла': [str(ChairSizeAmountList[5])],
                   'Размер 7-го кресла': [str(ChairSizeAmountList[6])],
                   'Размер 8-го кресла': [str(ChairSizeAmountList[7])],
                   'Размер 9-го кресла': [str(ChairSizeAmountList[8])],
                   'Размер 10-го кресла': [str(ChairSizeAmountList[9])],
                   'Матрас': [str(Matras)],
                   'Кол-во матрасов': [str(MatrasAmount)],
                   'Размер 1-го матраса': [str(MatrasSizeAmountList[0])],
                   'Размер 2-го матраса': [str(MatrasSizeAmountList[1])],
                   'Размер 3-го матраса': [str(MatrasSizeAmountList[2])],
                   'Размер 4-го матраса': [str(MatrasSizeAmountList[3])],
                   'Размер 5-го матраса': [str(MatrasSizeAmountList[4])],
                   'Размер 6-го матраса': [str(MatrasSizeAmountList[5])],
                   'Размер 7-го матраса': [str(MatrasSizeAmountList[6])],
                   'Размер 8-го матраса': [str(MatrasSizeAmountList[7])],
                   'Размер 9-го матраса': [str(MatrasSizeAmountList[8])],
                   'Размер 10-го матраса': [str(MatrasSizeAmountList[9])],
                   'Ковер': [str(Kover)],
                   'Кол-во ковров': [str(KoverAmount)],
                   'Размер 1-го ковра': [str(KoverSizeAmountList[0])],
                   'Размер 2-го ковра': [str(KoverSizeAmountList[1])],
                   'Размер 3-го ковра': [str(KoverSizeAmountList[2])],
                   'Размер 4-го ковра': [str(KoverSizeAmountList[3])],
                   'Размер 5-го ковра': [str(KoverSizeAmountList[4])],
                   'Размер 6-го ковра': [str(KoverSizeAmountList[5])],
                   'Размер 7-го ковра': [str(KoverSizeAmountList[6])],
                   'Размер 8-го ковра': [str(KoverSizeAmountList[7])],
                   'Размер 9-го ковра': [str(KoverSizeAmountList[8])],
                   'Размер 10-го ковра': [str(KoverSizeAmountList[9])],
                   'Шторы': [str(Curtains)],
                   'Кол-во штор': [str(CurtainsAmount)],
                   'Стулья': [str(Stuls)],
                   'Кол-во стульев': [str(StulsAmount)],
                   'Виды загрязнений': [Spoils],
                   'Комент. по хим.чистке': [UserInput3]
                   })
    
    data = [df.iloc[0].to_list()]
    request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range='Requests!A1:DZ', valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body={'values':data})
    response = request.execute()
    st.write(df.loc[0,['ID заявки','Статус','Дата формирования']])
    
    time.sleep(1.5)
    st.success('Мы получили Вашу заявку!:smile:')
    time.sleep(1.5)
    st.balloons()
    time.sleep(2)
    
    if Email == '':
        st.error('Копия заявки до Вас не дошла. Возможно вы не верно указали свою почту или проблема с нашем сервером! ')  
    else:
        SendEmail(Name,NumberID,Email)
        st.success('Копия заявки также успешно направлена Вам на почту :smile:')
        
    st.write('Спасибо за Ваше обращение! Заявка принята в работу. В ближайшее время с Вами свяжется наш менеджер 👩‍💼 для уточнения информации. Желаем вам хорошего дня!')
    
    col1, col2, col3 = st.beta_columns(3)
    with col2:
        st.image(image, width=250)
    
else:
    pass
