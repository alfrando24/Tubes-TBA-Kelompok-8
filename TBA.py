def tokenRecognizer(word: str):
    word = word.lower()
    try:
        if subjek(word): return 'S'
        elif predikat(word): return 'P'
        elif objek(word): return 'O'
        elif keterangan(word): return 'K'
        else: raise Exception("TokenUnrecognizedError")
    except Exception as e: 
        print(f"Kata \"{word}\" tidak masuk ke kategori token manapun")
        return '?'

def subjek(word: str) -> bool:
    #rafel, raka, rafi, rafli, rani
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0: current_State_Q = 1 if letter == 'r' else -1
            case 1: current_State_Q = 2 if letter == 'a' else -1
            case 2: 
                if letter == 'f': current_State_Q = 3
                elif letter == 'k': current_State_Q = 9
                elif letter == 'n': current_State_Q = 11
                else: current_State_Q = -1
            case 3: 
                if letter == 'i': current_State_Q = 4 # final state rafi
                elif letter == 'e': current_State_Q = 5
                elif letter == 'l': current_State_Q = 6
                else: current_State_Q = -1
            case 5: current_State_Q = 7 if letter == 'l' else -1 # final state rafel
            case 6: current_State_Q = 8 if letter == 'i' else -1 #final state rafli
            case 9: current_State_Q = 10 if letter == 'a' else -1 # final state raka
            case 11: current_State_Q = 12 if letter == 'i' else -1 # final state rani    
    return current_State_Q in {4, 7, 8, 10, 12}


def predikat(word: str) -> bool:
    #membeli, memasak, memeriksa, membuat, menanam
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0:current_State_Q = 1 if letter == 'm' else -1
            case 1:current_State_Q = 2 if letter == 'e' else -1
            case 2: 
                if letter == 'm': current_State_Q = 3
                elif letter == 'n': current_State_Q = 18
                else: current_State_Q = -1
            case 3: 
                if letter == 'b': current_State_Q = 4
                elif letter == 'a': current_State_Q = 10
                elif letter =='e': current_State_Q=13
                else: current_State_Q = -1
            case 4: 
                if letter == 'u': current_State_Q = 5
                elif letter == 'e': current_State_Q = 8
                else: current_State_Q = -1
            case 5: current_State_Q = 6 if letter == 'a' else -1
            case 6: current_State_Q = 7 if letter == 't' else -1 #final state 
            case 7: current_State_Q = 8 if letter == 'e' else -1
            case 8: current_State_Q = 9 if letter == 'l' else -1
            case 9: current_State_Q = 7 if letter == 'i' else -1 #final state 
            case 10: current_State_Q = 11 if letter == 's' else -1
            case 11: current_State_Q=12 if letter=='a' else -1
            case 12: current_State_Q=7 if letter =='k' else -1 #final state 
            case 13: current_State_Q=14 if letter=='r' else -1
            case 14: current_State_Q=15 if letter=='i' else -1
            case 15: current_State_Q=16 if letter=='k' else -1
            case 16: current_State_Q=17 if letter=='s' else -1
            case 17: current_State_Q=7 if letter=='a' else -1 #final state 
            case 18: current_State_Q=19 if letter=='a' else -1
            case 19: current_State_Q=20 if letter=='n' else -1
            case 20: current_State_Q=21 if letter=='a' else -1
            case 21: current_State_Q= 7 if letter=='m' else -1 #final state 
    return current_State_Q == 7

def objek(word: str) -> bool:
    #paku, pasta, pasien, patung, padi
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0: current_State_Q = 1 if letter == 'p' else -1
            case 1: current_State_Q = 2 if letter == 'a' else -1
            case 2: 
                if letter == 'k': current_State_Q = 3
                elif letter == 't': current_State_Q = 5
                elif letter == 's': current_State_Q = 9
                elif letter == 'd': current_State_Q = 15
                else: current_State_Q = -1
            case 3: current_State_Q = 4 if letter == 'u' else -1 #final state paku
            case 5: current_State_Q = 6 if letter == 'u' else -1
            case 6: current_State_Q = 7 if letter == 'n' else -1
            case 7: current_State_Q = 8 if letter == 'g' else -1 #final state patung
            case 9:
                if letter == 'i': current_State_Q=10
                elif letter =='t': current_State_Q=13
                else: current_State_Q=-1
            case 10: current_State_Q=11 if letter=='e' else -1
            case 11: current_State_Q=12 if letter=='n' else -1 #final state pasien
            case 13: current_State_Q=14 if letter=='a' else -1 #final state pasta
            case 15: current_State_Q=16 if letter=='i' else -1   #final state padi 
    return current_State_Q in {4, 8, 12, 14, 16}

