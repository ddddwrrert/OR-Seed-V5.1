import unittest


from seed_intelligence.discovery.bottleneck_discovery import opportunities
from fixtures import CHILD, PARENT, contrasted

class Discovery(unittest.TestCase):
    def test_paired_recovery_is_a_strict_value_gate(self):
        records = contrasted()
        self.assertEqual(len(opportunities([CHILD], PARENT, records, 9)), 1)
        self.assertEqual(opportunities([CHILD], PARENT, records, 10), [])
