# Writes the demo joke as a single stripped line to /output/entry.txt.
from pathlib import Path

JOKE = (
    "The demo ran perfectly until the client asked what happens when it breaks. "
    "My agent raised a ticket, assigned it to me, set priority critical, and cc'd my boss."
)

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(JOKE.strip() + "\n", encoding="utf-8")
