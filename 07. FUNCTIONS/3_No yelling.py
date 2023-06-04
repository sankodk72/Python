# https://www.codewars.com/kata/no-yelling

def filter_words(st):
    a = st.split()
    b = " ".join(a)
    c = b.capitalize()
    return c
