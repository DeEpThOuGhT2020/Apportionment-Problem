from apportionpy.methods.adam import calculate_adam
from apportionpy.methods.hamilton import calculate_hamilton
from apportionpy.methods.jefferson import calculate_jefferson
from apportionpy.methods.webster import calculate_webster
from apportionpy.methods.huntington_hill import calculate_huntington_hill
from apportionpy.methods.equal_proportions import calculate_equal_proportions


class Apportion:
    def __init__(self, seats, populations, method):
        """
        Initialize variables.

        :param seats: Amount of seats to apportion.
        :type seats: int

        :param populations: The populations of each state respectively.
        :type populations: [float]

        :param method: The apportioning method to be used.
        :type method: str
        """

        self.seats = seats
        self.populations = populations
        self.method = method.lower()

        self.initial_fair_shares = None
        self.fair_shares = None
        self.initial_quotas = None
        self.final_quotas = None
        self.initial_divisor = None
        self.modified_divisor = None
        self.initial_geometric_means = None
        self.final_geometric_means = None
        self.divisor_history = None

        if method.upper() == "ADAM":
            self.initial_fair_shares, self.fair_shares, self.initial_quotas, self.final_quotas, \
                self.initial_divisor, self.modified_divisor, self.divisor_history = \
                calculate_adam(self.seats, self.populations)
        elif method.upper() == "HAMILTON":
            self.initial_fair_shares, self.fair_shares, self.initial_quotas, self.final_quotas, \
                self.initial_divisor, self.modified_divisor = calculate_hamilton(self.seats, self.populations)
        elif method.upper() == "JEFFERSON":
            self.initial_fair_shares, self.fair_shares, self.initial_quotas, self.final_quotas, \
                self.initial_divisor, self.modified_divisor, self.divisor_history = \
                calculate_jefferson(self.seats, self.populations)
        elif method.upper() == "WEBSTER":
            self.initial_fair_shares, self.fair_shares, self.initial_quotas, self.final_quotas, \
                self.initial_divisor, self.modified_divisor, self.divisor_history = \
                calculate_webster(self.seats, self.populations)
        elif method.upper() == "HUNTINGTON HILL" or method.upper() == "HHILL":
            self.initial_fair_shares, self.fair_shares, self.initial_quotas, self.final_quotas, \
                self.initial_geometric_means, self.final_geometric_means, self.initial_divisor, self.modified_divisor \
                = calculate_huntington_hill(self.seats, self.populations)
        elif method.upper() == "EQUAL PROPORTIONS" or method.upper() == "EQUAL PROPORTION":
            self.fair_shares = calculate_equal_proportions(self.seats, self.populations)
        else:
            error_message = "\"" + method + "\" is not a valid method."
            raise Exception(error_message)
