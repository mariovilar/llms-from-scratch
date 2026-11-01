import torch

from llms_from_scratch import get_device, main


def test_package_exposes_cli_entry_point() -> None:
    assert callable(main)


def test_get_device_returns_a_usable_device() -> None:
    device = get_device()

    assert device.type in {"cuda", "mps", "cpu"}
    assert torch.ones(1, device=device).item() == 1
