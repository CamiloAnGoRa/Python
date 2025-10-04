import pandas as pd
import plotly.express as px
import streamlit as st

# --- Cargar datos ---
df = pd.read_csv("clientes_limpios.csv")
df["Ingresos"] = pd.to_numeric(df["Ingresos"], errors="coerce")
df = df.dropna(subset=["Ingresos", "Tipo_Servicio"])

st.title("Ingresos Promedio por Tipo de Servicio")

# --- Gráfico de barras ---
ingresos_prom = df.groupby("Tipo_Servicio")["Ingresos"].mean().reset_index()
fig_bar = px.bar(
    ingresos_prom,
    x="Tipo_Servicio",
    y="Ingresos",
    color="Tipo_Servicio",
    title="Ingresos Promedio por Tipo de Servicio",
    labels={"Ingresos": "Ingreso Promedio", "Tipo_Servicio": "Tipo de Servicio"}
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- Selector de servicio ---
servicio_sel = st.selectbox("Selecciona un servicio para ver la distribución:", df["Tipo_Servicio"].unique())

# --- Boxplot ---
df_filtrado = df[df["Tipo_Servicio"] == servicio_sel]
fig_box = px.box(
    df_filtrado,
    y="Ingresos",
    points="all",
    title=f"Distribución de Ingresos - {servicio_sel}",
    labels={"Ingresos": "Ingresos"}
)
st.plotly_chart(fig_box, use_container_width=True)
