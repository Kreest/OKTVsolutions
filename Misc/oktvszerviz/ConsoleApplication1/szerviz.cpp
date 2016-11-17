#include <iostream>
#include <cstdio>

using namespace std;

int n, m;

int tip[1005];
int el[200005], mut[200005], pont[1005];
int sor[1005];
int mennyi[4];
int megfelel[4];

int main()
{
	FILE *in = fopen("szerviz.be", "r");
	FILE *out = fopen("szerviz.ki", "w");
	fscanf(in, "%d%d", &n, &m);
	for (int i = 1; i <= n; i++) { pont[i] = 0; tip[i] = -1; }
	for (int i = 1; i <= m; i++)
	{
		int a, b; fscanf(in, "%d%d", &a, &b);

		el[2 * i - 1] = b;
		mut[2 * i - 1] = pont[a]; pont[a] = 2 * i - 1;

		el[2 * i] = a;
		mut[2 * i] = pont[b]; pont[b] = 2 * i;
	}

	int sk = 1; int sv = 1;
	sor[1] = 1; tip[1] = 0;
	mennyi[0] = 0; mennyi[1] = 0; mennyi[2] = 0;
	megfelel[0] = 0; megfelel[1] = 0; megfelel[2] = 0;

	while (sk <= sv)
	{
		int akt = sor[sk++];
		mennyi[tip[akt]]++;
		int ujtip = (tip[akt] + 1) % 3;


		int mm = pont[akt];
		while (mm>0)
		{
			if (tip[el[mm]] == -1)
			{
				tip[el[mm]] = ujtip;
				sor[++sv] = el[mm];
			}
			mm = mut[mm];
		}

	}

	int lj = 0;
	if (mennyi[1]>mennyi[lj]) lj = 1;
	if (mennyi[2]>mennyi[lj]) lj = 2;

	int db1 = 0; int db2 = 0;

	bool van = false;

	for (int i = 0; i<3; i++)
	{
		if (lj != i)
		{
			if (!van)
			{
				megfelel[i] = 1;
				van = true;
				db1 = mennyi[i];
			}
			else
			{
				megfelel[i] = 2;
				db2 = mennyi[i];
			}
		}
	}

	//printf("%d %d %d\n", mennyi[0], mennyi[1], mennyi[2]);
	//printf("%d %d %d\n", megfelel[0], megfelel[1], megfelel[2]);


	fprintf(out, "%d ", db1); for (int i = 1; i <= n; i++) if (megfelel[tip[i]] == 1) fprintf(out, "%d ", i); fprintf(out, "\n");
	fprintf(out, "%d ", db2); for (int i = 1; i <= n; i++) if (megfelel[tip[i]] == 2) fprintf(out, "%d ", i); fprintf(out, "\n");

	return 0;
}
