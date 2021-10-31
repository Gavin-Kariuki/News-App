import unittest
from app.models import Article


class ArticlesTest(unittest.TestCase):

    def setUp(self):
        self.new_article = Article(
            'oya', 'bazu', 'nakucheki', 'hey', 'https://123movies', '', '2021', 'choomba')

    def test_instance(self):

        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()
