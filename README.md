# Cryptography
Encrypt your message by using two kinds of cryptography methods: **Caesar Cipher** and **Vigenère Cipher**. 

# Caesar Cipher
In cryptography, a [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), 
also known as Caesar's cipher, 
the shift cipher, 
Caesar's code or Caesar shift, 
is one of the simplest and most widely known encryption techniques.

## How does it work?
Here's how it works:</br>
You take your message, 
something like "hello" and then you shift all of the letters by a certain offset. 

For example, if I chose an offset of 3 and a message of "hello", 
I would code my message by shifting each letter 3 places to the left (with respect to the alphabet). </br>
So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". </br>
Then I have my coded message, "ebiil"!

# Vigenère Cipher
The [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) is a method of encrypting alphabetic text by 
using a series of interwoven Caesar ciphers, 
based on the letters of a keyword. It employs a form of polyalphabetic substitution.

## How does it work?
The Vigenère Cipher is a polyalphabetic substitution cipher, 
as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. 
What this means is that opposed to having a single shift 
that is applied to every letter, 
the Vigenère Cipher has a **different shift** for each individual letter. 
The value of the shift for each letter is determined by a given **keyword**.

Consider the message:
```
barry is the spy
```
If we want to code this message, 
first we choose a keyword. For this example, we'll use the keyword
```
dog
```
Now we use the repeat the keyword over and over to generate a *keyword phrase* 
that is the same length as the message we want to code. 
So if we want to code the message "barry is the spy" 
our *keyword phrase* is "dogdo gd ogd ogd". 

Now we are ready to start coding our message. 
We shift the each letter of our message by the place value of the corresponding letter in the keyword phrase, 
assuming that "a" has a place value of 0, 
"b" has a place value of 1, and so forth. 
Remember, the index starts with zero.

So we shift "b", which has an index of 1, 
by the index of "d", which is 3. 
This gives us an place value of 4, which is "e". 
Then continue the trend: we shift "a" by the place value of "o", 
14, and get "o" again, we shift "r" by the place value of "g", 23, and get "x", 
shift the next "r" by 20 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:
```
eoxum ov hnh gvb
```

# Try it yourself
Download the pragram and run it. Play with the cryptography that you are instereted in!


