import sys
import os

# Import the existing send_email function from the workspace script
sys.path.append('/data/.openclaw/workspace')
from send_email_with_attachments import send_email

recipient = "danieltekula@gmail.com"
subject = "Arbeitsblatt: The Giver - Chapters 1 & 2"
body = """Hallo Daniel,

hier ist das gewünschte Arbeitsblatt zu 'The Giver' (Kapitel 1 & 2) für die 5C.

Inhalt:
- Vocabulary Match
- Fill-in-the-blanks (Summary)
- Open Questions
- Solutions (auf Seite 2)

Der GitHub-Upload in das Repo 'Danjo124/-teaching-materials' wird parallel durchgeführt.

Viele Grüße,
Digit ✍️"""

pdf_path = "/data/.openclaw/workspace/teaching-materials/The_Giver/Chapter_1-2/The_Giver_Ch1-2.pdf"

if os.path.exists(pdf_path):
    send_email(recipient, subject, body, [pdf_path])
else:
    print(f"Error: {pdf_path} not found.")
