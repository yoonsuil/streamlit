import streamlit as st 
import pandas as pd  #csv 파일 불러오려면 
import matplotlib as plt


def bmi_range(bmi):
    st.write(f'당신의 체질량지수는 {bmi:.2f}입니다.')
    
    if bmi >=18.5 and bmi<=22.9 :
        st.success('정상입니다.',icon="✅")
    elif bmi <=18.5 :
        st.warning('저체중입니다.', icon="⚠️")
    else:
        st.error('비만입니다.',icon="🚨")
        st.image('sunrise.jpeg',caption='산타고 운동하세요.')
    st.balloons()

selected = st.sidebar.selectbox('목차',("체질량 계산기","gapminder","국가별통계"))

if selected == "체질량 계산기":                                      

    st.title('체질량 지수 계산기')
    st.info('체질량지수는 자신의 몸무게를 키의 제곱으로 나눈 값입니다.')

    height = st.number_input("신장 (cm)",value= 160, step = 3)
    st.write(f"당신의 신장은 : {height} cm입니다.")

    weight = st.number_input("몸무게 (kg)",value= 60, step = 1)
    st.write(f"당신의 몸무게는 : {weight} kg입니다.")


    if st.button("계산하기"):
        bmi=weight/((height/100)**2)
        bmi_range(bmi)
        
if selected =="gapminder":
    st.title('gapminder')
    
    st.write("파일 불러오기")
    data =pd.read_csv("gapminder.csv")
    
    year = st.slider("Select a Year",1952,2007,1952,step=5)
    st.write(f"{year}년도")
    
    data = data[data["year"]== year]
    
    #st.write(data)
    
    #fig, ax = plt.subplots()
    #ax.scatter(data['gdpPercap'], data['LifeExp'], s= data['pop']*0.000002)  #s 는 데이터 사이즈 조정   
    #st.pyplot(fig)
    
    df= data[['gdpPercap','lifeExp']]
    st.scatter_chart(df)
    st.write(df)
    
if selected =="국가별통계":
    st.title("국가별통계")
