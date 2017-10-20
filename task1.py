def longest_word(filename):
    with open('Book1.txt', 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word('test.txt'))

def longest_word(filename):
    with open('Book2.txt', 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word('test.txt'))


def longest_word(filename):
    with open('Book3.txt', 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word('test.txt'))


