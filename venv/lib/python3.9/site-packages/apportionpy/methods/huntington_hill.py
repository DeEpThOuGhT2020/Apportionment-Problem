import math


def calculate_huntington_hill(num_seats, populations):
    """
    Calculate the initial fair shares, final fair shares, initial quotas, final quotas, initial divisor, and modified
    divisor using Huntington Hill's method of apportionment.

    :return: A list of initial fair shares, final fair shares, initial quotas, final quotas, initial geometric means,
    final geometric means, initial divisor, and modified divisor.
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

    # the initial geometric means respectively.
    initial_geometric_means = []

    # Initialize the final geometric means list values.
    final_geometric_means = []

    # calculate initial quotas and geometric means
    for i, quota in enumerate(initial_quotas):
        geo_mean = math.sqrt(math.floor(quota) * (math.floor(quota) + 1))
        initial_geometric_means.append(geo_mean)
        final_geometric_means.append(geo_mean)
        if geo_mean < quota:
            initial_fair_shares.append(int(math.ceil(quota)))
        elif geo_mean > quota:
            initial_fair_shares.append(int(math.floor(quota)))

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
            geo_mean = math.sqrt(math.floor(quota) * (math.floor(quota) + 1))
            final_geometric_means[i] = geo_mean
            if geo_mean < quota:
                final_fair_shares[i] = (int(math.ceil(quota)))
            elif geo_mean > quota:
                final_fair_shares[i] = (int(math.floor(quota)))

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
                geo_mean = math.sqrt(math.floor(quota) * (math.floor(quota) + 1))
                final_geometric_means[i] = geo_mean
                if geo_mean < quota:
                    final_fair_shares[i] = (int(math.ceil(quota)))
                elif geo_mean > quota:
                    final_fair_shares[i] = (int(math.floor(quota)))
        time_keeper += 1

    # If the loop didn't naturally end, return null values.
    if time_keeper == 5000:
        raise Exception("Incalculable values.")

    # Return a list for final fair shares and final quotas.
    else:
        return initial_fair_shares, final_fair_shares, initial_quotas, final_quotas, initial_geometric_means, \
               final_geometric_means, initial_divisor, modified_divisor
