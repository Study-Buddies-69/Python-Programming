import random
import logging


def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x = x + dx
        y = y + dy
    final_location = (x, y)
    # print('Final Location is ({}, {})'.format(x, y))
    return final_location


def abs_distance(final_location):
    absolute_distance = abs(final_location[0]) + abs(final_location[1])
    # print('Distance from home is {}'.format(absolute_distance))
    return absolute_distance


def probability_of_being_within_p_units_from_home_over_1_to_n_steps(p, n, iterations):
    for steps_count in range(n+1):
        success_counter = 0
        for i in range(iterations):
            final_location = random_walk(steps_count)
            absolute_distance = abs_distance(final_location)
            if absolute_distance <= p:
                success_counter += 1
        success_probability = float(success_counter / iterations)
        print("Probability of being within {} units from home after taking "
              "{} steps is {}".format(p, steps_count, success_probability))


probability_of_being_within_p_units_from_home_over_1_to_n_steps(4, 30, 20000)