from random import sample

class Emoji(object):

    food = set([
        'green_apple', 'apple', 'pear', 'tangerine', 'lemon', 'banana',
        'watermelon', 'grapes', 'strawberry', 'melon', 'cherries', 'peach',
        'pineapple', 'tomato', 'eggplant', 'hot_pepper', 'corn', 'sweet_potato',
        'honey_pot', 'bread', 'cheese_wedge', 'poultry_leg', 'meat_on_bone', 'fried_shrimp',
        'egg', 'hamburger', 'fries', 'hotdog', 'pizza', 'spaghetti',
        'taco', 'burrito', 'ramen', 'stew', 'fish_cake', 'sushi',
        'bento', 'curry', 'rice_ball', 'rice', 'rice_cracker', 'oden',
        'dango', 'shaved_ice', 'ice_cream', 'icecream', 'cake', 'birthday',
        'custard', 'candy', 'lollipop', 'chocolate_bar', 'popcorn', 'doughnut',
        'cookie', 'beer', 'beers', 'wine_glass', 'cocktail', 'tropical_drink',
        'champagne', 'sake', 'tea', 'coffee', 'baby_bottle', 'fork_and_knife',
        'knife_fork_plate'
    ])

    def random_food(self):
        return sample(self.food, 1)[0]
