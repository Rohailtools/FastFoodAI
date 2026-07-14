from pathlib import Path

env_path = Path(".env")

groq_key = input("Enter Groq API Key: ").strip()

if not groq_key:
    print("❌ Groq key empty hai")
    exit()

if not env_path.exists():
    print("❌ .env file nahi mili")
    exit()

content = env_path.read_text()

lines = content.splitlines()

updated = False

new_lines = []

for line in lines:
    if line.startswith("GROQ_API_KEY="):
        new_lines.append(f"GROQ_API_KEY={groq_key}")
        updated = True
    else:
        new_lines.append(line)

if not updated:
    new_lines.append(f"GROQ_API_KEY={groq_key}")

env_path.write_text("\n".join(new_lines))

print("✅ Groq API key updated")
