f = open("test.txt", "w")
f.write("")
f.close()

f = open("test.txt", "w")
f.write("more")
exit()
f.write("\n")
f.write("even more")
f.write("\n")
exit()
f.write("even even more")
f.close()

