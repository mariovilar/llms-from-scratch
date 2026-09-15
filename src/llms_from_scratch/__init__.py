def main() -> None:
    import torch
    print(torch.backends.mps.is_available())