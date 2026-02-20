import sys
import os
sys.path.append('/data/.openclaw/workspace')
from send_email_with_attachments import send_email

recipient = "tek@biondekgasse.at"
subject = "Arbeitsblatt Unit 8: Clothes & Shopping"
body = """Hallo Daniel,

hier ist das gewünschte Arbeitsblatt zur Unit 8 (Clothes & Shopping).

- QR Code Platzhalter mit TinyURL (oben rechts).
- Vokabelübungen, Lückentext und Analysefragen.
- Ausführliche Lösungen auf Seite 2.

Viele Grüße,
Digit ✍️"""

attachment = "/data/.openclaw/workspace/teaching-materials/english/year-1/Unit8_Clothes_Advanced.pdf"

if os.path.exists(attachment):
    send_email(recipient, subject, body, [attachment])
else:
    print(f"Error: {attachment} not found.")
