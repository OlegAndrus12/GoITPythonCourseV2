from pathlib import Path

list_data = ["First line", "Hello world", "Aloha guys", "Last line"]

# remove reports, dirs are not created by default
with open("reports/data.txt", "w", encoding="utf-8") as f:
    for line in list_data:
        f.write(f"{line}\n")

with open("reports/data-all.txt", "w", encoding="utf-8") as f:
    f.writelines(list_data)
