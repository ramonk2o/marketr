#!/usr/bin/env python3
"""Measure copy against channel limits. Models miscount characters; this does not.

fields FILE  Each line: label | limit | text (limit 0 = just count).
             --wide counts full-width characters (CJK) as 2, as Google Ads does.
             Ad placeholders count as rendered: {KeyWord:default} and other
             {NAME:default} as their default, {COUNTDOWN(...)} as 8.
sms FILE     The whole file is one message: encoding, length, segments, the
             characters that force UCS-2, and a GSM-7 version without them
             (a starting point to rewrite from, not a finished message).
Use - as FILE to read from stdin. Exits 1 when a field is over or empty.
Emoji counts are approximate: platforms count them differently.
"""
import re
import sys
import unicodedata

GSM_BASIC = set(
    "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?"
    "¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"
)
GSM_EXTENDED = set("^{}\\[~]|€\f")  # each costs 2 units
REPLACEMENTS = {
    "“": '"', "”": '"', "„": '"', "‘": "'", "’": "'",
    "–": "-", "—": "-", "…": "...", " ": " ", "ç": "c",
    "•": "-", "`": "'",
}


def read(path):
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8") as f:
        return f.read()


PLACEHOLDER = re.compile(r"\{(?:GLOBAL_)?COUNTDOWN\([^)]*\)\}|\{[^{}:]+:([^{}]*)\}", re.I)


def render(text):
    return PLACEHOLDER.sub(lambda m: m.group(1) if m.group(1) is not None else "x" * 8, text)


def length(text, wide):
    text = unicodedata.normalize("NFC", render(text))
    if not wide:
        return len(text)
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text)


def fields(path, wide):
    failed = False
    for n, line in enumerate(read(path).splitlines(), 1):
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split("|", 2)]
        if len(parts) != 3 or not parts[1].isdigit():
            print(f"line {n}: expected 'label | limit | text'")
            failed = True
            continue
        label, limit, text = parts[0], int(parts[1]), parts[2]
        size = length(text, wide)
        if not text:
            status, failed = "EMPTY", True
        elif not limit:
            status = ""
        elif size <= limit:
            status = f"ok ({limit - size} left)"
        else:
            status, failed = f"OVER by {size - limit}", True
        print(f"{label}: {size}/{limit or '-'} {status}".rstrip())
    return failed


def segments(sizes, single, part):
    # A character never splits across segments (escape pairs, emoji surrogates).
    if sum(sizes) <= single:
        return 1
    count, used = 1, 0
    for size in sizes:
        if used + size > part:
            count, used = count + 1, 0
        used += size
    return count


def sms_stats(text):
    if all(c in GSM_BASIC or c in GSM_EXTENDED for c in text):
        sizes = [2 if c in GSM_EXTENDED else 1 for c in text]
        return "GSM-7", sum(sizes), segments(sizes, 160, 153)
    sizes = [len(c.encode("utf-16-le")) // 2 for c in text]
    return "UCS-2", sum(sizes), segments(sizes, 70, 67)


def to_gsm(text):
    out = []
    for c in text:
        if c in GSM_BASIC or c in GSM_EXTENDED:
            out.append(c)
        elif c in REPLACEMENTS:
            out.append(REPLACEMENTS[c])
        else:
            base = "".join(
                b for b in unicodedata.normalize("NFD", c) if not unicodedata.combining(b)
            )
            out.append(base if base and all(b in GSM_BASIC for b in base) else "")
    return "".join(out)


def sms(path):
    text = unicodedata.normalize("NFC", read(path).replace("\r\n", "\n").rstrip("\n"))
    encoding, units, segments = sms_stats(text)
    print(f"encoding: {encoding}, length: {units}, segments: {segments}")
    if encoding == "UCS-2":
        culprits = sorted({c for c in text if c not in GSM_BASIC and c not in GSM_EXTENDED})
        print("forces UCS-2: " + " ".join(repr(c) for c in culprits))
        alt = to_gsm(text)
        a_enc, a_units, a_segments = sms_stats(alt)
        print(f"GSM-7 version: {a_enc}, length: {a_units}, segments: {a_segments}")
        print(alt)
    return False


def main(argv):
    wide = "--wide" in argv
    args = [a for a in argv if a != "--wide"]
    if len(args) != 2 or args[0] not in ("fields", "sms"):
        print(__doc__)
        return 1
    failed = fields(args[1], wide) if args[0] == "fields" else sms(args[1])
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
