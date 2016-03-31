infile = r"data.txt"

important = []
keep_phrases = ["test",
              "important",
              "keep me"]

with open(infile) as f:
    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                print(line)
                #important.append(line)
                break

#print(important)
