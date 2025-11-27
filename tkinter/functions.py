def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(text):
    text = str(text) # numbers do not have a len -> convert to str
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


def centre_text2(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# write to file
#with open("centered", mode='w') as centered_file:

    # call the function
    #centre_text2(12, file=centered_file)
    #centre_text2("spam and eggs", file=centered_file)
    #centre_text2("spam, spam and eggs", file=centered_file)
    #centre_text2("spam, spam, spam and spam", file=centered_file)
    #centre_text2("first", "second", 3, 4, "spam", sep=":", file=centered_file)

print(centre_text2("Spam and eggs"))
print(centre_text2("Spam, spam and eggs"))
print(centre_text2(12))
print(centre_text2("Spam, spam, spam and spam"))
print(centre_text2("first", "second", 3, 4, "spam", sep=":"))

print("=" + str(12 * 3))
print(sorted(["b", "d", "c", "a"]))