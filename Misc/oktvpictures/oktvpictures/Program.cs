using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oktvpictures
{
    class Program
    {
        struct Guest
        {
            public int arr { get; private set; }
            public int leave { get; private set; }
            public int index { get; private set; }
            public Guest(int arr, int leave, int index)
            {
                this.arr = arr;
                this.leave = leave;
                this.index = index;
            }
        }
        static void Main(string[] args)
        {
            //Read
            int[] header = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();
            int K = header[1];
            List<Guest> guests = new List<Guest>();

            for (int i = 0; i < header[0]; i++)
            {
                int[] tempguest = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();
                guests.Add(new Guest(tempguest[0], tempguest[1], i + 1));
            }

            //Simulate
            int max = guests.Select(x => x.leave).Max();
            List<List<Guest>> photos = new List<List<Guest>>();
            for (int i = 1; i <= max; i++)
            {
                List<Guest> currguests = new List<Guest>();
                foreach (var guest in guests)
                {
                    if (guest.arr <= i && guest.leave >= i)
                    {
                        currguests.Add(guest);
                    }
                }
                if (currguests.Count() >= K)
                {
                    photos.Add(new List<Guest>(currguests));
                    guests.RemoveAll(x => currguests.Contains(x));
                }
            }

            Console.WriteLine(photos.Count());
            foreach (var photo in photos)
            {
                Console.WriteLine(string.Join(" ", photo.Select(x => x.index)));
            }
        }
    }
}
