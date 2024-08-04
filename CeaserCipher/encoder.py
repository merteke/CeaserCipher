def encode(keyword,shift):
    keyword=list(keyword)
    word=[]
    for letter in keyword:
        encode_letter=ord(letter)+shift
        if encode_letter>ord('z'):
            encode_letter=ord('a')+encode_letter-ord('z')-1
        word.append(chr(encode_letter))        
    return "".join(word) 

