'''
Created on 2013-4-2

@author: Cong
'''

def NumberOfQueue(n):
    numbers = [[] for i in xrange(n + 2)]
    for i in xrange(n + 2):
        numbers[i] = [0 for j in xrange(n + 2)]
    for i in xrange(2, n + 2):
        numbers[i][1] = 1
    #for i in xrange(n + 2):    
        #print numbers[i]
        
    for i in xrange(n + 1):
        for j in xrange(1, n + 1):
            if i >= j:
                numbers[i + 1][j + 1] = numbers[i][j + 1] + numbers[i + 1][j]
            else:
                numbers[i + 1][j + 1] = 0
    print numbers[i + 1][j + 1]   
    
    #for i in xrange(n + 2):    
        #print numbers[i] 
    #print numbers


def main():

    NumberOfQueue(3)
    

if __name__ == '__main__':
    main()