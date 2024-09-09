import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl as op
from streamlit_extras.grid import grid

st.set_page_config(page_title='Robertson Guimarães', page_icon=':bar_icon', layout='wide') 

def Dash():   
    
    #st.write("<h1><Funções Expander, Form e Divides</center><h1>", unsafe_allow_html=True)

    df = pd.read_csv('data.csv')

    st.subheader('Painéis de Recursos Humanos')

    meu_grid = grid(1,3,2,1)

    idade = px.histogram(
        df, 
        'AGE',
        nbins=10,
        title='Distribuição por idade',  
    )
    #st.plotly_chart(idade)

    exp_med = df.groupby('DEPARTAMENT')['EXPERIENCE'].mean().reset_index()
    exp = px.bar(
        exp_med,
        x='DEPARTAMENT',
        y='EXPERIENCE',
        title='Experiência média por departamento',
        labels={'Departamento', 'Experiência', 'Experiência média'},
    )
    #st.plotly_chart(exp)

    satisf_med = df.groupby('GENDER')['JOBSATISFACTION'].mean().reset_index()
    satisf = px.bar(
        satisf_med,
        x="GENDER",
        y="JOBSATISFACTION",
        color="GENDER",
        title="Satisfação média por gênero",
        labels={"GENDER": "Gênero", "JOBSATISFACTION": "Satisfação Média"},
    )
    #st.plotly_chart(satisf)

    horas_trab = df.groupby('DEPARTAMENT')['HOURPERWEEK'].mean().reset_index()
    horas = px.bar(
        horas_trab,
        x='DEPARTAMENT',
        y='HOURPERWEEK',
        color='DEPARTAMENT',
        title='Horas trabalhadas - Média por departamento',
        labels={'DEPARTAMENT':'Departamento', 'HOURPERWEEK': 'Média de horas trabalhadas'},
        )
    #st.plotly_chart(horas)

    idade_salario = px.scatter_3d(
        df,
        x='AGE',
        y='SALARY',
        z='EXPERIENCE',
        color='GENDER',
        title='Idade, experiência e salário por gênero',
        labels={'AGE': 'Idade', 'SALARY': 'Salário', 'GENDER': 'Gênero'},
    )
    #st.plotly_chart(idade_salario)

    salario_exp = px.scatter(
        df,
        x='EXPERIENCE',
        y='SALARY',
        color='GENDER',
        title='Experiência e salário por gênero',
        labels={'EXPERIENCE': 'Experiência', 'SALARY': 'Salário', 'GENDER': 'Gênero'},
    )
    #st.plotly_chart(salario_exp)


    perf_med = df.groupby('DEPARTAMENT')['PERFORMACESCORE'].mean().reset_index()
    perf = px.bar_polar(
        perf_med,
        r='PERFORMACESCORE',
        theta='DEPARTAMENT',
        color='DEPARTAMENT',
        title='Performance média por departamento',
        labels={'PERFORMACESCORE': 'Performance média', 'DEPARTAMENT': 'Departamento'},
    )
    #st.plotly_chart(perf)

    meu_grid.plotly_chart(idade)
    meu_grid.plotly_chart(exp)
    meu_grid.plotly_chart(satisf)
    meu_grid.plotly_chart(horas)
    meu_grid.plotly_chart(idade_salario)
    meu_grid.plotly_chart(perf)
    meu_grid.plotly_chart(salario_exp)



