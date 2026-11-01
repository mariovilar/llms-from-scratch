"""A word-level tokenizer built from a regular expression and a fixed vocabulary."""

import re
from collections.abc import Iterable

# This teaching tokenizer uses both markers; GPT-2 uses <|endoftext|> but not <|unk|>.
ENDOFTEXT = "<|endoftext|>"
UNK = "<|unk|>"

_SPLIT_PATTERN = re.compile(r'([,.:;?_!"()\[\]]|--|\s)')
_SPACE_BEFORE_PUNCTUATION = re.compile(r'\s+([,.:;?_!"()\[\]])')


def split_text(text: str) -> list[str]:
    """Split text into words and punctuation marks, dropping whitespace."""
    return [token.strip() for token in _SPLIT_PATTERN.split(text) if token.strip()]


def build_vocabulary(
    tokens: Iterable[str], special_tokens: Iterable[str] = (ENDOFTEXT, UNK)
) -> dict[str, int]:
    """Map each unique token (sorted) and then each special token to a consecutive id."""
    vocabulary = sorted(set(tokens))
    vocabulary.extend(token for token in special_tokens if token not in vocabulary)
    return {token: idx for idx, token in enumerate(vocabulary)}


class SimpleTokenizer:
    """Encode text to ids and back; unknown words map to `UNK`."""

    def __init__(self, vocabulary: dict[str, int]) -> None:
        if UNK not in vocabulary:
            raise ValueError(f"vocabulary must contain the {UNK!r} token")
        self.str_to_idx = vocabulary
        self.idx_to_str = {idx: token for token, idx in vocabulary.items()}

    def encode(self, text: str) -> list[int]:
        unk_id = self.str_to_idx[UNK]
        return [self.str_to_idx.get(token, unk_id) for token in split_text(text)]

    def decode(self, token_ids: Iterable[int]) -> str:
        text = " ".join(self.idx_to_str[idx] for idx in token_ids)
        return _SPACE_BEFORE_PUNCTUATION.sub(r"\1", text)
