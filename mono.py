
alf = tuple("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
N = len(alf)


def encrypt(text, a, k):
    print(f"Зашифровка по ключу: {key}\n")
    text = text.upper()
    gv_txt = ""
    for ch in text:
        if ch in alf:
            enc_ch = (a * alf.index(ch) + key) % (N)
            gv_txt += alf[enc_ch]
        else:
            gv_txt += ch    
    return gv_txt

def decrypt(text, a, k):
    print(f"Расшифровка по ключу: {key}\n")
    text = text.upper()
    gv_txt = ""
    a_inv = 0
    flag = 0
    for i in range(0, N):
        flag = (a * i) % (N)
        if flag == 1:
            a_inv = i
        
    for ch in text:
        if ch in alf:
            enc_ch = ( a_inv * (alf.index(ch) - key) ) % (N)
            gv_txt += alf[enc_ch]
        else:
            gv_txt += ch    
    return gv_txt


a = 13
key = 5


while True:
    user = input("""введите "шифр", если нужно зашифровать текст или "расш", если нужно расшифровать, или же введи что-нибудь другое для того чтобы выйти из программы\n """)

    if user == 'шифр':
        text = input("введи текст, который нужно зашифровать\n")
        ciphtxt = encrypt(text, a, key)
        print("Ваш зашифрованный текст\n")
        print(ciphtxt)
        print('\n')

    elif user == 'расш':
        text = input("введи текст, который нужно расшифровать\n")
        firstxt = decrypt(text, a, key)
        print("Ваш расшифрованный текст\n")
        print(firstxt)
        print('\n')

    else : break

input("Прекращение работы программы")
