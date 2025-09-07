import pandas as pd

user_profiles = {
    "user_001": {
        "name": "Aarav Nair",
        "age": 29,
        "email": "aarav.nair@example.com",
        "is_active": True,
        "roles": ["admin", "editor"]
    },
    "user_002": {
        "name": "Meera Thomas",
        "age": 34,
        "email": "meera.thomas@example.com",
        "is_active": False,
        "roles": ["viewer"]
    },
    "user_003": {
        "name": "Ravi m n ",
        "age": 41,
        "email": "ravi.mn@example.com",
        "is_active": True,
        "roles": ["editor", "contributor"]
    }
}

user_df = pd.DataFrame(user_profiles)
print(user_df)

