def get_hidden_card(card_number, stars_count=4):
    visible_digits_line = card_number[-4:]
    return f"{'*' * stars_count}{str(visible_digits_line)}"


def trim_and_repeat(text, offset=0, repetitions=1):
    return f"{text[offset:] * repetitions}"


def is_international_phone(phone_number):
    first_symbol = phone_number[0]
    return first_symbol == '+'


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def is_palindrome(text):
    text_lower = text.lower()
    return text_lower == text_lower[::-1]


def is_not_palindrome(text):
    return not is_palindrome(text)


def string_or_not(text):
    answer = isinstance(text, str) and 'yes' or 'no'
    return print(answer)


def guess_number(number):
    if number == 42:
        return 'You win!'
    return 'Try again!'


def normalize_url(url):
    url = str(url)
    if url[:8] == 'https://':
        return url
    else:
        if url[:7] == 'http://':
            return 'https://' + url[7:]
    return 'https://' + url


def who_is_this_house_to_starks(family):
    if family == 'Karstark' or family == 'Tully':
        return 'friend'
    elif family == 'Lannister' or family == 'Frey':
        return 'enemy'
    return 'neutral'


def flip_flop(string):
    return 'flop' if string == 'flip' else 'flip'


def print_numbers(i):
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')


def multiply_numbers_from_range(start, finish):
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result


def join_numbers_from_range(start, finish):
    result = ''
    i = start
    while i <= finish:
        result = result + str(start)
        start = start + 1
        i = i + 1

    return result


def print_reversed_word_by_symbol(text):
    i = len(text) - 1
    while i >= 0:
        print(text[i])
        i -= 1


def count_chars(string, char):
    index = 0
    count = 0
    lower_string = string.lower()
    lower_char = char.lower()
    while index < len(string):
        if lower_string[index] == lower_char:
            count = count + 1
        index = index + 1
    return count


def my_substr(string, number):
    index = 0
    slice_string = ''
    while index <= number - 1:
        slice_string = slice_string + string[index]
        index += 1

    return slice_string


def is_arguments_for_substr_correct(string, index, length):
    slice_string = ''
    max_legth = len(string) - index
    if length < 0:
        return False
    elif index < 0:
        return False
    elif index >= len(string):
        return False
    elif length > max_legth:
        return False
    while len(slice_string) != length:
        slice_string = slice_string + string[index]
        index += 1
    return True


# def filter_string(string, char):
#     index = 0
#     total_string = ''
#     while index < len(string):
#         current_char = string[index]
#         if current_char != char:
#            total_string = total_string + current_char
#         index += 1
#     return total_string

def filter_string(string, char):
    total_string = ''
    for current_char in string:
        if current_char.lower() != char.lower():
            total_string = total_string + current_char
    return total_string


def is_contains_char(line, char):
    i = 0
    while i < len(line):
        current_char = line[i]
        if current_char == char:
            return True
        i += 1
    return False


def twoSum(nums, target):
    s = 0
    ind = []
    while len(ind) != 2:
        for i in range(len(nums) // 2):
            for j in range(len(nums)-1, len(nums)//2-1, -1):
                print('i=', i, 'j=', j)
                if i != j:
                    s = nums[i] + nums[j]
                    if s == target:
                        ind.append(i)
                        ind.append(j)
                    else:
                        s = 0
            if len(ind) == 2:
                break

            for j in range(len(nums)//2):
                print('i=', i, 'j=', j)
                if i != j:
                    s = nums[i] + nums[j]
                    if s == target:
                        ind.append(i)
                        ind.append(j)
                    else:
                        s = 0
    return ind


nums = [2, 7, 11, 15, 2, 3, 4, 5, 6, 33, 3]
target = 9
print(twoSum(nums, target))
