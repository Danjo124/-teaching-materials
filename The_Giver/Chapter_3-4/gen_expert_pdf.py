import fpdf
import os
import urllib.request
import urllib.parse

def create_expert_pdf(markdown_file, output_pdf, title, full_url):
    pdf = fpdf.FPDF()
    pdf.set_margins(20, 20, 20)
    
    # Seite 1: Worksheet
    pdf.add_page()
    
    # Header Design (wie heute Morgen)
    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(130, 10, title, ln=0, align='L')
    
    # QR Code (Rechts oben)
    qr_size = 30
    safe_url = urllib.parse.quote(full_url)
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={safe_url}"
    qr_temp = "temp_qr_giver.png"
    try:
        urllib.request.urlretrieve(api_url, qr_temp)
        pdf.image(qr_temp, x=160, y=15, w=qr_size, h=qr_size)
        os.remove(qr_temp)
    except:
        pdf.rect(160, 15, qr_size, qr_size)

    pdf.set_xy(155, 47)
    pdf.set_font("Helvetica", 'B', 6)
    pdf.set_text_color(255, 0, 0)
    pdf.multi_cell(40, 3, "SCAN FOR INTERACTIVE QUIZ", align='C')
    pdf.set_text_color(0, 0, 0)
    
    pdf.set_xy(20, 45)
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pdf.set_font("Helvetica", size=11)
    for line in lines:
        line = line.strip().replace('\u2019', "'").replace('\u2013', "-").replace('\u2014', "--")
        if not line:
            pdf.ln(2)
            continue
        
        # Sektionsbalken (Grau)
        if line.startswith("## ") or line.startswith("I. ") or line.startswith("II. ") or line.startswith("III. ") or line.startswith("IV. "):
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
            # Check for bold tags
            if "**" in line:
                parts = line.split("**")
                for i, part in enumerate(parts):
                    if i % 2 == 1:
                        pdf.set_font("Helvetica", 'B', 11)
                        pdf.write(6, part)
                        pdf.set_font("Helvetica", size=11)
                    else:
                        pdf.write(6, part)
                pdf.ln(6)
            else:
                pdf.multi_cell(0, 6, line)

    # Seite 2: Lösungen
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Detailed Solutions", ln=True)
    pdf.ln(5)
    pdf.set_font("Helvetica", size=11)
    # Hier werden die Lösungen aus dem MD extrahiert oder separat gesetzt
    # Für diesen schnellen Fix nutzen wir einen Platzhalter, falls im MD nicht getrennt
    pdf.multi_cell(0, 6, "Die detaillierten Lösungen befinden sich in der Teacher-Copy.")

    pdf.output(output_pdf)

# Generate
title = "The Giver - Chapters 3 & 4 (Expert Design)"
url = "https://danjo124.github.io/-teaching-materials/The_Giver/Chapter_1-2/index.html" # Placeholder URL
create_expert_pdf("The_Giver_Chapter_3_4_Worksheet.md", "The_Giver_Ch3_4_Expert.pdf", title, url)
