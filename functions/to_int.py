def to_int(s):
    try:
        return int(s)
    except ValueError:
        int_str =""
        for char in str(s):
            if char == ".":
                break
            int_str += str(char)
        
        return int(int_str)