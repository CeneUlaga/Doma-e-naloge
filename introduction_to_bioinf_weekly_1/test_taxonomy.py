import unittest

from taxonomy import first_differing_major_rank


class TestTaxonomy(unittest.TestCase):

    def test_genus_difference(self):
        lion = [
            ("superkingdom", "Eukaryota"),
            ("phylum", "Chordata"),
            ("class", "Mammalia"),
            ("order", "Carnivora"),
            ("family", "Felidae"),
            ("genus", "Panthera"),
        ]

        cat = [
            ("superkingdom", "Eukaryota"),
            ("phylum", "Chordata"),
            ("class", "Mammalia"),
            ("order", "Carnivora"),
            ("family", "Felidae"),
            ("genus", "Felis"),
        ]

        self.assertEqual(
            first_differing_major_rank(lion, cat),
            ("genus", "Panthera", "Felis")
        )

    def test_family_difference(self):
        dog = [
            ("superkingdom", "Eukaryota"),
            ("phylum", "Chordata"),
            ("class", "Mammalia"),
            ("order", "Carnivora"),
            ("family", "Canidae"),
        ]

        cat = [
            ("superkingdom", "Eukaryota"),
            ("phylum", "Chordata"),
            ("class", "Mammalia"),
            ("order", "Carnivora"),
            ("family", "Felidae"),
        ]

        self.assertEqual(
            first_differing_major_rank(dog, cat),
            ("family", "Canidae", "Felidae")
        )

    def test_order_difference(self):
        human = [
            ("superkingdom", "Eukaryota"),
            ("phylum", "Chordata"),
            ("class", "Mammalia"),
            ("order", "Primates"),
        ]

        rabbit = [
            ("superkingdom", "Eukaryota"),
            ("phylum", "Chordata"),
            ("class", "Mammalia"),
            ("order", "Lagomorpha"),
        ]

        self.assertEqual(
            first_differing_major_rank(human, rabbit),
            ("order", "Primates", "Lagomorpha")
        )


if __name__ == "__main__":
    unittest.main()