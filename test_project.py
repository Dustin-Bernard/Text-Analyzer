from project import clean_text, count_characters, count_words, find_longest_word, find_most_common_word

def test_clean_text():
    assert clean_text("Hello, world!") == "hello  world "

def test_count_characters():
    assert count_characters("Hello world") == 10

def test_count_words():
    assert count_words("Hello world") == 2

def test_find_longest_word():
    assert find_longest_word(["Hey", "world"]) == "world"

def test_find_most_common_word():
    assert find_most_common_word(["Hello", "world", "world"]) == "world"