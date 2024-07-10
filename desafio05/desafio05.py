

def timeInWords(h, m):
    numbers_to_words = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
        23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven',
        28: 'twenty eight', 29: 'twenty nine', 30: 'half'
    }

    if m == 0:
        return f"{numbers_to_words[h]} o' clock"
    elif m <= 30:
        if m == 15 or m == 30:
            return f"{numbers_to_words[m]} past {numbers_to_words[h]}"
        elif m == 1:
            return f"{numbers_to_words[m]} minute past {numbers_to_words[h]}"
        else:
            return f"{numbers_to_words[m]} minutes past {numbers_to_words[h]}"
    else:
        m = 60 - m
        h = h + 1 if h < 12 else 1
        if m == 15:
            return f"{numbers_to_words[m]} to {numbers_to_words[h]}"
        elif m == 1:
            return f"{numbers_to_words[m]} minute to {numbers_to_words[h]}"
        else:
            return f"{numbers_to_words[m]} minutes to {numbers_to_words[h]}"

# Exemplos de uso
print(timeInWords(5, 0))    # Output: "five o' clock"
print(timeInWords(5, 1))    # Output: "one minute past five"
print(timeInWords(5, 10))   # Output: "ten minutes past five"
print(timeInWords(5, 15))   # Output: "quarter past five"
print(timeInWords(5, 28))   # Output: "twenty eight minutes past five"
print(timeInWords(5, 30))   # Output: "half past five"
print(timeInWords(5, 40))   # Output: "twenty minutes to six"
print(timeInWords(5, 45))   # Output: "quarter to six"
print(timeInWords(5, 47))   # Output: "thirteen minutes to six"
print(timeInWords(11, 59))   # Output: "one minute to twelve"
print(timeInWords(10, 8))   # Output: "eight minutes past ten"
print(timeInWords(6, 31))   # Output: "twenty nine minutes to seven"
print(timeInWords(12, 33))   # Output: "twenty seven minutes to one"

