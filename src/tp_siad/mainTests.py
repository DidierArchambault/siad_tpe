import logging, sys

from pathlib import Path

import tp_siad.QC_Optimizer.problem as prob
import tp_siad.QC_Optimizer.solution as solution
import tp_siad.QC_Optimizer.solver as solver
import tp_siad.QC_Optimizer.fastroute_problem as frp
import tp_siad.QC_Optimizer.frp_rand_solver as frprs
import tp_siad.QC_Optimizer.route_solution as rsol


def main():
    # ----- logger config -------
    log_name = "temp_log_name"
    log_dir = Path(__file__).parent / "run_logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{log_name}.jsonl"

    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(log_path, mode="a")

    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    formatter = logging.Formatter(fmt)
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    for h in list(root_logger.handlers):
        root_logger.removeHandler(h)
    root_logger.addHandler(stream_handler)
    root_logger.addHandler(file_handler)

    logger = logging.getLogger(__name__)
    logger.info("Starting run for tests!")
    # ----- logger config -------

    # logger.info('Test des constructeurs des classes de base:')
    # my_prob = prob.Problem()
    # my_sol = solution.Solution()
    # my_solver = solver.Solver()

    # logger.info('\nTest des constructeurs des classes spécialisées:')
    # my_frp = frp.FastRouteProb()
    # my_rsol = rsol.Route()

    # logger.info('\nTest des fonctions d\'une solution:')
    # my_sol.evaluate()
    # my_sol.validate()

    # logger.info('\nTest des fonctions d\'une route:')
    # my_rsol.evaluate()
    # my_rsol.validate()

    # logger.info('\nTest du polymorphisme:')
    # for sol in (my_sol, my_rsol):
    #     sol.evaluate()
    #     sol.validate()

    logger.info('*** Tests FrpProblems ***')
    logger.info('L\'instance devrait s\'afficher:')
    dist_matrix = [[0, 20, 30, 40],
                   [20,  0,  30,  5],
                   [30, 30,   0, 10],
                   [40,  5,  10,  0]]
    frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
    logger.info(str(frp_inst))

    logger.info('*** Tests Route ***')
    logger.info('La solution devrait s\'afficher:')
    curr_rsol = rsol.Route(solvedProblem=frp_inst)
    curr_rsol.visit_sequence = [0, 2, 3]
    logger.info(str(curr_rsol))

    logger.info('count_locations devrait donner 4:')
    dist_matrix = [
        [0, 20, 30, 40],
        [20,  0,  30,  5],
        [30, 30,   0, 10],
        [40,  5,  10,  0]
                   ]
    frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
    logger.info(frp_inst.count_locations())


    logger.info('n_locations devrait être égal à 4:')
    curr_rsol = rsol.Route(solvedProblem=frp_inst)
    n_locations = curr_rsol.problem.count_locations()
    logger.info(n_locations)
    logger.info('La séquence initiale devrait être invalide:')
    logger.info(curr_rsol.validate())
    logger.info('La séquence [0, 2, 3] devrait être invalide:')
    curr_rsol.visit_sequence = [0, 2, 3]
    logger.info(curr_rsol.validate())
    logger.info('La séquence [1, 1, 1, 1] devrait être invalide:')
    curr_rsol.visit_sequence = [1, 1, 1, 1]
    logger.info(curr_rsol.validate())
    logger.info('La séquence [0, 1, 2, 3] devrait être valide:')
    curr_rsol.visit_sequence = [0, 1, 2, 3]
    logger.info(curr_rsol.validate())
    logger.info('La séquence [0, 2, 1, 3] devrait être valide:')
    curr_rsol.visit_sequence = [0, 2, 1, 3]
    logger.info(curr_rsol.validate())
    logger.info('La valeur de la fonction objectif pour [0, 2, 3] devrait être un grand nombre:')
    curr_rsol.visit_sequence = [0, 2, 3]
    logger.info(curr_rsol.evaluate())
    logger.info('La valeur de la fonction objectif pour [0, 2, 1, 3] devrait être 65:')
    curr_rsol.visit_sequence = [0, 2, 1, 3]
    logger.info(curr_rsol.evaluate())

    logger.info('*** Tests frp_rand_solver ***')
    logger.info('Retourne une solution sans afficher de sortie:')
    frp_solver = frprs.FrpRandSolver()
    frp_solver.max_time_sec = 3
    frp_solver.verbose = 0
    frp_sol = frp_solver.solve(frp_inst)
    logger.info('Solution retournée: ' + str(frp_sol))
    logger.info('Objectif: ' + str(frp_sol.evaluate()))


if __name__ == '__main__':
    main()