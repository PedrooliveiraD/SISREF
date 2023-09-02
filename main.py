# pip install streamlit pandas matplotlib seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Dashboard - Student Dataset", page_icon=":books:")
st.sidebar.title("Configurações de Exibição")
show_id = "1378939680"

gsheets_url = 'https://docs.google.com/spreadsheets/d/1Xr6uPNAlT4n9FDuR91JyY2QwFGLGmMICPE5WqjW-s1k/export?format=csv&gid=' + show_id

data = pd.read_csv(gsheets_url, on_bad_lines='skip')


st.title("Quantidade de alunos que não compareceram por Curso")
fig, ax = plt.subplots()
ax = sns.countplot(x="Curso", hue="Compareceu", data=data[data["Compareceu"] == "Não"])

ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(xlabel='Curso', ylabel='Quantidade de Alunos')
st.pyplot(fig)

