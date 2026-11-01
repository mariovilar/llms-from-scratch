import json
from pathlib import Path

import pytest

NOTEBOOKS = sorted((Path(__file__).parents[1] / "notebooks").glob("*.ipynb"))


@pytest.mark.parametrize("notebook", NOTEBOOKS, ids=lambda path: path.name)
def test_non_empty_notebooks_are_valid_json(notebook: Path) -> None:
    if notebook.stat().st_size == 0:
        pytest.skip("notebook is still empty (work in progress)")

    content = json.loads(notebook.read_text(encoding="utf-8"))

    assert content["nbformat"] >= 4
    assert isinstance(content["cells"], list)
