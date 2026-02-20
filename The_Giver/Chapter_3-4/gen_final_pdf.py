import fpdf
import os

def create_expert_pdf_no_qr(markdown_file, output_pdf, title):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    
    # Page 1: Worksheet
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='L')
    pdf.ln(5)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split("# SOLUTIONS")
    worksheet_text = parts[0]
    solutions_text = "# SOLUTIONS" + parts[1] if len(parts) > 1 else ""

    pdf.set_font("Helvetica", size=11)
    for line in worksheet_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u2014', "--")
        if not line:
            pdf.ln(2)
            continue
        
        if line.startswith("## "):
            pdf.ln(4)
            pdf.set_font("Helvetica", 'B', 12)
            pdf.set_fill_color(240, 240, 240)
            text = line.replace("## ", "")
            pdf.cell(0, 8, f" {text}", ln=True, fill=True)
            pdf.set_font("Helvetica", size=11)
            pdf.ln(2)
        elif line.startswith("---"):
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(2)
        else:
            pdf.multi_cell(0, 6, line)

    # Page 2: SOLUTIONS (Always separate)
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Solutions: " + title, ln=True)
    pdf.ln(5)
    pdf.set_font("Helvetica", size=11)
    
    for line in solutions_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u2014', "--")
        if not line: pdf.ln(2); continue
        if line.startswith("#") or line.startswith("## "):
            pdf.set_font("Helvetica", 'B', 12)
            pdf.multi_cell(0, 7, line.replace("## ", ""))
            pdf.set_font("Helvetica", size=11)
        else:
            pdf.multi_cell(0, 6, line)

    pdf.output(output_pdf)

title = "The Giver - Chapters 3 & 4 (Worksheet)"
create_expert_pdf_no_qr("teaching-materials/The_Giver/Chapter_3-4/worksheet_ch3_4_final.md", "teaching-materials/The_Giver/Chapter_3-4/The_Giver_Ch3_4_Final.pdf", title)
