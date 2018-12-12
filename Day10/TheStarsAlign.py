# Advent of code 2018
# --- Day 10: The Stars Align ---

import sys

def print_lights(lights):
    x = [x for x,y in lights.keys()]
    y = [y for x,y in lights.keys()]
    minx, maxx = min(x), max(x)
    miny, maxy = min(y), max(y)

    if maxy - miny < 18:
        result = []
        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                result.append("#" if (x, y) in lights else ".")
            result.append('\n')

        return ''.join(result)

    return False


def step(lights):
    return {(x + vx, y + vy): (vx, vy) for (x, y), (vx, vy) in lights.items()}

def parse(line):
    pos, vel = line[10:].strip().split("> velocity=<",)
    posx, posy = [int(i) for i in pos.split(", ")]
    velx, vely = [int(i) for i in vel[:-1].split(", ")]
    return posx, posy, velx, vely

def main():
    lights = {}
    for line in open('day10.txt').readlines():
        posx, posy, velx, vely = parse(line)
        lights[posx, posy] = (velx, vely)

    for i in range(25000):
        result = print_lights(lights)
        if result:
            print(result)
            print(i)
            break

        lights = step(lights)


if __name__ == '__main__':
	main()
