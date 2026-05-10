using System.Linq;
using static System.Console;

int[] input = ReadLine()!.Split().Select(int.Parse).ToArray();
int n = input[0];
int m = input[1];

int[] sol = Enumerable.Repeat(1, n).ToArray();

int numSpikes = n / m;

if (numSpikes * m == n)
{
    WriteLine("NO");
    return;
}

WriteLine("YES");

for (int i = 0; i < numSpikes; i++)
{
    sol[(i + 1) * m - 1] = 1000000;
}

foreach (int val in sol)
{
    WriteLine(val + " ");
}
