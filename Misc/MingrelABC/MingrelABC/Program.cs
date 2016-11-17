using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MingrelABC
{
    class Program
    {
        public struct Link
        {
            public char a, b;

            public Link(char a, char b)
            {
                this.a = a;
                this.b = b;
            }
        }
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            string[] words = new string[n];
            List<Link> links = new List<Link>();
            for (int i = 0; i < n; i++)
            {
                words[i] = Console.ReadLine();
            }
            links = GetLinks(words);
            foreach (Link link in links)
            {
                Console.WriteLine(link.a + "-" + link.b);
            }
            int Nuberofthingies = links.Count(x => x.a == 'a');
            Console.WriteLine(Nuberofthingies);
            Console.ReadKey();
        }

        public static List<Link> GetLinks(string[] words)
        {
            List<Link> links = new List<Link>();
            for (int i = 0; i < words.Length-1; i++)
            {
                int n = 0;
                while(words[i][n] == words[i+1][n])
                {
                    n++;
                }

                links.Add(new Link(words[i][n], words[i + 1][n]));
            }
            return links;
        }
    }
}
