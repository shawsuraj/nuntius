def multiLineInput() :
    print ("\nnuntius >>> Body :\n")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text

def getMailInput() :
    print("here")
    frm = input("\nnuntius >>> From :")
    to = input("\nnuntius >>> To :")
    sub = input("\nnuntius >>> Subject : ")
    body = multiLineInput()

    return frm, to, sub, body