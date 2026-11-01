# Contributing

Thanks for wanting to contribute to this study project. Contributions should prioritise teaching clarity, correctness and reproducible experiments.

## Before you start

Install Python 3.14 and [uv](https://docs.astral.sh/uv/), then set up the environment:

```bash
uv sync --locked --dev
```

The local `reference/` directory holds the book and its reference code for consultation. Do not modify it or include it in commits.

## Workflow

1. Create a descriptive branch from `main`.
2. Develop the explanation and the experiment in the notebook for the relevant chapter.
3. Once a piece is reusable, move it into `src/llms_from_scratch/` and import it from the notebook.
4. Add small tests for the important behaviour. Fast tests must not depend on datasets, weights or a GPU.
5. Run the local checks before opening a pull request:

   ```bash
   uv run pytest -q
   uv run ruff check .
   uv run ruff format --check .
   ```

## Code and notebooks

- Keep reusable code in the `src/` package, not only inside a notebook cell.
- Give modules descriptive names and keep one clear responsibility per file.
- Make notebooks readable from top to bottom: introduce the concept, show tensor shapes and check the result.
- Load data with `llms_from_scratch.data.read_text()` instead of relative paths, so notebooks work from any directory.
- Do not commit additional datasets, weights, secrets, logs or very large outputs. The small sample corpus under `data/` is an intentional exception.
- When an experiment is not deterministic, document the seed, the device and the limitations.
- Do not copy the PDF or the reference code into the project. If an implementation is adapted from an external source, say so and respect its license.

## Pull requests

The pull request description should explain what changes and which chapter or concept it affects. When relevant, include:

- the tests you ran and their results;
- whether you ran the full notebook, and on which device;
- dependency or file-structure changes;
- known limitations or next steps.

Pull requests must pass CI and stay focused. Content fixes, refactors and new implementations are welcome as long as they keep the educational goal.

## Issues

To report a bug, include the chapter, notebook or module affected, your operating system, Python version and a minimal reproducible example. For conceptual questions, explain which step of the book you are following and what you expected to get.
