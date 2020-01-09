from random import sample


def still_readable(your_string):
    """
    prints your string with shuffled middle letters of each word in a sentence
    :return: None
    """
    get_str = []
    for word in your_string.split():
        if len(word) > 3:
            get_str.append(word[0] + ''.join(sample([i for i in word[1:-1]], len(word) - 2)) + word[-1])
        else:
            get_str.append(word)
    print(*get_str)  # or you may use  > return ' '.join(words)


still_readable('Здесь должна быть шутка про Штирлица')
