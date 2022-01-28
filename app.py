from gilded_rose import *

# create our monthly stock
stock = GildedRose(
    [
        NormalItem("+5 Dexterity Vest", 10, 20),
        AgedBrie("Aged Brie", 2, 0),
        NormalItem("Elixir of the Mongoose", 5, 7),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Conjured("Conjured Mana Cake", 3, 6)

    ]
)

# update the quality of every item in the stock (every day of the month)
for day in range(1, 31):
    stock.updateQuality()