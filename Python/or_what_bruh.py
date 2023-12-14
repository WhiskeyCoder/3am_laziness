with open('../project/or_whatbruh.txt', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if "OR" in line:
            line = line.replace("OR", "\n")
            print(line)
        # remove white space from the start or end of each line
        line = line.strip()
        # remove empty lines
