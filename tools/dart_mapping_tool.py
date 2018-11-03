from boardreader.dart_reader import DartReader

def get_points(modifier, number):
    mod_vals = {"Double":2, "Big":1, "Little":1, "Triple":3}
    return mod_vals.get(modifier) * number

def get_mapping_string(pins, modifier, number):
    return str(pins) + ": {\'modifier': '" + modifier + "', 'number': " + str(number) + ", 'points': " + str(get_points(modifier, number)) +  "},\n"

if __name__ == "__main__":
    file = open("dartboard_mappings.txt", "w")
    try:
        reader = DartReader()    
        modifiers = ['Double', 'Big', 'Triple', 'Little']
        for number in range(1,21):
            for modifier in modifiers:
                print "Press " + modifier + " " + str(number)
                dart_tuple = reader.read_dart()
                mapping_string = get_mapping_string(dart_tuple, modifier, number)
                print mapping_string
                file.write(mapping_string)
    except KeyboardInterrupt as e:
        file.close()
