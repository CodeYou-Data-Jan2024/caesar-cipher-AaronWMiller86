cipher_amount = 5
correction_ammount = 26 - cipher_amount

def ceasar(text):
    result = ""
    for letter in text:
        if letter.isalpha():
            if chr(ord(letter) + cipher_amount).isalpha():
                unicode = ord(letter) + cipher_amount
                result += chr(unicode)
            else:
                unicode = ord(letter) - correction_ammount
                result += chr(unicode)
        else:
            result += letter
    return "The encrypted sentence is: " + result.lower()

print(ceasar(input("Please enter a sentence: ")))