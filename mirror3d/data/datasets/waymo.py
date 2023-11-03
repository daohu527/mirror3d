from ..base import BaseDataset


class Waymo(BaseDataset):
    def __init__(self, root: str) -> None:
        super().__init__(root)