def keterangan(word: str) -> bool:
    #ditoko, didapur, diigd, dibengkel, disawah
    current_State_Q = 0
    for letter in word:
        match current_State_Q:
            case -1: break
            case 0: current_State_Q = 1 if letter == 'd' else -1
            case 1: current_State_Q = 2 if letter == 'i' else -1
            case 2:
                if letter == 't': current_State_Q = 3
                elif letter == 'd': current_State_Q = 7
                elif letter == 'b': current_State_Q = 12
                elif letter =='i': current_State_Q=19
                elif letter == 's':current_State_Q=22
                else: current_State_Q = -1
            case 3: current_State_Q = 4 if letter=='o' else -1
            case 4: current_State_Q = 5 if letter=='k' else -1
            case 5: current_State_Q = 6 if letter=='o' else -1 #final state toko
            case 7: current_State_Q = 8 if letter=='a' else -1
            case 8: current_State_Q = 9 if letter=='p' else -1
            case 9: current_State_Q = 10 if letter=='u' else -1
            case 10: current_State_Q = 11 if letter=='r' else -1 #final state dapur
            case 12: current_State_Q = 13 if letter=='e' else -1
            case 13: current_State_Q = 14 if letter=='n' else -1
            case 14: current_State_Q = 15 if letter=='g' else -1
            case 15: current_State_Q = 16 if letter=='k' else -1
            case 16: current_State_Q = 17 if letter=='e' else -1
            case 17: current_State_Q = 18 if letter=='l' else -1 #final state bengkel
            case 19: current_State_Q = 20 if letter=='g' else -1
            case 20: current_State_Q = 21 if letter=='d' else -1 #final state igd
            case 22: current_State_Q = 23 if letter=='a' else -1
            case 23: current_State_Q = 24 if letter=='w' else -1
            case 24: current_State_Q = 25 if letter=='a' else -1
            case 25: current_State_Q = 26 if letter=='h' else -1 #final state sawah
    return current_State_Q in {6, 11, 18, 21, 26}
def parser(sentence):
    ERR = Exception('ParsingError')
    words = sentence.split() #memecah kalimat menjadi kata-kata
    words.append('')
    struktur = []
    stack = []
    state = 0
    #print("Stack:")
    #print(stack)
    stack.append('#')
    state = 1
    #print(stack)
    stack.append('START')
    state = 2
    #iterasi
    i = 0
    try:
        while stack[-1] != '#':
            #print(stack)
            word = words[i]
            if word != '': 
                token = tokenRecognizer(word)
            match stack[-1]:
                case 'START':
                    if token == 'S':
                        stack.pop()
                        stack.append('O OR K')
                        stack.append('P')
                        stack.append('S')
                    else: 
                        raise ERR
                case 'O OR K':
                    if word == '':
                        stack.pop()
                    else:
                        if token == 'O':
                            stack.pop()
                            stack.append('Z')
                            stack.append('O')
                        elif token == 'K':
                            stack.pop()
                            stack.append('Z')
                        else: 
                            raise ERR
                case 'Z':
                    if word == '':
                        stack.pop()
                    elif token == 'K':
                        stack.pop()
                        stack.append('K')
                    else: 
                        raise ERR
                case 'S':
                    if token == 'S':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'P':
                    if token == 'P':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'O':
                    if token == 'O':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'K':
                    if token == 'K':
                        struktur.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case _:
                    if token != '?':
                        stack.pop()
                        i += 1
                    else: 
                        raise ERR
        #print(stack)
        stack.pop()
        #print(stack)

        print("Struktur: ", end='')
        for i in struktur[:-1]:
            print(f"{i} - ", end='')
        print(struktur[-1])
        return True 
    except Exception as e:
        print(f"Kalimat \"{sentence}\" Struktur Tidak Sesuai")
        return False

if __name__ == '__main__': 
    sentence = input("Masukkan Kalimat: ")
    print()
    print(f"String: {sentence}\nStatus: Diterima\n") if parser(sentence) else print(f"String: {sentence}\nStatus: Ditolak \n") 

print("KELOMPOK 8")
print("1301223195-1301223035-1301220188 \n")