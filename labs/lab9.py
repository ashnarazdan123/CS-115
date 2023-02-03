'''Ashna Razdan
CS-115 Lab 9
I pledge my honor that I have abided by the Stevens Honor System.'''

from cs5png import PNGImage

def mult(c,n):
    """ mult uses only a loop and addition  
    to multiply c by the integer n 
    """ 
    result = 0 
    for x in range(n): 
        result = result + c
        n-=1
    return(result)
        
def update(c,n): 
    """ update starts with z=0 and runs z = z**2 + c 
    for a total of n times. It returns the final z.  
    """
    z = 0
    for x in range(n):
        z = z**2 +c
        n-=1
    return (z)

def inMSet(c,n): 
    """ inMSet takes in c for the update step of z = z**2+c 
    n, the maximum number of times to run that step 
    Then, it should return  
    False as soon as abs(z) gets larger than 2 
    True if abs(z) never gets larger than 2 (for n iterations) 
    """ 
    z = 0 + 0j
    for x in range(n):
        z = z**2 +c
        n-=1
        if abs(z)> 2:
            return False
    return True

def weWantThisPixel( col, row ): 
    """ a function that returns True if we want 
        the pixel at col, row and False otherwise 
    """ 
    if col%10 == 0  and  row%10 == 0: 
        return True 
    else: 
        return False 
 
def test(): 
    """ a function to demonstrate how 
        to create and save a png image 
    """ 
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            if weWantThisPixel( col, row ) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile()

#if this was changed then it would return true if either one of the conditions
#were true then as long as the row or column is 0 then it would return 0


