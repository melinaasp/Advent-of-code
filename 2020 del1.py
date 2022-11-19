file = open("nummer")
test_input = file.read()
file.close()

test_input = test_input.splitlines()

data= []
for elem in test_input:
    data.append(int(elem))

for a in range (len(data)):
    for b in range (a + 1, len(data)):
        if data[a] + data[b] == 2020:
            print (data[a] * data[b])
            break