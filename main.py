from blackjack import Blackjack
from spiller import Spiller
from kortstokk import Kortstokk

# Setter opp en kortstokk og starter et spill:
kortstokk = Kortstokk("https://blackjack.labs.nais.io/shuffle")
# Lager et Blackjack-spill og legger til kortstokken:
spill = Blackjack(kortstokk)

# Lager spillere:
ruby = Spiller("Ruby", spill)
marit = Spiller("Marit", spill)

# Starter spillet:
spill.spill(ruby, marit)



