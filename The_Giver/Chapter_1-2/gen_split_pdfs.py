import fpdf
import os

def clean_text(text):
    return text.replace('\u2013', '-').replace('\u2014', '-').replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"').replace('\u201d', '"')

def create_advanced_pdf(markdown_file, output_pdf, title):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    
    # 1. Worksheet Page
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, clean_text(title), ln=True, align='L')
    pdf.ln(5)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split("# Solutions")
    worksheet_text = parts[0]
    
    pdf.set_font("Helvetica", size=11)
    for line in worksheet_text.split('\n'):
        line = clean_text(line.strip())
        if not line:
            pdf.ln(2)
            continue
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

    # 2. Detailed Solutions Page
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, clean_text("Detailed Solutions - " + title), ln=True)
    pdf.ln(5)
    
    if len(parts) > 1:
        solutions_text = parts[1]
        for line in solutions_text.split('\n'):
            line = clean_text(line.strip())
            if not line:
                pdf.ln(2)
                continue
            if line.startswith("## "):
                pdf.ln(2)
                pdf.set_font("Helvetica", 'B', 11)
                pdf.cell(0, 6, line[3:], ln=True)
                pdf.set_font("Helvetica", size=11)
            else:
                pdf.multi_cell(0, 5, line)

    pdf.output(output_pdf)

create_advanced_pdf("teaching-materials/The_Giver/Chapter_1-2/ch1_worksheet.md", 
                    "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_1.pdf", 
                    "The Giver - Chapter 1 (Advanced)")

create_advanced_pdf("teaching-materials/The_Giver/Chapter_1-2/ch2_worksheet.md", 
                    "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_2.pdf", 
                    "The Giver - Chapter 2 (Advanced)")
