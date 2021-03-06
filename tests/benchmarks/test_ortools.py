import sys

sys.path.append("../")
from examples.ortools.base_ortools import OrToolsBase
from examples.ortools.vrp import VRP
from examples.ortools.cvrp import CVRP
from examples.ortools.vrptw import VRPTW
from examples.ortools.pdp import PDP
from examples.ortools.cvrpsdc import CVRPSDC

# from examples.ortools.cvrp_drop import Drop


class TestsOrTools:
    def setup(self):
        """
        Examples from the ortools routing library.
        https://developers.google.com/optimization/routing
        """
        self.base = OrToolsBase()

    def test_nodes(self):
        assert len(self.base.G.nodes()) == 18


######
# LP #
######


def test_vrp_subproblem_lp():
    data = VRP()
    data.solve(cspy=False)
    assert int(data.best_value) == 6208


def test_cvrp_subproblem_lp():
    data = CVRP()
    initial_routes = [
        ["Source", 1, 4, 3, 15, "Sink"],
        ["Source", 14, 16, 10, 2, "Sink"],
        ["Source", 7, 13, 12, 11, "Sink"],
        ["Source", 9, 8, 6, 5, "Sink"],
    ]
    data.solve(initial_routes=initial_routes, cspy=False)
    assert int(data.best_value) == 6208


def test_vrptw_subproblem_lp():
    data = VRPTW()
    initial_routes = [
        ["Source", 9, 14, 16, "Sink"],
        ["Source", 7, 1, 4, 3, "Sink"],
        ["Source", 12, 13, 15, 11, "Sink"],
        ["Source", 5, 8, 6, 2, 10, "Sink"],
    ]
    data.solve(initial_routes=initial_routes, cspy=False)
    assert int(data.best_value) == 68


def test_pdp_subproblem_lp():
    data = PDP()
    initial_routes = []
    for pickup_node in data.pickups_deliveries:
        if pickup_node in data.G.nodes():
            initial_routes.append(
                ["Source", pickup_node, data.pickups_deliveries[pickup_node], "Sink",]
            )
    data.solve(initial_routes=initial_routes, cspy=False, pricing_strategy="Exact")
    assert int(data.best_value) == 6916


def test_cvrpsdc_subproblem_lp():
    data = CVRPSDC()
    data.solve(cspy=False, pricing_strategy="Exact")
    assert int(data.best_value) == 6208


"""
def test_cvrp_drop_subproblem_lp(self):
    data = Drop()
    initial_routes = [
        ["Source", 9, 14, 16, "Sink"],
        ["Source", 12, 11, 4, 3, 1, "Sink"],
        ["Source", 7, 13, "Sink"],
        ["Source", 8, 10, 2, 5, "Sink"],
    ]
    data.solve(initial_routes=initial_routes, cspy=False)
    assert int(data.best_value) == 7776
"""


########
# cspy #
########

"""
def test_vrp_subproblem_cspy():
    data = VRP()
    data.solve(cspy=True)
    assert int(data.best_value) == 6208
"""


def test_cvrp_subproblem_cspy():
    data = CVRP()
    initial_routes = [
        ["Source", 1, 4, 3, 15, "Sink"],
        ["Source", 14, 16, 10, 2, "Sink"],
        ["Source", 7, 13, 12, 11, "Sink"],
        ["Source", 9, 8, 6, 5, "Sink"],
    ]
    data.solve(initial_routes=initial_routes, cspy=True)
    assert int(data.best_value) == 6208


def test_vrptw_subproblem_cspy():
    data = VRPTW()
    initial_routes = [
        ["Source", 9, 14, 16, "Sink"],
        ["Source", 7, 1, 4, 3, "Sink"],
        ["Source", 12, 13, 15, 11, "Sink"],
        ["Source", 5, 8, 6, 2, 10, "Sink"],
    ]
    data.solve(initial_routes=initial_routes, cspy=True)
    assert int(data.best_value) == 68


def test_cvrpsdc_subproblem_cspy():
    data = CVRPSDC()
    data.solve(cspy=True, pricing_strategy="Exact")
    assert int(data.best_value) == 6208


"""
def test_cvrp_drop_subproblem_cspy(self):
    data = Drop()
    initial_routes = [
        ["Source", 9, 14, 16, "Sink"],
        ["Source", 12, 11, 4, 3, 1, "Sink"],
        ["Source", 7, 13, "Sink"],
        ["Source", 8, 10, 2, 5, "Sink"],
    ]
    data.solve(initial_routes=initial_routes, cspy=True)
    assert int(data.best_value) == 7776
"""
