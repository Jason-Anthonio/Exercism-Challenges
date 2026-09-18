"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#prevents the use of Magic Numbers(a value that is not known in context of code readers) using constants
EXPECTED_BAKE_TIME = 40 #average time for the bake to finish (in minutes)
PREPARATION_TIME = 2 #average time for a layer to be added to the lasagna (in minutes)

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME` (expected bake time - current/elapsed bake time).
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the time for adding layers of the lasagna

    Parameters:
        number_of_layers (int): The number of layers wanted to add to the lasagna

    Returns:
        int: The total preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers wanted to add to the lasagna as
    an argument and returns how many minutes the layers are prepared for the lasagna 
    based on the `PREPARATION_TIME` (number of layers x preparation time per layer).
    """
    
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing the layers + baking).
    """
    
    return (PREPARATION_TIME * number_of_layers) + elapsed_bake_time
