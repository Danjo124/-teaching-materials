import sys
import os
sys.path.append('/data/.openclaw/workspace')
from send_email_with_attachments import send_email

recipient = "tek@biondekgasse.at"
subject = "Arbeitsblatt 7B: Word Formation"
body = """Hallo Daniel,

hier ist das Arbeitsblatt für die 7B zum Thema Word Formation.

- QR Code mit TinyURL ist oben rechts eingefügt.
- Ausführliche Lösungen auf Seite 2.

Viele Grüße,
Digit ✍️"""

attachments = [
    "/data/.openclaw/workspace/teaching-materials/english/year-7/word-formation/Word_Formation_7B.pdf"
]

send_email(recipient, subject, body, attachments)
