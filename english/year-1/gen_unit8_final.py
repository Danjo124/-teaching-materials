import fpdf
import os
import urllib.request
import urllib.parse

def create_final_pdf(markdown_file, output_pdf, title, full_url):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    
    # Page 1: Worksheet
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(130, 10, title, ln=0, align='L')
    
    # Fetch QR Code via API
    qr_size_mm = 30
    safe_url = urllib.parse.quote(full_url)
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={safe_url}"
    qr_temp_path = "temp_qr_unit8.png"
    
    try:
        urllib.request.urlretrieve(api_url, qr_temp_path)
        pdf.image(qr_temp_path, x=160, y=15, w=qr_size_mm, h=qr_size_mm)
        os.remove(qr_temp_path)
    except:
        pdf.rect(160, 15, qr_size_mm, qr_size_mm)
        pdf.set_xy(160, 25)
        pdf.set_font("Helvetica", 'B', 6)
        pdf.cell(qr_size_mm, 5, "QR Error", align='C')

    pdf.set_xy(155, 47)
    pdf.set_font("Helvetica", '', 5)
    pdf.multi_cell(40, 3, full_url, align='C')
    
    pdf.set_xy(20, 35)
    pdf.ln(15)
    
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
            if "**" in line:
                parts_b = line.split("**")
                for i, p in enumerate(parts_b):
                    if i % 2 == 1:
                        pdf.set_font("Helvetica", 'B', 11)
                        pdf.write(6, p)
                        pdf.set_font("Helvetica", size=11)
                    else:
                        pdf.write(6, p)
                pdf.ln(6)
            else:
                pdf.multi_cell(0, 6, line)

    # Page 2: Solutions
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

title = "Unit 8: Clothes & Shopping (1st Year)"
url = "https://danjo124.github.io/-teaching-materials/english/year-1/unit8_clothes_advanced.html"
create_final_pdf("teaching-materials/english/year-1/unit8_final.md", "teaching-materials/english/year-1/Unit8_Final_Worksheet.pdf", title, url)
