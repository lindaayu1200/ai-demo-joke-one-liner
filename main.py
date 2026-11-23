# Writes the demo joke as a single stripped line to /output/entry.txt.
from pathlib import Path

JOKE = (
    "During the demo the AI agent's code worked perfectly. "
    "So did the code it wrote for the bug report, the rollback plan, "
    "and the apology email it had already sent."
)

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(JOKE.strip() + "\n", encoding="utf-8")
