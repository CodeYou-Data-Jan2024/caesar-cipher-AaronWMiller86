def ceasar(text):
    result = ""
    for letter in text:
        if letter.isalpha():
            if chr(ord(letter) + 5).isalpha():
                unicode = ord(letter) + 5
                result += chr(unicode)
            else:
                unicode = ord(letter) - 21
                result += chr(unicode)
        else:
            result += letter
    print("Your cipher text is: ")
    return result

print(ceasar(input("Enter Text: ")))