from pathlib import Path

files = {
    "app/api/__init__.py": '"""API Package"""\n',
    "app/db/__init__.py": '"""Database Package"""\n',
    "app/services/__init__.py": '"""Services Package"""\n',
    "app/models/__init__.py": '"""Models Package"""\n',
    "app/schemas/__init__.py": '"""Schemas Package"""\n',
    "app/whatsapp/__init__.py": '"""WhatsApp Package"""\n',
    "app/ai/__init__.py": '"""AI Package"""\n',
    "app/dashboard/__init__.py": '"""Dashboard Package"""\n',
    "app/utils/__init__.py": '"""Utils Package"""\n',
}

for path, content in files.items():
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(content, encoding="utf-8")

print("✅ Package initialization files created successfully.")
