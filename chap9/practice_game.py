def game():
    return 659

score = game()

with open('chap9/hiscore.txt') as f:
    hi_score = f.read()

if hi_score == '':
    with open('chap9/hiscore.txt', 'w') as f:
        f.write(str(score))   

elif int(hi_score) < score :
    with open('chap9/hiscore.txt', 'w') as f:
        f.write(str(score))   