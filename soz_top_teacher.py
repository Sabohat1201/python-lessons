import random
from uzwords import words
def get_word():
    word=random.choice(words)
    while "-" in word or " " in word:
        word=random.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letters=""
    for letter in word:
        if letter in user_letters:
            display_letters+=letter
        else:
            display_letters+="-"
    return display_letters
#print(display('аор',get_word()))
def play():
    word=get_word()
    word_letters=set(word)
    user_letters=''
    print(f"Мен {len(word)} хонали сон уйладим. Топа оласанми?")
    while word_letters:
        print(display(user_letters,word))
        if user_letters:
            print(f"Шу вактгача киритган харфларингиз: {user_letters}")
        letter=(input("Харф киритинг: ")).upper()
        if letter in user_letters:
            print("Бу харфни аввал киритгансиз.Бошка харф киритинг")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} харфи тугри")
        else:
            print("Бундай харф йук!")
        user_letters+=letter
    print(f"Табриклайман! {word} сузини {len(user_letters)} та уриниш билан топдингиз")
print(play())
