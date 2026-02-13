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

    dist_matrix = [[0, 20, 30, 40], [20, 0, 30, 5], [30, 30, 0, 10], [40, 5, 10, 0]]
    frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
    # Run
    logger.info('Problème actuel:')
    logger.info(str(frp_inst))
    logger.info('Résoudre le problème...')

    frp_solver = frprs.FrpRandSolver()
    frp_sol = frp_solver.solve(frp_inst)
    logger.info('Solution retournée:')
    logger.info(str(frp_sol))
    logger.info(str(frp_sol.evaluate()))


if __name__ == '__main__':
    main()