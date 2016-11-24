using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OKTVGameBoard
{
    static class Program
    {
        static void Main(string[] args)
        {
            //Read
            Console.ReadLine();
            List<int> moves = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToList();

            //Compute
            for (int i = 0; i < moves.Count; i++)
            {
                switch (moves[i])
                {
                    case 3:
                        moves.RemoveAt(i);
                        moves.RemoveAt(i - 1);
                        i -= 2;
                        break;

                    case 4:
                        moves.RemoveAt(i);
                        i--;
                        for (int j = i; j >= 0; j--)
                        {
                            if (moves[j] == 0)
                            {
                                moves[j] = 2;
                            }
                            else if (moves[j] == 1)
                            {
                                moves[j] = 0;
                                break;
                            }
                            else if (moves[j] == 2)
                            {
                                moves[j] = 1;
                                break;
                            }
                        }
                        break;

                    case 5:
                        moves.RemoveAt(i);
                        i--;

                        for (int j = i; j >= 0; j--)
                        {
                            if (moves[j] == 0)
                            {
                                moves[j] = 1;
                                break;
                            }
                            else if (moves[j] == 1)
                            {
                                moves[j] = 2;
                                break;
                            }
                            else if (moves[j] == 2)
                            {
                                moves[j] = 0;
                            }
                        }
                        break;

                    default:
                        break;
                }
            }

            //Write
            Console.WriteLine(string.Join(" ", moves));
        }
    }
}