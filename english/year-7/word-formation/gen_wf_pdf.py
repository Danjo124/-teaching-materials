import fpdf
import os

def clean_text(text):
    return text.replace('\u2013', '-').replace('\u2014', '-').replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')

def create_wf_pdf(ws_md, sol_md, output_pdf, title):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    
    # Page 1: Worksheet
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, clean_text(title), ln=True)
    pdf.ln(5)
    
    pdf.set_font("Helvetica", size=11)
    with open(ws_md, 'r', encoding='utf-8') as f:
        for line in f:
            line = clean_text(line.strip())
            if not line: pdf.ln(2); continue
            if line.startswith("## "):
                pdf.ln(3)
                pdf.set_font("Helvetica", 'B', 12)
                pdf.set_fill_color(240, 240, 240)
                pdf.cell(0, 8, line[3:], ln=True, fill=True)
                pdf.set_font("Helvetica", size=11)
            elif line.startswith("---"):
                pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 170, pdf.get_y())
                pdf.ln(2)
            else:
                pdf.multi_cell(0, 6, line)

    # Page 2: Detailed Solutions
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, clean_text("Detailed Solutions - " + title), ln=True)
    pdf.ln(5)
    
    pdf.set_font("Helvetica", size=10)
    with open(sol_md, 'r', encoding='utf-8') as f:
        for line in f:
            line = clean_text(line.strip())
            if not line: pdf.ln(2); continue
            if line.startswith("## "):
                pdf.ln(2)
                pdf.set_font("Helvetica", 'B', 11)
                pdf.cell(0, 6, line[3:], ln=True)
                pdf.set_font("Helvetica", size=10)
            else:
                pdf.multi_cell(0, 5, line)
                
    pdf.output(output_pdf)

create_wf_pdf("teaching-materials/english/year-7/word-formation/worksheet.md",
              "teaching-materials/english/year-7/word-formation/solutions.md",
              "teaching-materials/english/year-7/word-formation/Word_Formation_7B.pdf",
              "Word Formation Practice - Grade 7B")
