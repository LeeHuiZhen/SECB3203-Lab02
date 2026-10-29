# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 2
- Student name: Lee Hui Zhen
- Matric no: A24CS0259
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 29 October 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 29 October 2026, 4:10 PM
- Tool: Google (2026). Gemini. Retrieved 29 October 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "How do I remove spaces, digits, and newlines from a string in Python all at once?"
- Output: Suggested filtering characters using a generator expression with .isalpha() to keep only letters, then joining them back together with "".join().
- Verified by: Checked Week 2 lecture slide 14 which uses the exact same "".join(ch for ch in raw.upper() if ch.isalpha()) pattern.
- My change: Implemented clean_sequence using this pattern with raw.upper().
- Used in: src/lab02_sequences.py (clean_sequence).

## Entry 2

- Date: 29 October 2026, 4:18 PM
- Tool: Google (2026). Gemini. Retrieved 29 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "Why does is_valid_dna need to check if seq is empty before checking if it is a subset of ACGT?"
- Output: Explained that an empty set is mathematically a subset of every set, so set('') <= allowed evaluates to True even when the sequence string is empty.
- Verified by: Tested set("") <= set("ACGT") directly in Python terminal to see the True result.
- My change: Added bool(seq) check in is_valid_dna to ensure an empty string returns False.
- Used in: src/lab02_sequences.py (is_valid_dna).

## Entry 3

- Date: 29 October 2026, 4:22 PM
- Tool: Google (2026). Gemini. Retrieved 29 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "In gc_content and transcribe, should a sequence with an N base be accepted or raise ValueError?"
- Output: Explained that unless allow_n is explicitly True, standard DNA consists only of ACGT; because is_valid_dna defaults to allow_n=False, calling if not is_valid_dna(...) will reject N and raise a ValueError to stop ambiguous data.
- Verified by: Checked Week 2 lecture slide 15 and Lab 2 brief Task T2/T3.
- My change: Used if not is_valid_dna(seq): raise ValueError(...) in both gc_content and transcribe.
- Used in: src/lab02_sequences.py (gc_content, transcribe)

## Entry 4

- Date: 29 October 2026, 4:26 PM
- Tool: Google (2026). Gemini. Retrieved 29 October 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "How do I find overlapping motifs like AAAA and AA without missing any?"
- Output: Suggested moving the search pointer forward by start + 1 instead of skipping by len(motif) when calling seq.find.
- Verified by: Tested by hand on AAAA and AA to ensure indices 0, 1, and 2 are returned.
- My change: Implemented the while loop using start = seq.find(motif, start + 1).
- Used in: src/lab02_sequences.py (find_motif).

## Entry 5

- Date: 29 October 2026, 4:38 PM
- Tool: Google (2026). Gemini. Retrieved 29 October 2026 from https://gemini.google.com
- Purpose: tests-plan
- Prompt: "What test cases should I write for find_motif to cover normal, boundary, and invalid inputs?"
- Output: Recommended testing non-overlapping matches, overlapping cases with case insensitivity, and an empty motif raising ValueError.
- Verified by: Checked against Lab 2 brief tasks T4 and T5.
- My change: Implemented test_find_motif_normal, test_find_motif_boundary_overlapping_and_case, and test_find_motif_invalid_empty_motif_raises using pytest.
- Used in: tests/test_lab02_sequences.py.