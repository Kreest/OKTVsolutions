using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OKTVFazekas
{
    class Program
    {
        struct craft
        {
            public uint session; //menet
            public bool furnace; //kemence

            public craft(uint session, bool furnace)
            {
                this.session = session;
                this.furnace = furnace;
            }
        }

        struct helper
        {
            public int index;
            public int value;

            public helper(int index, int value)
            {
                this.index = index;
                this.value = value;
            }
        }

        static void Main(string[] args)
        {
            //Read
            int k = int.Parse(Console.ReadLine().Split(' ')[1]);
            int[] times = Console.ReadLine().Split(' ').Select(x => int.Parse(x)).ToArray(); //idok

            //Setup
            craft[] result = new craft[times.Length]; //termekek

            //Dynamic stuff
            int[] maxTimes = new int[times.Length];
            for (int i = 0; i < times.Length; i++)
            {
                maxTimes[i] = int.MaxValue;
            }  //Set every value of maxTimes to int.MaxValue
            result[0] = new craft(1, false);

            for (int i = 0; i < times.Length-1; i++) //Iterate through each element of the list, except for the second and last one, wich cannot start a session
            {
                if (i == 1) continue; //rubberband
                for (int j = i+1; j < Math.Min(2*k+i, times.Length); j++) //Loop through every subsequence from i up to 2k length (OR stop at the last element)
                {
                    helper[] subArray = new helper[j-i+1];
                    for (int z = i; z <= j; z++) //Fill the dictionary from the crafts from i to j
                    {
                        subArray[z-i] = new helper(z, times[z]);
                    }
                    subArray = subArray.OrderBy(x => x.value).ToArray(); //order the items by their smelting time

                    int time = subArray[subArray.Length - 1].value + subArray[Math.Max(subArray.Length - k - 1, 0)].value + (i == 0 ? 0 : maxTimes[i - 1]);
                    if (time < maxTimes[j])
                    {
                        maxTimes[j] = time;
                        for (int z = i; z < subArray.Length + i; z++) 
                        {
                            if (i < 2)
                            {
                                result[z].session = 1;
                            }
                            else
                            {
                                result[z].session = result[i - 2].session + 1; 
                            }
                        } 
                    }
                }
            }

            //Write
            Console.WriteLine(maxTimes[maxTimes.Length - 1]);
            foreach (var item in result)
            {
                Console.WriteLine(item.session + " " + (item.furnace ? "2" : "1"));
            }
        }
    }
}
