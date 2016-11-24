using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oktvmetro
{
    class Program
    {
        static void Main()
        {
            //Read
            int[] header = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();
            int Ntimes = header[0];
            int Kescalatorl = header[1];
            int Lcapacity = header[2];
            int Mmetrofreq = header[3];
            int[] uparrivers = new int[Ntimes+1]; //
            for (int i = 0; i < header[4]; i++)
            {
                uparrivers[int.Parse(Console.ReadLine())]++;
            }
            int[] metroarrivers = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();

            //Simulate
            int upwaiting = 0;
            int[] escdown = new int[Kescalatorl];
            int downnewwaiting = 0;
            int downwaiting = 0;
            int[] outleft = new int[metroarrivers.Length];
            int leavingwaiting = 0;
            int currmetron = 0;

            for (int i = 0; i < Ntimes + Kescalatorl + Mmetrofreq + 1; i++)
            {
                if (i < Ntimes+1) //passangers can arrive
                    upwaiting += uparrivers[i];

                downnewwaiting = escdown[0];

                for (int j = 0; j < Kescalatorl - 1 ; j++)
                {
                    escdown[j] = escdown[j + 1];
                }
                escdown[Kescalatorl - 1] = 0;

                downwaiting += downnewwaiting;
                downnewwaiting = 0;

                int diff = Math.Min(upwaiting, 2);
                upwaiting -= diff;
                escdown[Kescalatorl - 1] = diff;


                if (i % Mmetrofreq == Mmetrofreq - 1 && i != 1) //metro arrived
                {
                    outleft[currmetron] = downwaiting;
                    leavingwaiting += metroarrivers[currmetron++];
                    downwaiting = 0;
                }
                leavingwaiting -= Math.Min(leavingwaiting, 2);


                if (downnewwaiting + downwaiting + leavingwaiting > Lcapacity)
                    break;
            }

            foreach (var item in outleft)
            {
                Console.WriteLine(item);
            }
        }
    }
}
