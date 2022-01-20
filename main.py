#from posixpath import expanduser
import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_culumn = st.beta_columns(2)
button =  left_column.button('右カラムに文字を表示')
if button:
    right_culumn.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#text = st.text_input('あなたの趣味を教えてください。')
#'あなたの趣味：', (text), 'です。'

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'2コンディション：', (condition)

#if st.checkbox('Show Image'):
    #img = Image.open('hp0.jpg')
    #st.image(img, caption='Kaishi', use_column_width=True)

#option = st.selectbox(
    #'あなたが好きな数字を教えてください',
    #list(range(1,11))
#)
#'あなたの好きな数字は',(option),'です。'