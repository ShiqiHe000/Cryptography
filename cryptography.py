
import sys

# 26 letters we use to create message
# Right now the encryption and decryption only works for lowercase letter. 
letter = "abcdefghijklmnopqrstuvwxyz"
# print(letter.find('d'))
# print(letter[20])
# Caesar Cipher Method =======================================================

# Decode a encrypted message-----------------------------------------------------
# decode the encoded word (a string) with the shifted number back to normal word
def decode_to_word(word, shift):
    word_decode = ""
    for c in word:
        index = letter.find(c)
        if(index == -1): # if punctuation
            word_decode = word_decode + c
        else: # if character
            index_shifted = (index + shift) % 26
            c_decode = letter[index_shifted]
            word_decode = word_decode + c_decode
    return word_decode

# function to decode the whole encoded message 
# massage: a string of the encoded message
# shift (int): the offset. 
def decode(message, shift):
    message_list = message.split()
    decode_list = []
    for word in message_list:
        word_decode = decode_to_word(word, shift)
        decode_list.append(word_decode)
    # join the decode_list back to a string
    decode_message = ' '.join(decode_list)
    print(decode_message)
    return decode_message

# test
# message1 = "hello! hello! hello!"
# message1 = "ebiil! ebiil! ebiil!"
# # message2 = "hey there! this is an example of a caesar cipher. 
# #               were you able to decode it? 
# #               i hope so! send me a message back with the same offset!"
# message2 = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
# offset = 10
# decode(message2, offset)

#------------------------------------------------------------------------------

# Encrypt a message -----------------------------------------------------------
# Input the normal word, output the encoded word. 
# shift (int): the offset user defined
def encode_to_word(word, shift):
    word_encode = ""
    for c in word:
        index = letter.find(c)
        if(index == -1):
            word_encode = word_encode + c
        else:
            index_shifted = (index + 26 - shift) % 26
            c_encode = letter[index_shifted]
            word_encode = word_encode + c_encode
    return word_encode


# encode your message (a string) into Caesar Cipher.
# Your message should be in lowercase. 
def encode(message, shift):
    message_list = message.split()
    encode_list = []
    for word in message_list:
        word_encode = encode_to_word(word, shift)
        encode_list.append(word_encode)
    # join the decode_list back to a string
    encode_message = ' '.join(encode_list)
    print(encode_message)
    return encode_message

# test
# message = 'hi pen pal! good to hear from you! now i am able to decode caesar cipher. let us talk in this way!'
# shift = 10
# my_message = encode(message, shift)
# decode(my_message, offset)
#-----------------------------------------------------------------------------

#==============================================================================


# Vigenère Cipher Method ======================================================
# return the place value (indices) of the keyword
def keyword_indices(keyword):
    indices = []
    for c in keyword:
        indices.append(letter.find(c))
    return indices

# test
# print(keyword_indices('dog'))

# Turn a normal word into encrypted word 
# word: original word
# keyword_indicies: a list of the keyword phrase place value (not including the 
#                   punctuation)
def encrypt_word(word, keyword_indices):
    
    i = 0   # index for keyword_indices
    encoded_word = '' # the encoded word we return
    
    for c in word:
        if(c not in letter):    # punctuation
            encoded_word = encoded_word + c
        else:
           c_index = letter.find(c) 
           code_index = c_index + keyword_indices[i]
           if(code_index > 25):
               code_index -= 26
           i += 1
           encoded_word = encoded_word + letter[code_index]
    return encoded_word

# Form the list of indices of the according keyword phrases
# massage_lst: a list of the words in the message
# keyword: the keyword
# keyword_indices: a list of the place values of each letter of the keyword
def form_keyword_phrases_indices_list(message_lst, keyword, keyword_indices):
    keyword_phrases_indices = []
    key_index = 0
    key_len = len(keyword)

    for word in message_lst:
        key_indices_now = []    
        
        for c in word:
            if(c not in letter):    # puncuation
                continue
            else:
                key_index = (key_len + key_index) % key_len
                # print(key_index)
                # print(type(keyword_indices[key_index]))
                key_indices_now.append(keyword_indices[key_index])
                # print(key_indices_now)
                key_index += 1
        # print(word)      
        keyword_phrases_indices.append(key_indices_now)
        
    return keyword_phrases_indices
                

