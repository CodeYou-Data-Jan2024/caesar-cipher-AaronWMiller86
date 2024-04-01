def ceasar(text):
    result = ""
    for letter in text:
        if letter.isalpha():
            unicode = ord(letter) + 5
            result += chr(unicode)
        else:
            result += letter
    print("Your cipher text is: ")
    return result

print(ceasar(input("Enter Text: ")))