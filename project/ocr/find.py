




def find(search, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    found = False

    for i, line in enumerate(lines, start=1):
        if search.lower() in line.lower():
            print("Line:", i)
            print(line.strip())
            found = True

    if found == False:
        print("Not found!")