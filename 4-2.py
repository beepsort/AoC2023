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

def get_match_count(card):
    a = set(card[0])
    b = set(card[1])
    return len(list(a&b))

card_matches = list(map(get_match_count, cards))
print(card_matches)

num_cards = [1] * len(card_matches)

for i in range(len(cards)-1):
    head = card_matches[i]
    tail = card_matches[i+1:]
    num_cards[i+1:i+1+head] = list(map(lambda x: x+num_cards[i], num_cards[i+1:i+1+head]))

print(sum(num_cards))
