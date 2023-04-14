from classes.street import Street

def csv_to_streets(file_path = "./data/default.csv"):
    streets = []
    with open(file_path, "r") as f:
        f = f.readlines()
        for line in f:
            line = line.split(",")
            if line[0] == "name":
                continue
            streets.append(Street(line[0], line[1], line[2], line[3]))
    return streets
