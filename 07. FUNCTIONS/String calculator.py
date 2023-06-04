# Write a function that calculates the number of characters 
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def func(**kwargs):
    print(kwargs)
    return kwargs

w = "hello"
h=w.count("h")
e=w.count("e")
l=w.count("l")
o=w.count("o")
    
w = func(h = h, e = e, l = l, o = o)
