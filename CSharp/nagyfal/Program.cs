using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BigWall
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] header = Console.ReadLine().Split(' ');
            int n = int.Parse(header[0]);
            int m = int.Parse(header[1]);
            bool[] guards = new bool[n];

            int unuseds = 0;
            for (int i = 0; i < m; i++)
            {
                int x = int.Parse(Console.ReadLine());
                if (guards[x-1] == true)
                {
                    unuseds++;
                }
                guards[x-1] = true;
            }

            //A
            bool[] defendedWalls = new bool[n - 1];
            for (int i = 0; i < n - 1; i++) //Get defended walls 
            {
                defendedWalls[i] = guards[i] && guards[i + 1]; //A wall is defended if both of its neighbouring guard posts are manned
            }

            int defendedN = 0;
            for (int i = 0; i < n - 1; i++)
            {
                if (defendedWalls[i] && (i == n-2 || !defendedWalls[i+1]))
                {
                    defendedN++;
                }
            }

            //B
            bool[] overwatchedWalls = new bool[n - 1];
            for (int i = 0; i < n - 1; i++) //Get overwatched walls 
            {
                overwatchedWalls[i] = guards[i] || guards[i + 1]; //A wall is overwatched if at least one of its neighbouring guard posts are manned
            }

            int overwatchedN = 0;
            for (int i = 0; i < n - 1; i++)
            {
                if (overwatchedWalls[i] && (i == n-2 || !overwatchedWalls[i+1])) 
                {
                    overwatchedN++;
                }
            }

            //C
            int optimalPlaces = 0;
            for (int i = 1; i < n-1; i++)
            {
                if (guards[i-1] && !guards[i] && guards[i+1])
                {
                    optimalPlaces++;
                }
            }

        }
    }
}
