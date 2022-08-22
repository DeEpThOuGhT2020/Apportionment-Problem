import math


def calculate_equal_proportions(num_seats, populations):
    """
    Calculate final fair shares
    """

    # The number of states to apportion seats to.
    num_states = len(populations)

    # The fair shares per state.
    fair_shares = []
    for _ in range(num_states):
        fair_shares.append(1)

    # Reciprocals of the geometric means per state.
    priority_numbers = []
    for i in range(num_states):
        priority_numbers.append(populations[i] / math.sqrt(fair_shares[i] * (fair_shares[i] + 1)))

    # Stat apportionment.
    while sum(fair_shares) != num_seats:

        # Update the priority numbers.
        for i in range(num_states):
            priority_numbers[i] = (populations[i] / math.sqrt(fair_shares[i] * (fair_shares[i] + 1)))

        # Find the biggest priority number, and give that state another seat.
        highest_priority = max(priority_numbers)
        index = priority_numbers.index(highest_priority)
        fair_shares[index] += 1

    return fair_shares
