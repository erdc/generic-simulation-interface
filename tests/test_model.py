import unittest
from genesis.model import Model
import holoviews.plotting.bokeh
import geoviews.plotting.bokeh


class TestMain(unittest.TestCase):

    def test_model_instantiation(self):
        model_object = Model()

        self.assertIsInstance(model_object, Model)

