import unittest


def main(input):
    return input.title()

def main2(input):
    if not input or len(input) == 0:
        return ""
    result = "" 
    for word in input.split(" "):
        if len(word) > 0:
            result += word[0].upper() + word[1:] + " "
        else:
            result += " "
   # print(result)
    #return result
    return result[0:len(result)-1]
    #return " ".join(result)
    
if __name__ == '__main__':
    print(main("inputted string"))
    print(main2("inputted string"))
    print(main("i'm dumb"))
    print(main2("i'm dumb"))
    print(main(""))
    print(main2(""))
    print(main("Hello     World"))
    print(main2("Hello     World"))
