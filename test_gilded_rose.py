# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    # The Quality of an item is never negative
    def test_foo_quality_never_negative(self):
        items = [Item("foo", 10, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie_increases_in_quality_as_older(self):
        items = [Item("Aged Brie", -1, 9)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)

    # The Quality of an item is never more than 50
    def test_quality_of_item_never_more_than_50(self):
        items = [Item("foo", 10, 100)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)

    # "Conjured" items degrade in Quality twice as fast as normal items
    def test_conjured_degrade_in_quality_twice_fast_as_normal_items(self):

        vest = "Conjured"
        items = [Item(vest, 10, 5)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(3, items[0].quality)

    def test_conjured_degrade_in_quality_twice_fast_once_sell_by_date_has_passed(self):
        vest = "Conjured"
        items = [Item(vest, -1, 5)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEqual(1, items[0].quality)


if __name__ == '__main__':
    unittest.main()
