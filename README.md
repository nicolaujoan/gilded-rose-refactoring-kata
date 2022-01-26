# gilded-rose-refactoring-kata
Refactoring kata from Emily Bache's coding dojo

This Kata was originally created by Terry Hughes (http://twitter.com/TerryHughes). It is already on GitHub here. See also Bobby Johnson's description of the kata.

I translated the original C# into a few other languages, (with a little help from my friends!), and slightly changed the starting position. This means I've actually done a small amount of refactoring already compared with the original form of the kata, and made it easier to get going with writing tests by giving you one failing unit test to start with. I also added test fixtures for Text-Based approval testing with TextTest (see the TextTests)

As Bobby Johnson points out in his article "Why Most Solutions to Gilded Rose Miss The Bigger Picture", it'll actually give you better practice at handling a legacy code situation if you do this Kata in the original C#. However, I think this kata is also really useful for practicing writing good tests using different frameworks and approaches, and the small changes I've made help with that. I think it's also interesting to compare what the refactored code and tests look like in different programming languages.

I use this kata as part of my work as a technical coach. I wrote a lot about the coaching method I use in this book Technical Agile Coaching with the Samman method. A while back I wrote this article "Writing Good Tests for the Gilded Rose Kata" about how you could use this kata in a coding dojo.

###### This kata has been used for:
- Base our development in a DDD specification done in class
- Don't modify the Item class from gildedRose.py
- remove a mountain of if-else clauses by creating clases and applying common behaviors
- Learn how inheritance works in python
- simulate an interface in python (in this case an informal interface has been used)
- automate the testing process (in test/test_collector.py we are using a class that help us), because the original tests are in test/stdout.gr

#### see GildedRoseRequirements.txt to understand how the magic shop works

