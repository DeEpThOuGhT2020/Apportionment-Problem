import math


def calculate_adam(num_seats, populations):
    """
    Calculate the initial fair shares, final fair shares, initial quotas, final quotas, initial divisor, and modified
    divisor using Adam's method of apportionment.

    :return: A list of initial fair shares, final fair shares, initial quotas, final quotas, initial divisor, 
    and modified divisor. 
    """

    # Record divisors.
    estimated_divisors = []

    # The number of states to apportion to.
    num_states = len(populations)

    # The initial divisor
    initial_divisor = sum(populations) / num_seats
    estimated_divisors.append(initial_divisor)

    # The original state quotas respectively.
    initial_quotas = []
    for i, population in enumerate(populations):
        initial_quotas.append(population / initial_divisor)

    # The initial state fair shares respectively.
    initial_fair_shares = []
    for i, quota in enumerate(initial_quotas):
        initial_fair_shares.append(math.ceil(quota))

    # Initialize the final quota and original quota list values.
    final_quotas = []

    # Initialize the modified divisor variable.
    # At this point, the modified divisor is the same as the original divisor value.
    modified_divisor = sum(populations) / num_seats

    # Calculate the original quota values.
    # At this point, the final quotas list is the same as the original quotas list.
    for i, population in enumerate(populations):
        final_quotas.append(population / modified_divisor)

    # Initialize the final fair shares list to list of zeros.
    final_fair_shares = [0] * num_states

    # Initialize an estimator to use in changing the quotas if they need to be reapportioned.
    estimator = sum(populations) / num_seats

    # Initialize a time keeper to break from the loop if apportionment is impossible.
    time_keeper = 0

    # Start the apportionment process.
    while sum(final_fair_shares) != num_seats:
        if time_keeper == 5000:
            break
        for i, quota in enumerate(final_quotas):
            final_fair_shares[i] = math.ceil(quota)

        # Recalculate the divisor if the seats are not fully apportioned.
        if sum(final_fair_shares) != num_seats:

            # Increase the modified divisor if it is too little.
            if sum(final_fair_shares) > num_seats:
                modified_divisor += estimator

            # Decrease the modified divisor if it is too high
            else:
                modified_divisor -= estimator

            # Decrease the estimator so the next loop will not result in the previous modified divisor
            estimator = estimator / 2

            # The modified divisor cannot ever be 0 (prevents divide by 0 error)
            if modified_divisor == 0:
                modified_divisor = 1

            # Recalculate the quotas with the updated modified divisor.
            for i, population in enumerate(populations):
                final_quotas[i] = population / modified_divisor

            # Reapportion the seats to states given a set of new quotas.
            for i, quota in enumerate(final_quotas):
                final_fair_shares[i] = math.ceil(quota)

            # Save updated divisor.
            estimated_divisors.append(modified_divisor)

        time_keeper += 1

    # If the loop didn't naturally end, return null values.
    if time_keeper == 5000:
        raise Exception("Incalculable values.")

    # Return a list for final fair shares, final quotas and a value for the modified divisor.
    else:
        return initial_fair_shares, final_fair_shares, initial_quotas, final_quotas, initial_divisor, modified_divisor \
            , estimated_divisors
