# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shout: yell
yell = 'congratulation'

print(shout(yell))

# Print yell


nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)

print(list(result)[3])