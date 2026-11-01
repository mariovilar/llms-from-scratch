import pytest

from llms_from_scratch.ch02 import ENDOFTEXT, UNK, SimpleTokenizer, build_vocabulary, split_text

TEXT = "The lady, with the dog."


def test_split_text_separates_punctuation_and_drops_whitespace() -> None:
    assert split_text("Hello,  world.\nIs this-- a test?") == [
        "Hello",
        ",",
        "world",
        ".",
        "Is",
        "this",
        "--",
        "a",
        "test",
        "?",
    ]


def test_build_vocabulary_is_sorted_and_appends_special_tokens() -> None:
    vocabulary = build_vocabulary(["b", "a", "b"])

    assert vocabulary == {"a": 0, "b": 1, ENDOFTEXT: 2, UNK: 3}


def test_encode_decode_round_trip() -> None:
    tokenizer = SimpleTokenizer(build_vocabulary(split_text(TEXT)))

    assert tokenizer.decode(tokenizer.encode(TEXT)) == TEXT


def test_unknown_words_map_to_unk() -> None:
    vocabulary = build_vocabulary(split_text(TEXT))
    tokenizer = SimpleTokenizer(vocabulary)

    ids = tokenizer.encode(f"The cat. {ENDOFTEXT} The dog.")

    assert ids.count(vocabulary[UNK]) == 1
    assert vocabulary[ENDOFTEXT] in ids
    assert tokenizer.decode(ids) == f"The {UNK}. {ENDOFTEXT} The dog."


def test_vocabulary_without_unk_is_rejected() -> None:
    with pytest.raises(ValueError):
        SimpleTokenizer({"a": 0})
