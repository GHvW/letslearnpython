from typing import Dict, Optional


def fake_db_table() -> Dict[int, str]:
    return {
        1: "Austin",
        2: "Denver",
        3: "Olympia",
        4: "Tallahassee"
    }


# why the error?
def capital_by_id(capitals_table: Dict[int, str], id: int) -> Optional[str]:
    if id in capitals_table.keys():
        return capitals_table[id]


result = capital_by_id(fake_db_table(), 1)
print(result)