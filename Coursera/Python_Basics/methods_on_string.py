ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

############################

aa = "    Hello, World    "

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")

news = ss.replace("o", "***")
print(news)

#############################

s = "python rocks"
print(s[1]*s.index("n"))