import tp_siad.QC_Optimizer.problem as prob
import tp_siad.QC_Optimizer.solution as sol

import logging
import time

logger = logging.getLogger(__name__)

class Solver:
    def __init__(self, max_time_sec=10):
        self.max_time_sec = max_time_sec
        self._last_run_start = 0
        self._last_run_end = 0
        self.verbose = 1
        logger.info('Solver::init')

    def _prepare(self):
    # Initialiser tous les attributs pour l'exécution self._last_run_sec = 0
    # Démarrer le chronomètre
        self._last_run_start = time.time()

    def _continue(self):
        elapsed_time = time.time() - self._last_run_start
        if elapsed_time <= self.max_time_sec:
            return True
        return False

    def _terminate(self):
    # Arrêter le chronomètre et calculer le temps utilisé self._last_run_end = time.time()
        self._last_run_sec = self._last_run_end - self._last_run_start

    def solve(self, prob=None): # Préparer l'exécution self._prepare()
        # Boucle d'exécution
        while(self._continue()):
    # TODO Coder la boucle d'exécution ici à la place de pass pass
        # Finaliser l'exécution
            self._terminate()

    # Retourner une solution
    # TODO Le code ci-dessous est un code temporaire return solution.Solution()