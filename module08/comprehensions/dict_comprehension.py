original_dict = {
    "The Legend of Zelda: Ocarina of Time": 1998,
    "Grand Theft Auto IV": 2008,
    "Red Dead Redemption": 2018,
    "Perfect Dark": 2000,
    "The Orange Box": 2007,
}


# lowercase titles
# select all after 2000 year
# select all in range

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)
