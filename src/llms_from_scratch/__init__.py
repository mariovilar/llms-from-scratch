"""Educational, from-scratch implementations of transformer language models."""

import torch


def get_device() -> torch.device:
    """Return the best available accelerator: CUDA, then Apple MPS, then CPU."""
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def main() -> None:
    print(f"PyTorch {torch.__version__} | device: {get_device()}")
