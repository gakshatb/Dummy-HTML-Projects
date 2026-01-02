'''
Letter Partners Game
In a fun game, every letter in English alphabet has a partner. The first thirteen letters of the English alphabet are called pre-partners and the next thirteen letters are called post-partners. That is ‘a’ is the pre-partner and the corressponding post-partner is ‘n’, ‘b’ is the pre-partner and the corressponding post partner is ‘o’ ....‘m’ is the pre-partner and ‘z’ is the post-partner.

In this game, players will be asked to take a lot with a string ‘w’ and they are said to won the game if the following conditions are satisfied by the letters in ‘w’:

(i) The string may be mixed with pre-partners and post-partners but all pre-partners should have a post-partner

(ii) A pre-partner should come before it’s corressponding post-partner

(iii) For a pre-partner that is in position ‘i’ it’s post-partner

(a) Shall come immediately at posititon ‘i+1’

                                                      or

(b) Should come before all corressponding post-partners of pre-partners that is in positions < i and after all corressponding post-partners of pre-partners that is in position > i.

And the player has lost the game otherwise.

For example, if the word in the lot taken is ‘abon’ then the player has won the game. All pre-partners come before the post-partner and condition (iii) is also satisfied as follows:

1) ‘o’ comes immediately after its pre-partner ‘b’, and as per condition (a) of (iii) it is acceptable

2) ‘n’ comes after its prepartner ‘a’ and it comes after the post-partners of pre-partners that has come after ‘a’ and as per condition (b) of (iii) it is acceptable

Whereas if the word in the lot taken is ‘abno’ then the player has lost the game as the post-partener ‘n’ for pre-partner ‘a’ has come before the post-partner of the pre-partner ‘b’, violates condition (iii).

And if the word in the lot is ‘aerfsbon’ then also the player has won

'''
import sys
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m']
list2=['n','o','p','q','r','s','t','u','v','w','x','y','z']
w=input("Enter a word ")
prepartner=prepartner1=[]
postpartner1=postpartner=[]
for i in w:
    if(i in list1):
        prepartner.append(i)
    if(i in list2):
        postpartner.append(i)
for j in prepartner:
    list1index=list1.index(j)
    if(list2[list1index] in postpartner):#testing if all prepartners has postpartners
        pass
    else:
        print("YOU LOST")
        sys.exit()
prepartner1=prepartner
postpartner1=postpartner
for k in prepartner:
    x=prepartner.index(k)
    y=postpartner.index(list2[list1.index(k)])
    if(w.index(prepartner[x])<w.index(postpartner[y])):
        if(w.index(postpartner[y])-w.index(prepartner[x])==1):#testing3a
            prepartner1.pop(x)
            postpartner1.pop(y)
    else:
        print("YOU LOST")
        sys.exit()
postpartner1.reverse()
count=0
for l in prepartner1:
    if(prepartner1.index(l)==postpartner1.index(list2[list1.index(l)])):#testing3b
        count+=1
if(count==len(prepartner1)):
    print("GAME WON")
else:
    print("GAME LOST")

