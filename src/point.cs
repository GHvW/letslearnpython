
public class Point
{
    private double X { get; }
    private double Y { get; }

    public Point(double x, double y)
    {
        this.X = x;
        this.Y = y;
    }

    public double DistanceTo(Point other)
    {
        return Math.Sqrt(
            Math.Pow(this.X - other.X, 2) + 
            Math.Pow(this.Y - other.Y, 2));
    }
}