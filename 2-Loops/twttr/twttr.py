text_novowels = input("Input text: ")

result = (
    text_novowels.replace("a", "")
    .replace("e", "")
    .replace("i", "")
    .replace("o", "")
    .replace("u", "")
    .replace("A", "")
    .replace("E", "")
    .replace("I", "")
    .replace("O", "")
    .replace("U", "")
)

print(result)
