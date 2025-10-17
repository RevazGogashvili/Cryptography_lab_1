Discussion: Why is Caesar cipher insecure? Where might legacy systems still use
similar encryption?

The Caesar cipher is one of the first encryptions people learn about, but it's completely insecure for protecting real secrets. Why is it so easy to break?
There are two big problems with the Caesar cipher:

There are only 25 guesses. The "key" is just a number from 1 to 25. You can just try every single key, one by one, until the message makes sense. This is called a "brute-force attack," 
and a computer can do it in less than a second. It's like having a bike lock with only 25 possible combinations—it's not going to stop anyone.
It doesn't hide the letter patterns. In English, 'E' is the most common letter. If you have a long coded message, you can just count all the letters. If the letter 'H' shows up the most, 
you can make a good guess that 'H' is the secret code for 'E'. Once you figure that out, you've found the key and can decode the whole message.

So if it's so bad, where is it still used?
Even though it's useless for security, you still see it in a few places where the goal isn't really about keeping secrets.

Hiding Spoilers (ROT13): On websites like Reddit, people use a Caesar cipher with a key of 13 (called ROT13) to hide movie spoilers or puzzle answers. 
It's not meant to be secure; it just stops you from accidentally reading something you don't want to see yet.

Old Technology: Think of a simple machine or a program from the 1980s. It might have used a simple cipher to hide a password in a config file. 
The goal wasn't to stop a real hacker, but just to keep a regular user from easily seeing it in plain text.

Puzzles and Games: It's a fun and simple challenge in video games, online puzzles, and coding competitions. 
It’s often the first step in a bigger puzzle—something easy to solve so you can get to the next stage.

The bottom line is, the Caesar cipher is a great tool for learning about encryption and a fun puzzle, but it’s a terrible tool for keeping real information safe.
