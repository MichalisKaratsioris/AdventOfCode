"""
--- Day 6: Tuning Trouble ---

--- Part One ---
The preparations are finally complete; you and the Elves leave camp on foot and begin to make your way toward
the star fruit grove. As you move through the dense undergrowth, one of the Elves gives you a handheld device.
He says that it has many fancy features, but the most important one to set up right now is the communication
system.

However, because he's heard you have significant experience dealing with signal-based systems, he convinced
the other Elves that it would be okay to give you their one malfunctioning device - surely you'll have no
problem fixing it. As if inspired by comedic timing, the device emits a few colorful sparks. To be able to
communicate with the Elves, the device needs to lock on to their signal. The signal is a series of
seemingly-random characters that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet
marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a
sequence of four characters that are all different.

The device will send your subroutine a datastream buffer (your puzzle input); your subroutine needs to identify
the first position where the four most recently received characters were all different. Specifically, it needs
to report the number of characters from the beginning of the buffer to the end of the first such four-character
marker.

For example, suppose you receive the following datastream buffer:

                                        mjqjpqmgbljsphdztnvjfqwrcgsmlb

After the first three characters (mjq) have been received, there haven't been enough characters received yet to
find the marker. The first time a marker could occur is after the fourth character is received, making the most
recent four characters mjqj. Because j is repeated, this isn't a marker.

The first time a marker appears is after the seventh character arrives. Once it does, the last four characters
received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the
first start-of-packet marker is complete after 7 characters have been processed.

Here are a few more examples:

    - bvwbjplbgvbhsrlpgdmjqwftvncz      : first marker after character 5
    - nppdvjthqldpwncqszvftbrmjlhg      : first marker after character 6
    - nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg : first marker after character 10
    - zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw  : first marker after character 11

How many characters need to be processed before the first start-of-packet marker is detected?
"""
import os


def tuning_trouble_61(s: str) -> int:
    """

    """

    dir_path = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(dir_path, s)

    with open(txt_file, mode='a') as f:
        f.write("\n\n")

    # with open(txt_file, mode='r') as f:
    #     for line in f:
    #         for i in range(len(line[:-1]) - 1):
    #             uniques = [line[i]]
    #             for j in range(i + 1, i + 5):
    #                 if not line[j] in uniques:
    #                     uniques.append(line[j])
    #                     if len(uniques) == 4:
    #                         return j+1
    #                 else:
    #                     break
    answers = []
    with open(txt_file, mode='r') as f:
        count = 0
        for line in f:
            count = count + 1
            for i in range(len(line[:-1]) - 1):
                uniques = [line[i]]
                for j in range(i + 1, len(line[:-1])):
                    if not line[j] in uniques:
                        uniques.append(line[j])
                        if len(uniques) == 4:
                            answers.append(j+1)
                    else:
                        break
                if len(answers) == count:
                    break
    return answers


# print(tuning_trouble_61('test.txt'))
# print(tuning_trouble_61('input_day_6.txt'))


"""
Your puzzle answer was 1757. The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it 
also needs to look for messages. A start-of-message marker is just like a start-of-packet marker, except it 
consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

                        mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
                        bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
                        nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
                        nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
                        zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
                        
How many characters need to be processed before the first start-of-message marker is detected?
"""


def tuning_trouble_62(s: str) -> int:
    """

    """

    dir_path = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(dir_path, s)

    with open(txt_file, mode='a') as f:
        f.write("\n\n")

    with open(txt_file, mode='r') as f:
        for line in f:
            for i in range(len(line[:-1]) - 15):
                uniques = [line[i]]
                for j in range(i + 1, i + 15):
                    if not line[j] in uniques:
                        uniques.append(line[j])
                        if len(uniques) == 14:
                            return j+1
                    else:
                        break
    # answers = []
    # with open(txt_file, mode='r') as f:
    #     count = 0
    #     for line in f:
    #         count = count + 1
    #         for i in range(len(line[:-1]) - 1):
    #             uniques = [line[i]]
    #             for j in range(i + 1, len(line[:-1])):
    #                 if not line[j] in uniques:
    #                     uniques.append(line[j])
    #                     if len(uniques) == 14:
    #                         answers.append(j + 1)
    #                 else:
    #                     break
    #             if len(answers) == count:
    #                 break
    # return answers


# print(tuning_trouble_62('test.txt'))
# print(tuning_trouble_62('input_day_6.txt'))

"""
Your puzzle answer was 2950. Both parts of this puzzle are complete! They provide two gold stars: **
You are two gold stars closer to collecting enough star fruit. You have completed Day 6!
"""
