"""
--- Day 5: Supply Stacks ---

--- Part One ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in
stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be
rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or
fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which
crate will end up where, and they want to be ready to unload them as soon as possible, so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input).
For example:

                                                [D]
                                            [N] [C]
                                            [Z] [M] [P]
                                             1   2   3

                                            move 1 from 2 to 1
                                            move 3 from 1 to 3
                                            move 2 from 2 to 1
                                            move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N
is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a
single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack
to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack
1, resulting in this configuration:

                                            [D]
                                            [N] [C]
                                            [Z] [M] [P]
                                             1   2   3

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate
to be moved (D) ends up below the second and third crates:

                                                    [Z]
                                                    [N]
                                                [C] [D]
                                                [M] [P]
                                             1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up
below crate M:

                                                    [Z]
                                                    [N]
                                            [M]     [D]
                                            [C]     [P]
                                             1   2   3

Finally, one crate is moved from stack 1 to stack 2:

                                                    [Z]
                                                    [N]
                                                    [D]
                                            [C] [M] [P]
                                             1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in
stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
import os


def supply_stacks_51(s: str) -> int:
    """

    """

    dir_path = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(dir_path, s)

    with open(txt_file, mode='a') as f:
        f.write("\n\n")

    stacks = [["Z", "N"],
              ["M", "C", "D"],
              ["P"]]

    # stacks = [["N", "D", "M", "Q", "B", "P", "Z"],
    #           ["C", "L", "Z", "Q", "M", "D", "H", "V"],
    #           ["Q", "H", "R", "D", "V", "F", "Z", "G"],
    #           ["H", "G", "D", "F", "N"],
    #           ["N", "F", "Q"],
    #           ["D", "Q", "V", "Z", "F", "B", "T"],
    #           ["Q", "M", "T", "Z", "D", "V", "S", "H"],
    #           ["M", "G", "F", "P", "N", "Q"],
    #           ["B", "W", "R", "M"]]
    top_crates = ''
    orders = []
    with open(txt_file, mode='r') as f:
        for line in f:
            if line[0] == 'm':
                lin = line.split(" ")
                lin[-1] = lin[-1][:-1]
                orders.append(lin)
    for order in orders:
        for i in range(int(order[1])):
            from_stack = int(order[3]) - 1
            crate = stacks[from_stack][-1]
            to_stack = int(order[-1]) - 1
            stacks[to_stack].append(crate)
            stacks[from_stack].pop()
    for stack in stacks:
        top_crates = top_crates + stack[-1]
    return top_crates


# print(supply_stacks_51('test.txt'))
# print(supply_stacks_51('input_day_5.txt'))

"""
Your puzzle answer was QGTHFZBHV. The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.
Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 
9000 - it's a CrateMover 9001. The CrateMover 9001 is notable for many new and exciting features: air conditioning, 
leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

                                            [D]    
                                        [N] [C]    
                                        [Z] [M] [P]
                                         1   2   3 
 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

                                        [D]        
                                        [N] [C]    
                                        [Z] [M] [P]
                                         1   2   3 
 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same 
order, resulting in this new configuration:

                                                [D]
                                                [N]
                                            [C] [Z]
                                            [M] [P]
                                         1   2   3
 
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

                                                [D]
                                                [N]
                                        [C]     [Z]
                                        [M]     [P]
                                         1   2   3
 
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

                                                [D]
                                                [N]
                                                [Z]
                                        [M] [C] [P]
                                         1   2   3
 
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD. 

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to 
be ready to unload the final supplies.

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""


def supply_stacks_52(s: str) -> int:
    """

    """

    dir_path = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(dir_path, s)

    with open(txt_file, mode='a') as f:
        f.write("\n\n")

    # stacks = [["Z", "N"],
    #           ["D", "M", "C", "D"],
    #           ["P"]]

    stacks = [["N", "D", "M", "Q", "B", "P", "Z"],
              ["C", "L", "Z", "Q", "M", "D", "H", "V"],
              ["Q", "H", "R", "D", "V", "F", "Z", "G"],
              ["H", "G", "D", "F", "N"],
              ["N", "F", "Q"],
              ["D", "Q", "V", "Z", "F", "B", "T"],
              ["Q", "M", "T", "Z", "D", "V", "S", "H"],
              ["M", "G", "F", "P", "N", "Q"],
              ["B", "W", "R", "M"]]
    top_crates = ''
    orders = []
    with open(txt_file, mode='r') as f:
        for line in f:
            if line[0] == 'm':
                lin = line.split(" ")
                lin[-1] = lin[-1][:-1]
                orders.append(lin)
    for order in orders:
        if len(stacks[int(order[3])-1]) > 0:
            if int(order[1]) == 1:
                from_stack = int(order[3]) - 1
                crate = stacks[from_stack][len(stacks[from_stack])-1]
                to_stack = int(order[-1]) - 1
                stacks[to_stack].append(crate)
                stacks[from_stack].pop()
            else:
                from_stack = int(order[3]) - 1
                to_stack = int(order[-1]) - 1
                num_stacks = int(order[1])
                for i in range(num_stacks):
                    index_to_remove = len(stacks[from_stack])-int(order[1])+i
                    stack = stacks[from_stack][index_to_remove]
                    stacks[to_stack].append(stack)
                    stacks[from_stack].pop(index_to_remove)
    for stack in stacks:
        top_crates = top_crates + stack[-1]
    return top_crates


# print(supply_stacks_52('test.txt'))
# print(supply_stacks_52('input_day_5.txt'))

"""
Your puzzle answer was MGDMPSZTM. Both parts of this puzzle are complete! They provide two gold stars: **
You are two gold stars closer to collecting enough star fruit. You have completed Day 5!
"""