def encryption_Veigenere(message, keyword):
    # get the message list
    message_lst = message.split()
    # print(message_lst)
    
    # get keyword place value
    keyword_place_values = keyword_indices(keyword)
    
    # get the list of the keyword phrase indices
    keyword_phrases_indices = \
        form_keyword_phrases_indices_list(message_lst, \
                                          keyword, keyword_place_values)
    # print(keyword_phrases_indices)
    
    # form the encrypted word
    encoded_message_lst = []
    i = 0
    for word in message_lst:
        encoded_message_lst.append(encrypt_word(word, keyword_phrases_indices[i]))
        i += 1
        
    # turn the encrypted list into a string
    encoded_message_str = ' '.join(encoded_message_lst)
    print(encoded_message_str)
    return encoded_message_str

# encryption_Veigenere("barry is the spy.", 'dog')

# translate the encrypted word back to normal word. 
# word: encrypted word
# keyword_place_value_lst: a list of keyword place values (not include punctuations.)
def deocde_word_back(word, keyword_place_value_lst):
    
    decoded_word = ''
    i = 0
    
    for c in word:
        if(c not in letter): # punctuation
            decoded_word = decoded_word + c
        else:
            code_index = letter.find(c)
            key_index = keyword_place_value_lst[i]
            i += 1
            normal_word_index = code_index - key_index
            if(normal_word_index < 0):
                normal_word_index += 26
            decoded_word = decoded_word + letter[normal_word_index]
    return decoded_word


# decode the encrypted message back to human language. 
# message: encrypted message
# keyword: the keyword to decode the message
def decode_Veigenere(message, keyword):
    # get the message list
    message_lst = message.split()
    
    # get keyword place value
    keyword_place_values = keyword_indices(keyword)
    
    # get the list of the keyword phrase indices
    keyword_phrases_indices = \
        form_keyword_phrases_indices_list(message_lst, \
                                          keyword, keyword_place_values)

    # decode the message_lst
    decoded_lst = []
    i = 0
    for word in message_lst:
        translate_back = deocde_word_back(word, keyword_phrases_indices[i])
        i += 1
        decoded_lst.append(translate_back)
    decoded_message = ' '.join(decoded_lst)
    print(decoded_message)
    return decoded_message

# decode_Veigenere('dfc aruw fsti gr vjtwhr wznj? vmph otis! \
#                  cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!', 'friends')
# result:
# you were able to decode this? 
# nice work! you are becoming quite the expert at crytography!
#==============================================================================

# interact with user===========================================================
# encrypt or decrype a message
print("Hello! Let's play with cryptography!")
print("If you want to try Caesar Cipher, please enter 1.")
print("If you want to try Vigenère Cipher, please enter 2.")
# user enter its choice
method_num = int(input("Enter you choice:"))

method1 = "Caesar Cipher"
method2 = "Vigenère Cipher"
if(method_num == 1):
    print("You have chosen", method1)
elif(method_num == 2):
    print("You have chosen", method1)
else:
    print("Invaild input. Abort.")
    sys.exit()

# encrypt a message or decrypt a message
print("Now let's start the game.")
print("If you want to encrypt a messsge, enter 1.")
print("If you want to decrypt a message, enter 2.")

message_en_or_de = int(input("Enter your choice here: "))
# validate input
if(message_en_or_de != 1 and message_en_or_de != 2):
    print("Invalid input. Abort")
    sys.exit()

# user input message
my_message = input("""Enter the message here 
(please use lowercase letters, punctuation is acceptable): \n""")

# now we generate the result
if(message_en_or_de == 1):  # encode
    
    if(method_num == 1):
        offset = int(input("What is the choice of the offset? Enter here: \n"))
        print("Here is your encoded message: ")
        encode(my_message, offset)
    else:
        my_keyword = input("What is your keyword? Enter here:")
        print("Here is your encoded message: ")
        encryption_Veigenere(my_message, my_keyword)
else:   # decode
    if(method_num == 1):
        offset = int(input("What is the choice of the offset? Enter here: \n"))
        print("Here is your decoded message: ")
        decode(my_message, offset)
    else:
        my_keyword = input("What is your keyword? Enter here:")
        print("Here is your decoded message: ")
        decode_Veigenere(my_message, my_keyword)
    
#==============================================================================



