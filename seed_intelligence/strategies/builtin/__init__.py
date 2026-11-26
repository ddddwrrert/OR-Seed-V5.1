from . import s01_universal
from . import s02_structure_aware
from . import s03_difficulty_adaptive
from . import s04_algorithm_instance
from . import s05_failure_driven
from . import s06_randomness_controlled
from . import s07_distribution_aware
from . import s08_instance_relationship
from . import s09_rare_case
from . import s10_operator_complementarity
from . import s11_search_budget
from . import s12_parameter_adaptive
from . import s13_landscape_aware
from . import s14_constraint_aware
from . import s15_generalization_aware

CATALOG = {
    "s01": s01_universal,
    "s02": s02_structure_aware,
    "s03": s03_difficulty_adaptive,
    "s04": s04_algorithm_instance,
    "s05": s05_failure_driven,
    "s06": s06_randomness_controlled,
    "s07": s07_distribution_aware,
    "s08": s08_instance_relationship,
    "s09": s09_rare_case,
    "s10": s10_operator_complementarity,
    "s11": s11_search_budget,
    "s12": s12_parameter_adaptive,
    "s13": s13_landscape_aware,
    "s14": s14_constraint_aware,
    "s15": s15_generalization_aware,
}
