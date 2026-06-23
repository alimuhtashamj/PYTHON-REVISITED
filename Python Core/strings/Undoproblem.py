emails = ["  user1@gmail.com ", "user2@yahoo.com", "  user3@outlook.com  "]
for i in emails:
    i.strip()
    for j in i:
        if j == "@":
            print(j)
            