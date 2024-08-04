def decode(keyword,shift):
    keyword=list(keyword)
    word=[]
    for letter in keyword:
        decode_letter=ord(letter)-shift
        if decode_letter<ord('a'):
            decode_letter=ord('z')-(ord('a')-decode_letter)+1
        word.append(chr(decode_letter))        
    return "".join(word) 


