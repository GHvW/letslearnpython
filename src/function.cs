public static class Function
{
    public static string GenerateGreeting(string kind)
    {
        if (kind == "Texan")
        {
            return "Howdy!";
        }
        else if (kind == "Spanish")
        {
            return "Hola";
        }
        else if (kind == "New Yorker")
        {
            return "";
        }
        else
        {
            return "Hello";
        }
    }

    public static bool IsEven(int it) => it % 2 == 0;

    public static int Add(int x, int y) => x + y;

    public static int Add10(int x) => Add(x, 10);
}