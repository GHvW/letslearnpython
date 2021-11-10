

IEnumerable<B> Select<A, B>(Func<A, B> fn, IEnumerable<A> items) =>
    items.Select(fn);

var result = Select(x => {
    var y = 100;
    return x * y;
}, new List<int>() { 1, 2, 3, 4, 5 });

var printable = string.Join(", ", result.ToList());

Console.WriteLine(printable);