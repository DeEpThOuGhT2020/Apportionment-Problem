import math


def estimate_lowest_divisor(method, divisor, populations, seats):
    """
    Calculates the estimated lowest possible divisor.

    :param method: The method used.
    :type method: str

    :param divisor: A working divisor in calculating fair shares.
    :type divisor: float

    :param populations: The populations for each state respectively.
    :type populations: [float]

    :param seats: The amount of seats to apportion.
    :type seats: int

    :return: An estimation of the lowest possible divisor.
    """

    # The number of states to apportion to.
    states = sum(populations)

    # Initialize lists for fair shares and quotas.
    quotas = [0] * states
    fair_shares = [0] * states

    # Keep track of the previous divisor calculated and lowest of them.
    prev_divisor = 0
    lowest_divisor = 0

    # Estimator to use in predicting divisors.
    estimator = 1000000000

    counter = 0
    while counter < 1000:
        for i, population in enumerate(populations):
            if divisor is None or population is None:
                return None
            quotas[i] = population / divisor
            if method.upper() == "ADAM":
                fair_shares[i] = math.ceil(quotas[i])
            elif method.upper() == "WEBSTER":
                fair_shares[i] = round(quotas[i])
            elif method.upper() == "JEFFERSON":
                fair_shares[i] = math.floor(quotas[i])
        if sum(fair_shares) != seats:
            estimator = estimator / 10
            prev_divisor = divisor
            divisor = lowest_divisor - estimator
        else:
            lowest_divisor = divisor
            divisor = prev_divisor - estimator
            if lowest_divisor == divisor:
                break
        counter += 1
    return math.ceil(lowest_divisor * 1000) / 1000


def estimate_highest_divisor(method, divisor, populations, seats):
    """
    Calculates the estimated highest possible divisor.

    :param method: The method used.
    :type method: str

    :param divisor: A working divisor in calculating fair shares.
    :type divisor: float

    :param populations: The populations for each state respectively.
    :type populations: [float]

    :param seats: The amount of seats to apportion.
    :type seats: int

    :return: An estimation of the lowest possible divisor.
    """

    # The number of states to apportion to.
    states = sum(populations)

    # Initialize lists for fair shares and quotas.
    quotas = [0] * states
    fair_shares = [0] * states

    # Keep track of the previous divisor calculated and highest of them.
    prev_divisor = 0
    highest_divisor = 0

    # Estimator to use in predicting divisors.
    estimator = 1000000000

    counter = 0
    while counter < 1000:
        for i, population in enumerate(populations):
            if divisor is None or population is None:
                return None
            quotas[i] = population / divisor
            if method.upper() == "ADAM":
                fair_shares[i] = math.ceil(quotas[i])
            elif method.upper() == "WEBSTER":
                fair_shares[i] = round(quotas[i])
            elif method.upper() == "JEFFERSON":
                fair_shares[i] = math.floor(quotas[i])
        if sum(fair_shares) != seats:
            estimator = estimator / 10
            prev_divisor = divisor
            divisor = highest_divisor + estimator
        else:
            highest_divisor = divisor
            divisor = prev_divisor - estimator
            if highest_divisor == divisor:
                break
        counter += 1
    return math.ceil(highest_divisor * 1000) / 1000
