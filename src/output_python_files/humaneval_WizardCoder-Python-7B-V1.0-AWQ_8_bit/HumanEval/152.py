def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result


# Test cases
print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,6])) # [0,0,0,0,0,0]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,5])) # [0,0,0,0,1,1]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,7])) # [0,0,0,0,1,1]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,4]) # [0,0,0,0,1,1]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,0]) # [0,0,0,0,1,5]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,-1]) # [0,0,0,0,1,1]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,10]) # [0,0,0,0,1,10]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,-10]) # [0,0,0,0,1,10]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,100]) # [0,0,0,0,1,100]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,-100]) # [0,0,0,0,1,100]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,1000]) # [0,0,0,0,1,100]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,-1000]) # [0,0,0,0,1,100]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,10000]) # [0,0,0,0,1,10000]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,-10000]) #