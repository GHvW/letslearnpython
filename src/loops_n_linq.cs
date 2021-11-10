public static class LoopsNLinq
{
    public static IEnumerable<int> Forloopyrange(int start, int end)
    {
        foreach (var n in Enumerable.Range(start, end - start))
        {
            if (Function.IsEven(n))
            {
                yield return Function.Add10(n);
            }
        }
    }

    public static IEnumerable<int> Expressionrange(int start, int end) =>
        Forloopyrange(start, end)
            .Where(Function.IsEven)
            .Select(Function.Add10);
}