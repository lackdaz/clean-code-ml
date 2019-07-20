import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from src.workshop import *


class TestWorkshop(unittest.TestCase):
    def test_df_should_equal_itself(self):
        df = pd.DataFrame({
          'column 1': [1,2,3]
        })
        assert_frame_equal(df, df)

    def test_impute_nans_should_fail_nans_with_median_value(self):
      df = pd.DataFrame({
        'some_column': [1, np.nan]
      })

      expected = pd.DataFrame({
        'some_column': [1., 1.]
      })
      
      actual = impute_nans(df, columns=["some_column"])

      assert_frame_equal(expected, actual)

    def test_confirm_fail(self):
      assertEquals(1, 2)

