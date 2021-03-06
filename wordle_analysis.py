"""a little wordle analyzing"""

def get_letter_index(letter: str) -> int:
    """get index of letter (a = 0, z = 25)"""
    return ord(letter) - ord("a")

def word_repeats_letters(word: str) -> bool:
    """returns true if a word has repeated letters"""
    return len(set(word)) != len(word)

def absolute_letter_frequency(word_list: list) -> list:
    """returns list of tuples (letter, letter frequency) in order by most used"""
    char_freq = [0] * 26
    for word in word_list:
        for letter in word:
            char_freq[get_letter_index(letter)] += 1

    char_freq = map(lambda x: (chr(x[0] + ord("a")), x[1]), enumerate(char_freq))
    char_freq = sorted(char_freq, key=lambda x: x[1], reverse=True)
    return char_freq

def positional_letter_frequency(word_list: list) -> list:
    """returns a 5 * 26 matrix of which letters appear most frequently in which spaces"""
    ret = [[0 for _ in range(26)] for _ in range(5)]
    for word in word_list:
        for i, letter in enumerate(word):
            ret[i][get_letter_index(letter)] += 1
    return ret

def get_word_rankings(word_list: list, omit_ends_with_s: bool = False, omit_words_with_repeated_letters: bool = False) -> list:
    """get words most likely to have green letters
    returns list of tuples (word, score)"""
    matrix = positional_letter_frequency(word_list)

    if omit_words_with_repeated_letters:
        word_list = list(filter(lambda x: not word_repeats_letters(x), word_list))
    if omit_ends_with_s:
        word_list = list(filter(lambda x: x[4] != "s", word_list))

    scores = []
    for word in word_list:
        score = 0
        for i, letter in enumerate(word):
            score += matrix[i][get_letter_index(letter)]
        scores.append((word, score))
    return sorted(scores, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    with open (r"wordle_words.txt", "r", encoding="UTF-8") as word_file:
        words = word_file.readlines()
        words = list(map(lambda x: x.rstrip().lower(), words))
        words = list(filter(lambda x: len(x) == 5, words))

        word_rankings = get_word_rankings(words,True,True)
        # with open (r"word_rankings.txt", "w", encoding="UTF-8") as rank_file:
        #     for i, word_t in enumerate(word_rankings):
        #         rank_file.write(f"{i + 1}: {word_t[0]} ({word_t[1]})\n")
            