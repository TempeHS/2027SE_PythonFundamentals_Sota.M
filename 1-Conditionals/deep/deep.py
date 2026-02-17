n = input(
    "What is the answer to the Great Question of Life, the Universe and Everything: "
)

match n:
    case "42" | "forty two" | "Forty Two" | "forty-two" | "Forty-Two":
        print("Yes")
    case _:
        print("No")
