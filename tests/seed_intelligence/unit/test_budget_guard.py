import unittest


from seed_intelligence.budget.budget_controller import eligible
from fixtures import BUDGET, PARENT

class Budget(unittest.TestCase):
    def test_only_paid_special_slots_are_eligible(self):
        self.assertTrue(eligible(PARENT, BUDGET, 0, 1))
        self.assertFalse(eligible(PARENT, BUDGET, 1, 1))
        self.assertFalse(eligible({"fitness": None}, BUDGET, 0, 1))
