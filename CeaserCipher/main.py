import encoder
import decoder
import os
cls= lambda:os.system('cls')
print('''
    __    ___   ____  _____  ____  ____  
   /  ]  /  _] /    |/ ___/ /    ||    \\ 
  /  /  /  [_ |  o  (   \\_ |  o  ||  D  )
 /  /  |    _]|     |\\__  ||     ||    / 
/   \\_ |   [_ |  _  |/  \\ ||  _  ||    \\ 
\\     ||     ||  |  |\\    ||  |  ||  .  \\
 \\____||_____||__|__| \\___||__|__||__|\\_|
                                         
    __  ____  ____  __ __    ___  ____   
   /  ]|    ||    \\|  |  |  /  _]|    \\  
  /  /  |  | |  o  )  |  | /  [_ |  D  ) 
 /  /   |  | |   _/|  _  ||    _]|    /  
/   \\_  |  | |  |  |  |  ||   [_ |    \\  
\\     | |  | |  |  |  |  ||     ||  .  \\ 
 \\____||____||__|  |__|__||_____||__|\\_|       
''')

go='yes'

while go == 'yes':
    process=input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    cls()
    word=input('Please write your message:\n')
    cipher_shift=int(input('Type the shift value:\n'))
    if process == 'encode':
        print(encoder.encode(word,cipher_shift))
    if process == 'decode':
        print(decoder.decode(word,cipher_shift))
    go=input('Type "yes" to go again, Otherwise type "no".')
    
    