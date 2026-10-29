"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return "".join(ch for ch in raw.upper() if ch.isalpha())


def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    allowed = DNA_BASES | {"N"} if allow_n else DNA_BASES
    return bool(seq) and set(seq.upper()) <= allowed


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    if not is_valid_dna(seq):
        raise ValueError(f"invalid DNA sequence: {seq!r}")
    seq = seq.upper()
    return (seq.count("G") + seq.count("C")) / len(seq) * 100


def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    if not is_valid_dna(dna):
        raise ValueError(f"invalid DNA sequence: {dna!r}")
    return dna.upper().replace("T", "U")


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    if not motif:
        raise ValueError("motif must not be empty")
    seq, motif = seq.upper(), motif.upper()
    positions = []
    start = seq.find(motif)
    while start != -1:
        positions.append(start)
        start = seq.find(motif, start + 1)
    return positions
