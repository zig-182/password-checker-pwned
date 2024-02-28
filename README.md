# Description
This Python script allows users to check the security of a password by querying the Have I Been Pwned API, which contains breached passwords. After the script informs the user whether the password they entered has been in a data breach, they can check additional passwords if desired.

## Languages
* Python 

## Brief Notes
I’ve written about cybersecurity within technical products for around 10 years, so I found this project really interesting. In fact, I’ve actually used this password checker before, so to be able to incorporate it into a project was exciting for me. 


For this project, I wanted to learn more about how APIs work and I also wanted to practice googling some similar scripts and leveraging existing code, while refining it and adding parts that I felt could be useful for the user. (I’m told this is one of the most important skill a Developer can have.) The following are features I thought to be useful:
* Provide users with advice on how to enhance their cybersecurity
* Included a loop to give users the options of checking more passwords and leaving the program when they want
* Provide a prompt if the user leaves the password blank (as I did when I was testing it)

**For Fun:** Think of someone you know who might enter their name as a password and see what happens…

```
Enter the password you want to check: donaldtrump
Your password, "donaldtrump", was found 1314 time(s). Change your password as soon as possible to enhance your cybersecurity! If you would like advice on how to choose a suitable password, check out this article: https://support.microsoft.com/en-gb/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb!
```
