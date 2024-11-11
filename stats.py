Python 3.12.3 (main, Sep 11 2024, 14:17:37) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np

    def calculer_statistiques(notes):
        notes = [note for note in notes if 0 <= note <= 20]
        if len(notes) == 0:
            return None
        return {
            "moyenne": np.mean(notes),
            "médiane": np.median(notes),
            "écart_type": np.std(notes)
        }

