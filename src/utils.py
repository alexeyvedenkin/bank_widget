import json
import os
from typing import Any, Dict, List


def get_financial_transactions(path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as file_json:
        data_json = json.load(file_json)
    return data_json


transactions = get_financial_transactions("C:\\Users\\Макс\\my_prj\\bank widget\\data\\operations.json")

# print(transactions)
