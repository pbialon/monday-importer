from pathlib import Path
from typing import List

from models.expense import Expense


class BaseConverter:
    def __init__(self, csv_file_path: Path) -> None:
        pass
    
    def convert(self) -> List[Expense]:
        pass