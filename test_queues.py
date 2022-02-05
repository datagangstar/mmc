import math
from unittest import TestCase

from queues import is_valid

class Test(TestCase):

    def test_nonnumeric(self):
        self.assertTrue(math.isnan(is_valid(5,"test",1)))


    # def test_is_valid(self):
    #     #self.fail()
    #
    # def test_is_feasible(self):
    #     self.fail()
    #
    # def test_calc_p0(self):
    #     self.fail()
    #
    # def test_calc_lq_mmc(self):
    #     self.fail()
    #
    # def test_calc_bk_mmc(self):
    #     self.fail()
    #
    # def test_calc_wqk_mmc(self):
    #     self.fail()
    #
    # def test_calc_lqk_mmc(self):
    #     self.fail()
    #
    # def test_use_littles_law(self):
    #     self.fail()