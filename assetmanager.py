import os
import pygame


class AssetManager:
    """
    AssetManager class handles all of the sound and image assets for the game.
    """
    def __init__(self, debug):
        """
        Initialize the assets. If we're in debug mode, load the debug assets instead.
        """
        if not debug:
            # Load all the assets into instance variables.
            # For now, do nothing.
            pass

        else:
            # Load all the debug assets.
            self.music      = load_sound("piano-loop2.wav")
            self.highhat    = load_sound("high-hat.wav")
            self.lowtom     = load_sound("low-tom.wav")
            self.snare      = load_sound("snare.wav")
            self.tambourine = load_sound("tambourine.wav")


def load_sound(filename):
    """
    Load the given sound file into memory and return the Sound object.
    There's apparently a bug in pygame.mixer.Sound that doesn't raise an exception
    if it can't find the file. It just assumes its some sort of sound data.
    So that's why I explicitly check if the file exists instead of catching an exception.
    :rtype : pygame.mixer.Sound
    """
    # Get the full path for the file. All assets are in the assets\ directory.
    fullpath = os.path.join("assets", filename)
    if not os.path.isfile(fullpath):
        raise IOError("Could not load file: " + fullpath)

    return pygame.mixer.Sound(fullpath)