input = ["Alice 95", "Bob 78", "Charlie 92", "David 85"]

sorted = list(sorted(
    [(name, int(score)) 
      for name, score in [tuple(el.split(" ")) for el in input]],
        key=lambda x: list(x)[1], reverse=True))

print(sorted)
