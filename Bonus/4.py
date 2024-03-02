# Write your solution for algorithm 4 below
def sort_words_in_string(input_string):
    words = input_string.split()

    sorted_words = sorted(words, key=lambda x: x.lower())

    return sorted_words

# Example usage
input_str = 'I am Laney'
sorted_words = sort_words_in_string(input_str)
print(sorted_words)

