import re
#  fr = open("kool.txt", encoding="utf-8")
#  fa = open("500 000+ sona.txt", "a", encoding="utf-8")
#  fr2 = open("500 000+ sona.txt", "r")
fr = open("articel.txt", encoding="utf-8")
fa = open("articelfinal.txt", "a", encoding="utf-8")
fr2 = open("articelfinal.txt", "r")
count = 0


def isLineEmpty(line):
    return len(line.strip()) == 0


def secondhalf(string):
    length_string = len(string)
    first_length = round(length_string / 2)
    second_half = string[first_length:].lower()
    return second_half


def ending(string, rule, rule2, rule3):
    for element in rule:
        first_length = len(string) - len(element)
        sl = string[first_length:].lower()
        if element in sl and not secondhalf(t) == "ment":
            der_print = t + " der" + "  " + sl + "  " + element + "\n"
            der_find = str(t + " der" + "  " + sl + "  " + element)
            if der_find in fr2.read():
                pass
            print(der_print)
            fa.write(der_print)
            continue
    for element in rule2:
        first_length = len(string) - len(element)
        sl = string[first_length:].lower()
        if element in sl:
            die_print = t + " die" + "  " + sl + "  " + element + "\n"
            die_find = str(t + " die" + "  " + sl + "  " + element)
            if die_find in fr2.read():
                pass
            print(die_print)
            fa.write(die_print)
            continue
    for element in rule3:
        first_length = len(string) - len(element)
        sl = string[first_length:].lower()
        if element in sl:
            das_print = t + " das" + "  " + sl + "  " + element + "\n"
            das_find = str(t + " das" + "  " + sl + "  " + element)
            if das_find in fr2.read():
                pass
            print(das_print)
            fa.write(das_print)
            continue


der_rules = ["and", "ant", "ent", "er", "ig", "mus", "ist", "ling", "or", "ner", "smus"]
die_rules = ["ei", "enz", "heit", "keit", "ie", "ik", "in", "ion", "schaft", "tät", "ung"]
das_rules = ["chen", "lein", "nis", "ment", "o", "rum", "tum", "ma", "um"]
for line in fr:
    if " " == line:
        continue
    lines_of_words = (re.findall(r"(?i)\b[a-z, öüä]+\b", line))
    words = ', '.join(lines_of_words)
    p = words.split(" ", 1)[0]  # p = words # if no word after the german word
    s = re.findall('([A-Z][a-z]+)', p)
    t = (', '.join(s))
    if isLineEmpty(t) is True:
        continue
    ending(t, der_rules, die_rules, das_rules)

fr2.close()
fr.close()
fa.close()
