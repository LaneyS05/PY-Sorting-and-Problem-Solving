def match_nums_with_words(nums, sentence):
    words = sentence.split()

    words_by_length = {}
    for word in words:
        word_length = len(word)
        if word_length not in words_by_length:
            words_by_length[word_length] = [word]
        else:
            words_by_length[word_length].append(word)

    result_pairs = []

    for num in nums:
        if num in words_by_length:
            matching_words = words_by_length[num]
            
            pairs = [(num, word) for word in matching_words]
            
            result_pairs.extend(pairs)

    return result_pairs

words = "I like pizza"
nums = [1, 5, 4, 7]
result = match_nums_with_words(nums, words)
print(result)
