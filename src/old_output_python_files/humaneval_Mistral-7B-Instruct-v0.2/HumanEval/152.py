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
        result.append(abs(game[i]-guess[i]))
    return result

# test
game = [1,2,3,4,5,1]
guess = [1,2,3,4,2,-2]
print(compare(game,guess))

game = [0,5,0,0,0,4]
guess = [4,1,1,0,0,-2]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,1]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [2,2,2,2,2,2]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,2,1,1,1,1]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,2,1]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,3]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,0]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,4]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,5]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,6]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,7]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,8]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,9]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,10]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,1,11]
print(compare(game,guess))

game = [1,1,1,1,1,1]
guess = [1,1,1,1,