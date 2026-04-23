"""Bengali text utilities:normalization, whitespace cleaning, punctuation helpers."""

import re
import unicodedata

# Sentence ending punctuation in Bengali text.
# Daari (।) is the primary Bengali terminator; ? and ! are shared
# with English but valid in Bengali sentence too.
SENTENCE_TERMINATORS: frozenset[str] = frozenset({"।", "॥", "?", "!"})

# Used for splitting - regex pattern derived from the set above.
SENTENCE_TERMINATOR_PATTERN: str = r"[।॥?!]+"


def normalize_text(text: str) -> str:
    """Normalize Bengali text to Unicode NFC form.

    Converts decomposed sequences (e.g., য +  ় ) into their canonical
    precomposed equivalents (য়). This is the first gate for any Bengali
    Text entering the pipeline - downstream functions assume NFC input.

    Args:
        text: Raw input text, possibly with inconsistent Unicode forms.

    Returns:
        NFC-normalized text where visually identical strings are
        byte equivalent.
    """

    return unicodedata.normalize("NFC", text)


def clean_whitespace(text: str) -> str:
    """Normalize whitespace while preserving paragraph boundaries.

    Collapses multiple spaces and tabs into single space per line,
    strips leading/trailing whitespace from each line.
    Paragraph structure (blank lines between paragraphs) is preserved.

    Args:
        text: text with potentially inconsistent whitespace.

    Returns:
        whitespace-cleaned text with paragraph structure intact.
    """

    lines = text.splitlines()
    cleaned_lines = [" ".join(line.split()) for line in lines]
    return "\n".join(cleaned_lines)


def split_into_sentences(text: str) -> list[str]:
    """Split Bengali text into sentences on Daari (।), ?, !.

    Args:
        text: NFC-normalized, whitespace-cleaned Bengali text.

    Returns:
        list of sentence strings with leading/trailing whitespace
        stripped. Empty strings are excluded from the result.
    """

    parts = re.split(SENTENCE_TERMINATOR_PATTERN, text)
    return [s.strip() for s in parts if s.strip()]
