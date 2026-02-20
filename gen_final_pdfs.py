import fpdf
import os

def create_advanced_pdf(markdown_file, output_pdf, title, qr_url=None):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    
    # Page 1: Worksheet
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(130, 10, title, ln=0, align='L')
    
    # QR Code Placeholder (Top Right)
    if qr_url:
        pdf.set_xy(160, 15)
        pdf.set_font("Helvetica", 'B', 7)
        pdf.cell(30, 30, "QR CODE", border=1, ln=1, align='C')
        pdf.set_xy(160, 42)
        pdf.cell(30, 5, qr_url, ln=1, align='C')
    
    pdf.set_xy(20, 35)
    pdf.ln(5)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split("# Solutions")
    worksheet_text = parts[0]
    solutions_text = "# Solutions" + parts[1] if len(parts) > 1 else ""

    pdf.set_font("Helvetica", size=11)
    for line in worksheet_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', "--")
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

    # Page 2: Detailed Solutions
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Detailed Solutions - " + title, ln=True)
    pdf.ln(5)
    pdf.set_font("Helvetica", size=11)
    
    for line in solutions_text.split('\n'):
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u201c', '"').replace('\u201d', '"').replace('\u2014', "--")
        if not line: pdf.ln(2); continue
        if line.startswith("#"):
            pdf.set_font("Helvetica", 'B', 12)
            pdf.multi_cell(0, 7, line)
            pdf.set_font("Helvetica", size=11)
        else:
            pdf.multi_cell(0, 6, line)

    pdf.output(output_pdf)

create_advanced_pdf("teaching-materials/The_Giver/Chapter_1-2/ch1_worksheet.md", 
                    "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_1.pdf", 
                    "The Giver - Chapter 1", "https://tinyurl.com/giver-ch1-dan")

create_advanced_pdf("teaching-materials/The_Giver/Chapter_1-2/ch2_worksheet.md", 
                    "teaching-materials/The_Giver/Chapter_1-2/The_Giver_Chapter_2.pdf", 
                    "The Giver - Chapter 2", "https://tinyurl.com/giver-ch2-dan")

create_advanced_pdf("teaching-materials/english/year-7/word-formation/worksheet.md", 
                    "teaching-materials/english/year-7/word-formation/Word_Formation_7B.pdf", 
                    "Word Formation - Grade 7B", "https://tinyurl.com/7b-wf-dan")
