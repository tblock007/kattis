using System;

public class Program
{  

    public static void Main()
    {
        string[] tokens = Console.ReadLine().Split();
        int q = int.Parse(tokens[1]);

        int[] c = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        for (int i = 0; i < q; i += 1)
        {
            tokens = Console.ReadLine().Split();
            int a = int.Parse(tokens[1]);
            int b = int.Parse(tokens[2]);

            if (tokens[0] == "1")
            {
                c[a - 1] = b;
            }
            else if (tokens[0] == "2")
            {
                Console.WriteLine(Math.Abs(c[a - 1] - c[b - 1]));
            }
        }
    }
}
