"""a little wordle analyzing"""

def get_letter_index(letter):
    """get index of letter (a = 0, z = 25)"""
    return ord(letter) - ord("a")
def absolute_letter_frequency(word_list):
    """returns list of tuples (letter, letter frequency) in order by most used"""
    char_freq = [0] * 26
    for word in word_list:
        for letter in word:
            char_freq[get_letter_index(letter)] += 1

    char_freq = map(lambda x: (chr(x[0] + ord("a")), x[1]), enumerate(char_freq))
    char_freq = sorted(char_freq, key=lambda x: x[1])[::-1]
    return char_freq
def positional_letter_frequency(word_list):
    """should return a 26 * 5 matrix of which letters appear most frequently in which spaces"""
    ret = [[0 for _ in range(26)] for _ in range(5)]
    for word in word_list:
        for i, letter in enumerate(word):
            ret[i][get_letter_index(letter)] += 1
    return ret
def get_word_rankings(word_list):
    """get words most likely to have green letters
    ranking method:
    assign each word a score
    for a given word its score will be the sum of the number of words that have
        the same letter in the same space
    e.g.
    there are 1560 letters that start with 's'
    there are 176 letters that have 'c' in the second position
    there are 989 letters that have 'o' in the third position
    there are 716 letters that have 'r' in the fourth position
    there are 1519 letters that have 'e' in the fifth position
    so the score for the word "score" is 4960
    """
    matrix = positional_letter_frequency(word_list)
    no_repeated_letter_words = list(filter(lambda x: not word_repeats_letters(x), words))
    scores = []
    for word in no_repeated_letter_words:
        score = 0
        for i, letter in enumerate(word):
            score += matrix[i][get_letter_index(letter)]
        scores.append((word, score))
    return sorted(scores, key=lambda x: x[1])[::-1]
def word_repeats_letters(word):
    """returns if a word has repeated letters"""
    return len(set(word)) != len(word)
if __name__ == "__main__":
    with open (r"wordle_words.txt", "r", encoding="UTF-8") as word_file:
        words = word_file.readlines()
        words = list(map(lambda x: x.rstrip().lower(), words))
        words = list(filter(lambda x: len(x) == 5, words))

        word_rankings = get_word_rankings(words)

        print(word_rankings)
        # with open (r"word_rankings.txt", "w", encoding="UTF-8") as rank_file:
        #     for i, word_t in enumerate(word_rankings):
        #         rank_file.write(f"{i + 1}: {word_t[0]} ({word_t[1]})\n")
            