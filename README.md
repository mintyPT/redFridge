#redFridge - mintyPT

##About this

I forked this in first place to learn about python, json, etc.

This is simply a dict{} containing several keys, your products, and an amount, their value.



##How to use this:

1.  load the script:  
*run fridge.py  

2.  pick your fridge:  
*f = fridge()  

3.  open it:  
*f.open()  

4.  use your fridge like a big boy.  


5.  What's next?

    *In your fridge you have:*  
    f.show()  

    If you need to add 6 beers, no problem:  
    fridge.add('Beer',6)  

    If after all you just have 4 beers, just remove 2:  
    f.sub('Beer',2)  

    How many beers do you have after all?  
    f.amountOf('Beer')  
  
    To get rid of everything:  
    f.clear()  

6.  Don't forget to close it after you're done:  
    f.close()  

