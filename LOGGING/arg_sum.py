import argparse

parser = argparse.ArgumentParser(
    description = 'Sum two intergers')

parser.add_argument(
    '-a', "--a_vlaue",
    dest = "a", help = "A ingegers", type = int, required = True)

parser.add_argument(
    '-b', "--b_vlaue",
    dest = "b", help = "B ingegers", type = int, required = True)

args = parser.parse_args()
print(args)
print(args.a)
print(args.b)
print(args.a + args.b)