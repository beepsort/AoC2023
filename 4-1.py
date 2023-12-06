cards = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
cards = cards.splitlines()

with open('4.txt') as f:
    cards = f.readlines()

def parse_card(cardstr):
    cardstr = cardstr.split(':')[1]
    win_nums, have_nums = cardstr.split('|')
    def parse_nums(numstr):
        numstr = numstr.strip()
        return numstr.split(' ')
    win_nums = parse_nums(win_nums)
    have_nums = parse_nums(have_nums)
    win_nums = list(filter(None, win_nums))
    have_nums = list(filter(None, have_nums))
    win_nums = list(map(lambda s: int(s), win_nums))
    have_nums = list(map(lambda s: int(s), have_nums))
    return win_nums, have_nums

cards = list(map(parse_card, cards))

def get_matching_nums(card):
    a = set(card[0])
    b = set(card[1])
    return list(a&b)

card_matches = list(map(get_matching_nums, cards))
print(card_matches)

def calc_score(matches):
    n = len(matches)
    if n == 0:
        return 0
    return 2**(n-1)

card_scores = list(map(calc_score, card_matches))
print(card_scores)
print(sum(card_scores))
