# LÖST

import math

bonusLevels = [0, 25, 50, 75, 150]

C = int(input())

bonusLevel1 = math.floor(C / 2000.0)
bonusLevel1 = min(bonusLevel1, 4)
bonus1 = bonusLevels[bonusLevel1]
C -= 2000 * bonusLevel1

bonusLevel2 = math.floor(C / 2000.0)
bonusLevel2 = min(bonusLevel2, 4)
bonus2 = bonusLevels[bonusLevel2]

totBonus = bonus1 + bonus2
print(totBonus)