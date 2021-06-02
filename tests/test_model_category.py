import sys
import os
sys.path.append(os.getcwd())

from model_category import Category

class TestModelCategory:

    def test_model_categories(self):

        name1 = 'eletronicos'
        description1 = 'favoritos'

        cat = Category(name1, description1)
        cat.name = name1
        cat.description = description1

        assert type(cat) == Category
        assert isinstance(cat, Category)

        assert cat.name == name1
        assert cat.description == description1

        assert isinstance(cat.name, str)
        assert isinstance(cat.description, str)
