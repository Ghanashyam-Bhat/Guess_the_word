#Word guessing game
print("Guess the word.")
print(" 5 wrong attempts are allowed")
new_word = ('Ghanashyam').lower()
given = new_word
word_space = ""
for x in new_word :
    word_space += x
    word_space += " "
word_list = word_space.split(" ")
word_list.pop()
code_together = "*"*len(new_word)
code = ""
for g in code_together :
    code += g
    code += " "
code_list = code.split(" ")
code_list.pop()
print(code)
r = 0
p = 0
while r <= 5  :
    entered = input("> ").lower()
    if entered in new_word:
        place = new_word.find(entered)
        code_list.pop(place)
        code_list.insert(place , entered)
        code = ""
        for i in code_list :
            code += i
        print(code)
        word_list.pop(place)
        word_list.insert( place , "+")
        new_word = ""
        for y in word_list :
            new_word += y
        p += 1
        if p == len(given) :
            print("You won")
            break

    elif entered not in new_word :
        if 5-r > 0 :
            print("Wrong")
            r += 1
            print(f" {5 - r} more wrong guesses are allowed")
        else :
            print("You lose")
            print(f"The secret word is '{given}'")
            break
