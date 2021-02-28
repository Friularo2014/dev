import string

def longest_word(t):
    max_word_len = -1
    idx1 = 0
    idx2 = t.find(' ', idx1+1)
    while idx2 != -1:
        word_len = idx2-idx1
        if word_len > max_word_len:
            max_word_len = word_len
        idx1 = idx2
        idx2 = t.find(' ', idx1+1)
    return max_word_len


def display_solution(decrypted_text, password):
    print('=== password as ascii : ' + str(password))
    print('=== password as string: ', end = '')
    for p_ascii in password:
        print(chr(p_ascii), end = '')
    print()
    print('=== decrypted_text: ' + decrypted_text)
    ascii_sum = 0
    for s in decrypted_text:
        ascii_sum += ord(s)
    print('=== ascii_sum = ' + str(ascii_sum))
    print()
    
    
txt = []
file = open("p059_cipher.txt", "r")
for line in file:
    fields = line.split(",")
    for field in fields:
        txt.append(int(field))

for a in list(string.ascii_lowercase):
    for b in list(string.ascii_lowercase):
        for c in list(string.ascii_lowercase):
            password = [ord(a), ord(b), ord(c)]
            decrypted_text = ''
            char_ok = True
            i = 0
            while i < len(txt) and char_ok:
                d = chr(txt[i] ^ password[i%3])
                char_ok = d in string.printable
                if char_ok:
                    i += 1
                    decrypted_text += d

            if i == len(txt) \
               and char_ok   \
               and 1 < longest_word(decrypted_text) < 34:
                   display_solution(decrypted_text, password)

