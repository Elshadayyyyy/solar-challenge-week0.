import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_summary

st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

st.title("Cross-Country Solar Potential Dashboard")
st.markdown("Compare **GHI**, **DNI**, and **DHI** across Benin, Sierra Leone, and Togo.")

df = load_data()
metrics = ['GHI', 'DNI', 'DHI']


countries = st.sidebar.multiselect("Select countries:", df['Country'].unique(), default=df['Country'].unique())
metric = st.sidebar.selectbox("Select metric:", metrics)


filtered_df = df[df['Country'].isin(countries)]


st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(data=filtered_df, x='Country', y=metric, hue='Country', palette='Set2', legend=False, ax=ax)
st.pyplot(fig)


st.subheader("Summary Statistics")
summary = get_summary(filtered_df)
st.dataframe(summary)


st.subheader("Average GHI by Country")
avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots(figsize=(6,4))
sns.barplot(x=avg_ghi.index, y=avg_ghi.values, hue=avg_ghi.index, palette='viridis', legend=False, ax=ax2)
st.pyplot(fig2)
