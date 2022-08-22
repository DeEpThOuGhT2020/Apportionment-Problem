import math


def calculate_hamilton(num_seats, populations):
    """
    Calculate the initial fair shares, final fair shares, initial quotas, final quotas, initial divisor, and modified
    divisor using Hamilton's method of apportionment.

    :return: A list of initial fair shares, final fair shares, initial quotas, final quotas, initial divisor,
    and modified divisor.
    """

    # The number of states to apportion seats to.
    num_states = len(populations)

    # The original divisor.
    initial_divisor = sum(populations) / num_seats

    # The original state quotas respectively.
    initial_quotas = []
    for i, population in enumerate(populations):
        initial_quotas.append(population / initial_divisor)

    # The initial state fair shares respectively.
    initial_fair_shares = []
    for i, quota in enumerate(initial_quotas):
        initial_fair_shares.append(math.floor(quota))

    # Initialize the final quota and original quota list values.
    final_quotas = []

    decimal_list = []

    # Initialize the modified divisor variable.
    # At this point, the modified divisor is the same as the original divisor value.
    modified_divisor = sum(populations) / num_seats

    # Calculate the original quota values.
    # At this point, the final quotas list is the same as the original quotas list.
    for i, population in enumerate(populations):
        final_quotas.append(population / modified_divisor)
        decimal_list.append(math.modf(population / initial_divisor)[0])

    # Initialize the final fair shares list to list of zeros.
    final_fair_shares = [0] * num_states

    # Calculate the original quota values.
    # At this point, the final quotas list is the same as the original quotas list.
    for i, quota in enumerate(initial_quotas):
        final_fair_shares[i] = math.floor(quota)

    # Initialize a time keeper to break from the loop if apportionment is impossible.
    time_keeper = 0

    # Start the apportionment process.
    while sum(final_fair_shares) != num_seats:
        if time_keeper == 5000:
            break
        if sum(final_fair_shares) != num_seats:
            highest_decimal = max(decimal_list)
            index = decimal_list.index(highest_decimal)
            final_fair_shares[index] += 1
            decimal_list[index] = 0
        time_keeper += 1

    # If the loop didn't naturally end, return null values.
    if time_keeper == 5000:
        raise Exception("Incalculable values.")

    # Return a list for final fair shares and final quotas.
    else:
        return initial_fair_shares, final_fair_shares, initial_quotas, final_quotas, initial_divisor, modified_divisor
