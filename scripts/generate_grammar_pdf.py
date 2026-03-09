from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import cm
import sys

def create_worksheet(output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=1, fontSize=20, spaceAfter=10)
    section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], fontSize=14, spaceBefore=8, spaceAfter=5, textColor=colors.HexColor("#2E5984"))
    task_style = ParagraphStyle('TaskStyle', parent=styles['Normal'], fontSize=10, italic=True, spaceAfter=5)
    normal_style = styles['Normal']
    normal_style.fontSize = 10
    normal_style.leading = 12

    elements = []

    # Header: Name and Date
    header_data = [['Name: __________________________', 'Date: __________________________']]
    header_table = Table(header_data, colWidths=[9*cm, 8*cm])
    header_table.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'LEFT'), ('VALIGN', (0,0), (-1,-1), 'TOP'), ('FONTSIZE', (0,0), (-1,-1), 9)]))
    elements.append(header_table)
    elements.append(Spacer(1, 0.4*cm))

    # Title
    elements.append(Paragraph("English Grammar: Questions & Objects", title_style))
    elements.append(Spacer(1, 0.2*cm))

    # Section 1: Question Words
    elements.append(Paragraph("1. Question Words (What / Where / How often)", section_style))
    elements.append(Paragraph("Task: Fill in the correct question word (What, Where or How often).", task_style))
    
    q_sentences = [
        "1. ____________ is your pet's name?",
        "2. ____________ does your dog live?",
        "3. ____________ do you feed your hamster?",
        "4. ____________ is your favorite animal?",
        "5. ____________ do you phone your friends? (Every day!)",
        "6. ____________ does she keep her pony?"
    ]
    for s in q_sentences:
        elements.append(Paragraph(s, normal_style))
        elements.append(Spacer(1, 0.1*cm))

    elements.append(Spacer(1, 0.3*cm))

    # Section 2: Object Pronouns
    elements.append(Paragraph("2. Object Pronouns", section_style))
    elements.append(Paragraph("Task: Replace the underlined words with the correct object pronoun (me, you, him, her, it, us, them).", task_style))
    
    obj_sentences = [
        "1. I like <u>my dog</u>. -> I like __________.",
        "2. We love <u>Mandy</u>. -> We love __________.",
        "3. She carries <u>Tom and me</u> to school. -> She carries __________ to school.",
        "4. Do you like <u>the cat</u>? -> Do you like __________?",
        "5. We don't like <u>the boys</u>. -> We don't like __________.",
        "6. Nice to meet <u>you</u>! -> Nice to meet __________!"
    ]
    for s in obj_sentences:
        elements.append(Paragraph(s, normal_style))
        elements.append(Spacer(1, 0.1*cm))

    elements.append(Spacer(1, 0.3*cm))

    # Section 3: Irregular Plurals
    elements.append(Paragraph("3. Irregular Plurals", section_style))
    elements.append(Paragraph("Task: Write the plural form of the animals.", task_style))
    
    plural_data = [['Singular', 'Plural'], ['one mouse', 'two __________'], ['one pony', 'three __________']]
    plural_table = Table(plural_data, colWidths=[4*cm, 6*cm])
    plural_table.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 1, colors.grey), ('BACKGROUND', (0,0), (-1,0), colors.lightgrey), ('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('FONTSIZE', (0,0), (-1,-1), 10)]))
    elements.append(plural_table)

    elements.append(Spacer(1, 0.4*cm))

    # Section 4: Possessive 's
    elements.append(Paragraph("4. Possessive 's", section_style))
    elements.append(Paragraph("Task: Use the possessive 's to say who the pet belongs to.", task_style))
    
    pos_examples = [
        "1. Mr White / shark -> ____________________________",
        "2. The dog / ball -> ____________________________",
        "3. My friend / pony -> ____________________________",
        "4. The girl / cat -> ____________________________"
    ]
    for s in pos_examples:
        elements.append(Paragraph(s, normal_style))
        elements.append(Spacer(1, 0.1*cm))


    # Build PDF
    doc.build(elements)

if __name__ == "__main__":
    create_worksheet("Grammar_Worksheet_Questions_Objects.pdf")
    print("PDF created successfully.")
