```
┌──(kali㉿kali)-[~]
└─$ ssh -p 55453 ctf-player@atlas.picoctf.net
ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: ls
Please enter a valid number.
Enter your guess: 500
Higher! Try again.
Enter your guess: 800
Higher! Try again.
Enter your guess: 900
Higher! Try again.
Enter your guess: 923
Higher! Try again.
Enter your guess: 950

Higher! Try again.
Enter your guess: Please enter a valid number.
Enter your guess: 970
Higher! Try again.
Enter your guess: 990
Higher! Try again.
Enter your guess: 999
Lower! Try again.
Enter your guess: 998
Lower! Try again.
Enter your guess: 997
Congratulations! You guessed the correct number: 997
Here's your flag: picoCTF{g00d_gu355_bee04a2a}
Connection to atlas.picoctf.net closed.
```

Flag:
```
picoCTF{g00d_gu355_bee04a2a}
```