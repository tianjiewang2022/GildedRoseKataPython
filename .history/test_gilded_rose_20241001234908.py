# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    # "Sulfuras, Hand of Ragnaros", being a legendary item, never has to be sold or decreases in Quality
    def test_sulfuras_never_sold_or_decreases_in_quality(self):

        vest = "Sulfuras, Hand of Ragnaros"
        items = [Item(vest, 10, 10)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEquals(9, items[0].sell_in)

    # "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie_increase_in_quality_as_older(self):

        vest = "Aged Brie"
        items = [Item(vest, 20, 20)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEquals(20, items[0].quality)

    # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    # Quality drops to 0 after the concert
    def test_backstage_increase_in_quality_as_sellIn_value_approaches(self):

        vest = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(vest, 10, 2)]
        gr = GildedRose(items)

        gr.update_quality()

        self.assertEquals(3, items[0].quality)


if __name__ == '__main__':
    unittest.main()
