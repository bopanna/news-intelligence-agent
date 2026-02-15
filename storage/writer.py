from datetime import datetime
import os


def save_digest(text):
    os.makedirs("storage", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"storage/digest_{today}.md"

    with open(filename, "w") as f:
        f.write("# Daily News Digest\n\n")
        f.write(text)

    print(f"\nSaved digest to {filename}")
