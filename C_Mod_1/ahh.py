def mirroted_strin(my_string):
    forwards = ""
    backwards = ""

    for character in my_string:
        if character.isalpha():
            forwards += character 
            #print(forwards)
            backwards = character + backwards
            print(backwards)

print(mirroted_strin("12 Noon"))