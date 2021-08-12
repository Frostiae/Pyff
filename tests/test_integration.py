from flyff import Flyff
import unittest


class IntegrationTestFlyff(unittest.TestCase):
    """
    A test suite for the Flyff Project M data API

    Currently only testing on the item methods because the implementation
    for the other parts of the API (worlds, classes, monsters, skills, NPCs)
    is identical
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.flyff = Flyff()

    def test_all_items(self):
        result = self.flyff.get_all_items()
        self.assertTrue(len(result) > 1)

    def test_item_int(self):
        result = self.flyff.get_item_by_id(3)
        self.assertTrue(result['name']['en'] == 'Layered Boots')

    def test_item_str(self):
        result = self.flyff.get_item_by_id('640')
        self.assertTrue(result['name']['en'] == 'Buff breaker')

    def test_item_invalid(self):
        result = self.flyff.get_item_by_id(-1)
        self.assertTrue(result['statusCode'] == 404)

    def test_items_by_list(self):
        result = self.flyff.get_items_by_ids([3, 640])
        self.assertTrue(result[0]['name']['en'] == 'Layered Boots'
                        and result[1]['name']['en'] == 'Buff breaker')

    def test_items_by_str(self):
        result = self.flyff.get_items_by_ids('3,640')
        self.assertTrue(result[0]['name']['en'] == 'Layered Boots'
                        and result[1]['name']['en'] == 'Buff breaker')

        result = self.flyff.get_items_by_ids('3 640')
        self.assertTrue(result[0]['name']['en'] == 'Layered Boots'
                        and result[1]['name']['en'] == 'Buff breaker')
