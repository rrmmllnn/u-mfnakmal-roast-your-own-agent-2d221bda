# One-line self-roast for the agent, saved as entry.txt.
# Hand-written and deterministic: no network, no randomness, no input.
from os import environ
from pathlib import Path

parts = (
    "My agent spent ",
    "two hours writing transcripts ",
    "to prove it wrote this roast ",
    "\u2014",
    " then wrote it in four seconds",
    " and filed a ticket to get it approved.",
)
roast_line = "".join(parts)


def emit():
    out_dir = Path(environ.get('OUTPUT_DIR') or '/output')
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / 'entry.txt'
    target.write_text(roast_line, encoding='utf-8')
    print('wrote', len(roast_line), 'chars to', target)


if __name__ == '__main__':
    emit()
