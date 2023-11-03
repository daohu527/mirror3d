from ..base import BaseDataset


class KITTI(BaseDataset):
    def __init__(self, root: str) -> None:
        super().__init__(root)
