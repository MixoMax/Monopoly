from classes.street import Street

def csv_to_streets(file_path = "./data/default.csv"):
    streets = []
    with open(file_path, "r", encoding="UTF-8") as f:
        f = f.readlines()
        for line in f:
            line = line.split(",")
            if line[0] == "name":
                continue
            name, price, rent, house_price, color = line
            streets.append(Street(name, int(price), int(rent), int(house_price), color))
    return streets
