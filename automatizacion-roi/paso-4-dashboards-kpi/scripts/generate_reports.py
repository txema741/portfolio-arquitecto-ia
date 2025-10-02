import argparse
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_md(df_roi, df_copq, output_file):
    """Genera un informe en Markdown"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 📈 Informe Consolidado ROI y CoPQ\n\n")
        f.write("## ROI (Return on Investment – Retorno de la Inversión)\n")
        f.write(df_roi.to_markdown(index=False))
        f.write("\n\n## CoPQ (Cost of Poor Quality – Coste de la Mala Calidad)\n")
        f.write(df_copq.to_markdown(index=False))

def generate_pdf(df_roi, df_copq, output_file):
    """Genera un informe en PDF"""
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("📈 Informe Consolidado ROI y CoPQ", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph("ROI – Return on Investment (Retorno de la Inversión)", styles["Heading2"]))
    story.append(Paragraph(df_roi.to_string(index=False), styles["Normal"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph("CoPQ – Cost of Poor Quality (Coste de la Mala Calidad)", styles["Heading2"]))
    story.append(Paragraph(df_copq.to_string(index=False), styles["Normal"]))

    doc.build(story)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar reportes ROI y CoPQ")
    parser.add_argument("--roi", required=True, help="CSV de ROI (kpis_por_tarea.csv)")
    parser.add_argument("--copq", required=True, help="CSV de CoPQ (copq_por_error.csv)")
    parser.add_argument("--outdir", required=True, help="Carpeta de salida")
    parser.add_argument("--pdf", action="store_true", help="Generar también PDF")
    args = parser.parse_args()

    df_roi = pd.read_csv(args.roi)
    df_copq = pd.read_csv(args.copq)

    # Exportar CSV consolidado
    final_csv = f"{args.outdir}/final_report.csv"
    df_final = pd.concat([df_roi, df_copq], axis=1)
    df_final.to_csv(final_csv, index=False)

    # Exportar Markdown
    final_md = f"{args.outdir}/final_report.md"
    generate_md(df_roi, df_copq, final_md)

    # Exportar PDF opcional
    if args.pdf:
        final_pdf = f"{args.outdir}/final_report.pdf"
        generate_pdf(df_roi, df_copq, final_pdf)

    print("✅ Reportes generados en", args.outdir)
