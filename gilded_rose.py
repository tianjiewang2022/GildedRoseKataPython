# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    # update_backstage_quality
    # -----
    # Parameter:
    #   item: Item
    # Return:
    #   None
    # -------
    # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    # Quality drops to 0 after the concert

    def update_backstage_quality(self, item: Item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1

    # check_validation
    # -----
    # Parameter:
    #   item: Item
    # Return:
    #   None
    # -------
    # The Quality of an item is never negative
    # The Quality of an item is never more than 50

    def check_validation(self, item: Item):
        if item.quality <= 0:
            item.quality = 0
        if item.quality > 50:
            item.quality = 50

    # update_quality_once_sell_date_passed
    # -----
    # Parameter:
    #   item: Item
    # Return:
    #   None
    # -------
    # Once the sell by date has passed, Quality degrades twice as fast
    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    # "Conjured" items degrade in Quality twice as fast as normal items

    def update_quality_once_sell_date_passed(self, item: Item):
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                        if item.name == "Conjured":
                            item.quality = max(0, item.quality - 1)
                else:
                    item.quality = item.quality - item.quality

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
                    if item.name == "Conjured":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    self.update_backstage_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            self.update_quality_once_sell_date_passed(item)
            self.check_validation(item)
