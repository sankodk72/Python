# You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words 
# - "better", "never" and "is" in the given line
# - you need to display all text in uppercase (all letters in uppercase)
# - replace all occurrences of the symbol “i” with “&”

rule = 'Although never is often better than *right* now'
search1 = rule.count('better')
search2 = rule.count('never')
search3 = rule.count('is')
letters = rule.upper()
replacing = rule.replace('i','&')
print(f"better {search1}, never {search2}, is {search3}")
print(letters, replacing, sep='\n')
