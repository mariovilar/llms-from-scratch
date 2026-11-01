from pathlib import Path
from unittest.mock import patch

from llms_from_scratch.data import DATA_DIR, download_text_file, read_text


def test_download_text_file_fetches_when_missing(tmp_path: Path) -> None:
    dest = tmp_path / "nested" / "the-verdict.txt"

    with patch("llms_from_scratch.data.urlretrieve") as mock_urlretrieve:
        mock_urlretrieve.side_effect = lambda _url, path: Path(path).write_text("hello")
        result = download_text_file("https://example.com/the-verdict.txt", dest)

    assert result == dest
    assert dest.read_text() == "hello"
    mock_urlretrieve.assert_called_once()


def test_download_text_file_skips_when_present(tmp_path: Path) -> None:
    dest = tmp_path / "the-verdict.txt"
    dest.write_text("already here")

    with patch("llms_from_scratch.data.urlretrieve") as mock_urlretrieve:
        result = download_text_file("https://example.com/the-verdict.txt", dest)

    assert result == dest
    assert dest.read_text() == "already here"
    mock_urlretrieve.assert_not_called()


def test_read_text_reads_utf8_from_data_dir(tmp_path: Path) -> None:
    (tmp_path / "sample.txt").write_text("Verney’s pavilion", encoding="utf-8")

    assert read_text("sample.txt", data_dir=tmp_path) == "Verney’s pavilion"


def test_bundled_corpus_is_available() -> None:
    assert (DATA_DIR / "the-lady-with-the-dog.txt").is_file()
