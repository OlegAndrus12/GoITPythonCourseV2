from __future__ import annotations

import json

# curl https://jsonplaceholder.typicode.com/posts/
# wget -O-  https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
