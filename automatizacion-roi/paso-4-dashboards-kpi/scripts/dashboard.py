import argparse
import pandas as pd
import plotly.express as px
import streamlit as st

def load_data(csv_file: str):
    return pd.read_csv(csv_file)

def streamlit_dashboard(df: pd.DataFrame):
    st.title("📊 Dashboard ROI y CoPQ")
    st.markdown("Visualización de KPIs generados en el Paso 3")

    # ROI
    if "ROI" in df.columns:
        st.subheader("ROI por Tarea")
        fig_roi = px.bar(df, x=df.index, y="ROI", title="Evolución del ROI")
        st.plotly_chart(fig_roi)

    # Payback
    if "Payback" in df.columns:
        st.subheader("Payback")
        fig_payback = px.line(df, x=df.index, y="Payback", title="Payback en meses")
        st.plotly_chart(fig_payback)

    # CoPQ
    if "CoPQ_Estimado(EUR)" in df.columns:
        st.subheader("Coste de la Mala Calidad (CoPQ)")
        fig_copq = px.pie(df, names="Tipo_Error", values="CoPQ_Estimado(EUR)", title="Distribución de CoPQ")
        st.plotly_chart(fig_copq)

def export_html(df: pd.DataFrame, output_file: str):
    fig = px.bar(df, x=df.index, y=df.columns[1], title="Vista rápida de KPIs")
    fig.write_html(output_file)
    print(f"✅ Dashboard exportado a {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dashboard KPI ROI/CoPQ")
    parser.add_argument("--input", type=str, required=True, help="CSV de KPIs")
    parser.add_argument("--export", type=str, help="Ruta de salida para exportar en HTML")
    args = parser.parse_args()

    df = load_data(args.input)

    if args.export:
        export_html(df, args.export)
    else:
        streamlit_dashboard(df)
