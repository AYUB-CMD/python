for i in range(1, 21):
    
    with open(f"chap9/tables/{i}.txt", 'w') as f:
            for j in range(1, 11):
                f.write(f"{i}*{j}={i*j}\n")
            if j != 10:
                f.write("\n")
         