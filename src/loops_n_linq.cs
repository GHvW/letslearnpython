public static class LoopsNLinq
{
    public static bool IsEven(int it) => it % 2 == 0;

    public static int Add(int x, int y) => x + y;

    public static int Add10(int x) => Add(x, 10);

    public static IEnumerable<int> Forloopyrange(int start, int end)
    {
        foreach (var n in Enumerable.Range(start, end - start))
        {
            if (IsEven(n))
            {
                yield return Add10(n);
            }
        }
    }

    public static IEnumerable<int> Expressionrange(int start, int end) =>
        Enumerable
            .Range(start, end - start)
            .Where(IsEven)
            .Select(Add10);
}