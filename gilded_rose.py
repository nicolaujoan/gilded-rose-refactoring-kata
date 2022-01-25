# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, stock):
        self.stock = stock      # GildedRose has-a stock
    
    def updateQuality(self):
        for item in self.stock:
            item.updateQuality()

    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1
    
    def add_item():
        pass


# this class cannot be modified
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# our informal interface
class Updateable():
    def updateQuality(self) -> None:
        """Update the quality of an item"""
        pass



class NormalItem(Item, Updateable):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def getQuality(self) -> int:
        return self.quality
    
    def getSellIn(self) -> int:
        return self.sell_in
    
    def decreaseQuality(self, decrement):
            self.quality -= decrement
    
    def decreaseSellIn(self):
        self.sell_in -= 1

    def updateQuality(self):
        if self.getSellIn() < 0 and self.getQuality() > 1:
            self.decreaseQuality(2)

        if self.getSellIn() >= 0 and self.getQuality() > 0:
            self.decreaseQuality(1)
        
        self.decreaseSellIn()
    


class Sulfuras(Item):
    
    QUALITY = 80

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, Sulfuras.QUALITY)



# inherits from NormalItem because its behaviour is similar (can reuse methods)
class Conjured(NormalItem, Updateable):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def updateQuality(self):
        if self.getSellIn() < 0 and self.getQuality() > 3:
            self.decreaseQuality(4)

        if self.getSellIn() >= 0 and self.getQuality() > 1:
            self.decreaseQuality(2)
            
        self.decreaseSellIn()


class AgedBrie(Item, Updateable):
    
    MAX_QUALITY = 50

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def getQuality(self) -> int:
        return self.quality
    
    def increaseQuality(self, increment):
        self.quality += increment
    
    def getSellIn(self) -> int:
        return self.sell_in
    
    def decreaseSellIn(self):
        self.sell_in -= 1

    def updateQuality(self):
        if self.getQuality() < AgedBrie.MAX_QUALITY and self.getSellIn() > 0:
            self.increaseQuality(1)

        if self.getQuality() < AgedBrie.MAX_QUALITY and self.getSellIn() <= 0:
            self.increaseQuality(2)
            
        self.decreaseSellIn()


class BackstagePass(Item, Updateable):

    MAX_QUALITY = 50

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def getQuality(self) -> int:
        return self.quality
    
    def increaseQuality(self, increment):
        self.quality += increment
    
    def decreaseQuality(self, decrement):
        self.quality -= decrement
    
    def getSellIn(self) -> int:
        return self.sell_in
    
    def decreaseSellIn(self, decrement):
        self.sell_in -= decrement

    def updateQuality(self):
        if self.getSellIn() < 0 and self.getQuality() > 0: 
            self.decreaseQuality(self.getQuality())

        if self.getSellIn() <= 5 and self.getQuality() < (BackstagePass.MAX_QUALITY - 2):
            self.increaseQuality(3)

        if self.getSellIn() <= 10 and self.getQuality() < (BackstagePass.MAX_QUALITY - 1):
            self.increaseQuality(2)
            
        if self.getSellIn() >= 0 and self.getQuality() < BackstagePass.MAX_QUALITY:
            self.increaseQuality(1)

        self.decreaseSellIn(1)