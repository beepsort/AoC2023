from dataclasses import dataclass
from typing import List

lines= """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lines = lines.splitlines()

with open('2.txt') as f:
    lines = f.readlines()

@dataclass
class CubeDraw:
    red: int = 0
    green: int = 0
    blue: int = 0

@dataclass
class CubeGame:
    id: int
    draws: List[CubeDraw]

    def is_possible(self, r, g, b):
        for draw in self.draws:
            if r<draw.red or g<draw.green or b<draw.blue:
                print("Game Impossible: " + str(draw))
                return False
        return True

def parse_game(line):
    def parse_single_draw(draw_line):
        color_count = draw_line.split(',')
        draw = CubeDraw()
        for cstr in color_count:
            cstr = cstr.strip()
            (n, color) = cstr.split(' ', 1)
            color = color.lower()
            if color == "red":
                draw.red += int(n)
            if color == "green":
                draw.green += int(n)
            if color == "blue":
                draw.blue += int(n)
        return draw
    (game_id, game_draws) = line.split(':', 1)
    game_id = int(game_id.split(' ', 1)[1])
    game_draws = game_draws.split(';')
    game_draws = list(map(parse_single_draw, game_draws))
    return CubeGame(game_id, game_draws)

games = list(map(parse_game, lines))
games_possible = list(filter(lambda g: g.is_possible(12, 13, 14), games))
games_possible = list(map(lambda g: g.id, games_possible))
print(games_possible)
print(sum(games_possible))
