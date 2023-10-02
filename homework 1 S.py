for i in range(1, 151):
    output = {3: "Fizz", 5: "Buzz"}.get(i % 3, "") + {5: "Buzz"}.get(i % 5, "")
    print(output if output else i)
