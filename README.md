# LLMs from scratch

[![CI](https://github.com/mariovilar/llms-from-scratch/actions/workflows/ci.yml/badge.svg)](https://github.com/mariovilar/llms-from-scratch/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A personal, step-by-step implementation of the ideas in Sebastian Raschka's [*Build a Large Language Model (From Scratch)*](https://www.manning.com/books/build-a-large-language-model-from-scratch). The aim is to understand each component by building it, explaining the reasoning in notebooks and moving reusable code into a small Python package.

**This is an ongoing study project.** I am working through the book in order, so notebooks and modules will grow as I reach each topic. This is not the book's official implementation; see [Raschka's repository](https://github.com/rasbt/LLMs-from-scratch) for the original code.

## What this project covers

The planned path follows the book from the foundations to a usable language model:

1. PyTorch fundamentals and the training loop (Appendix A).
2. Text preparation: tokenization, sampling and embeddings (Chapter 2).
3. Attention mechanisms and transformer blocks (Chapter 3).
4. GPT architecture and text generation (Chapter 4).
5. Pretraining and model evaluation (Chapter 5).
6. Fine-tuning for classification (Chapter 6).
7. Fine-tuning to follow instructions (Chapter 7).

Each topic starts as an experiment and explanation in `notebooks/`. Code that is useful across experiments moves to `src/llms_from_scratch/`, with small tests in `tests/`. The [PyTorch](notebooks/pytorch.ipynb), [Chapter 2](notebooks/ch02.ipynb) and [Chapter 3](notebooks/ch03.ipynb) notebooks show the work currently in the repository; an existing notebook may still be in progress.

## Get started

You need Python 3.14 and [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/mariovilar/llms-from-scratch.git
cd llms-from-scratch
uv sync --locked --dev
uv run jupyter lab
```

Select the kernel from the `.venv` environment created by uv. The notebooks use the installed package to load data, so they can run regardless of Jupyter's working directory.

To check the installed PyTorch version and selected device (CUDA, Apple MPS or CPU):

```bash
uv run llms-from-scratch
```

## Repository layout

```text
notebooks/                     Explanations and experiments
src/llms_from_scratch/         Reusable Python code and a device-check CLI
tests/                         Fast, deterministic checks
data/                          Small sample corpus
reference/                     Local book PDF and reference code (Git-ignored)
```

The local `reference/` directory is for consultation and is not part of the published repository. Model weights, generated files and additional datasets are also Git-ignored.

## Checks

```bash
uv run pytest -q
uv run ruff check .
uv run ruff format --check .
```

[CI](.github/workflows/ci.yml) runs tests on Linux, macOS and Windows, plus lint and formatting checks. It checks the notebook files but does not execute every experiment end to end.

## Data and attribution

The sample corpus is Anton Chekhov's *The Lady with the Dog* in Constance Garnett's English translation, used instead of the book's sample story. It is available in [*The Lady with the Dog and Other Stories*](https://www.gutenberg.org/ebooks/13415).

The original code and notes in this repository are released under the [MIT License](LICENSE). The book, its PDF and the local reference code are separate works and are not covered by that license. See [Raschka's repository](https://github.com/rasbt/LLMs-from-scratch) for more information about the book and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines to this repository.
