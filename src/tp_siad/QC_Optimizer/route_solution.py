import tp_siad.QC_Optimizer.solution as sol
import tp_siad.QC_Optimizer.fastroute_problem as frp

import logging
import sys

from typing import Any

logger = logging.getLogger(__name__)


class Route(sol.Solution):
    def __init__(self, solvedProblem=frp.FastRouteProb()):
        super(Route, self).__init__()
        self.visit_sequence = []
        self.problem = solvedProblem

    def __str__(self):
        tmp_str = ', '.join([str(i) for i in self.visit_sequence])
        return str(tmp_str)

    def evaluate(self) -> float:
        if self.validate() == False:
            # Pour nous, une solution non réalisable aura une très grande
            # # valeur de fonction objectif.
            # (rappel: nous minimisons l'objectif)
            return sys.float_info.max

        obj_val = 0
        for i in range(0, self.problem.count_locations() - 1):
            crurr_source = self.visit_sequence[i]
            curr_destination = self.visit_sequence[i + 1]
            obj_val = obj_val + self.problem._dist_matrix[crurr_source][curr_destination]

        return obj_val

    def validate(self) -> bool:
        locations_list = list(range(0, self.problem.count_locations()))
        if sorted(self.visit_sequence) == locations_list:
            return True
        return False