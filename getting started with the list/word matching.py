# Word Matching

def word_matching(word_list, target_word):

    matched_words = []

    for word in word_list:

        if word == target_word:

            matched_words.append(word)

    return matched_words

# Example usage

words = ["apple", "banana", "cherry", "date", "apple", "fig", "grape"]

target = "apple"

result = word_matching(words, target)

print("Matched words:", result)