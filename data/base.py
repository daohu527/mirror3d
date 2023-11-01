
from typing import Any

import torch.utils.data as data


class BaseDataset(data.Dataset):
    """
    refer to
    https://pytorch.org/vision/stable/_modules/torchvision/datasets/vision.html#VisionDataset

    Args:
        data (_type_): _description_

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
    """
    # Todo(zero): add more params
    def __init__(self, root: str) -> None:
        pass

    # Todo(zero): torch type is T_co
    def __getitem__(self, index: int) -> Any:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
