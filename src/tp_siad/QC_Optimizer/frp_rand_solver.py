import tp_siad.QC_Optimizer.solver as solver
import tp_siad.QC_Optimizer.fastroute_problem as frp
import tp_siad.QC_Optimizer.route_solution as rsol
import numpy as np

import time
import copy
import logging

logger = logging.getLogger(__name__)

class FrpRandSolver(solver.Solver):
        def __init__(self):
            super(FrpRandSolver, self).__init__()

        def solve(self, prob) -> rsol.Route:
            # Préparer l'exécution
            super(FrpRandSolver, self)._prepare()

            # Créer une première solution à partir du problème
            curr_rsol = rsol.Route(solvedProblem=prob)
            n_locations = curr_rsol.problem.count_locations()
            all_locations = range(0, n_locations)
            curr_rsol.visit_sequence = np.random.permutation(all_locations)
            if(self.verbose > 1):
                logger.info('Solution initiale et objectif:')
                logger.info(str(curr_rsol))
                logger.info(str(curr_rsol.evaluate()))
            # Boucle d'exécution:
            # Algorithme simple qui consiste à générer plusieurs solutions au # hasard pour améliorer la solution courante

            iteration_no = 1
            while(self._continue()):
                if(self.verbose > 1):
                    logger.info('Itération ' + str(iteration_no))

                new_rsol = rsol.Route(solvedProblem=prob)
                new_rsol.visit_sequence = np.random.permutation(all_locations)

                if(self.verbose > 1):
                    logger.info('Solution testée et objectif:')
                    logger.info(str(new_rsol))
                    logger.info(str(new_rsol.evaluate()))

                if new_rsol.evaluate() < curr_rsol.evaluate():
                    curr_rsol = copy.deepcopy(new_rsol)

                if(self.verbose > 0):
                    logger.debug('Meilleure solution courante mise à jour:')
                    logger.info(str(curr_rsol))
                    iteration_no = iteration_no + 1

            # Finaliser l'exécution
            super(FrpRandSolver, self)._terminate()
            # Retourner une solution
            return curr_rsol