using System;
using static System.Console;

int[] bonusLevels = [0, 25, 50, 75, 150];

int c = int.Parse(ReadLine()!);

int bonusLevel1 = Math.Min(c / 2000, 4);
int bonus1 = bonusLevels[bonusLevel1];
c -= 2000 * bonusLevel1;

int bonusLevel2 = Math.Min(c / 2000, 4);
int bonus2 = bonusLevels[bonusLevel2];

WriteLine(bonus1 + bonus2);
