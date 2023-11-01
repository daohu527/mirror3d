from ..base import BaseDataset


class nuScenes(BaseDataset):
    def __init__(self, root: str) -> None:
        super().__init__(root)
