# Day 1 Solution - GitStreak

def count_vowels(text: str) -> int:
    """Returns the count of vowels in text."""
    return sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == '__main__':
    assert count_vowels('hello') == 2
    assert count_vowels('GitStreak') == 3
    print('All tests passed!')
