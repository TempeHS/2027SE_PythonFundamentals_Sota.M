text_novowels = input("Input text: ")

result = (
    text_novowels.replace("a", "")
    .replace("e", "")
    .replace("i", "")
    .replace("o", "")
    .replace("u", "")
)

print(result)
