import java.util.Random;

public class Hoeffding
{
	public static int randomint(double min, double max)
	{
		Random rand = new Random();
		double ranval = min + (max - min) * rand.nextDouble();
		int r = (int)(999 * ranval);
		return r;
	}
	public static double randomDouble(double min, double max)
	{
		Random rand = new Random();
		double randomValue = min + (max - min) * rand.nextDouble();
		return randomValue;
	}
	public static void main(String arg[])
	{
		double vavgm = 0.0, vavg1 = 0, vavgr = 0;
		int index = 0;
		int coins[][] = new int[1000][10];
		int count[] = new int[1000];
		for(int trial = 0; trial < 100000; trial++)
		{
			int m = 1000000;
			double c1 = 0;
			double crand = 0;
			double cmin = 0;
			for(int i=0; i<1000; i++)
			{
				for(int j=0; j<10; j++)
				{
					double d = randomDouble(-1.0,1.0);
					if(d >= 0)
					{
						coins[i][j] = 1;
					}	
					else
					{
						coins[i][j] = -1;
					}		
				}
			}
			for(int i=0; i<1000; i++)
				for(int j=0; j<10; j++)
					if(coins[i][j] == 1)
						count[i]++;
			
			int r = randomint(0.0,1.0);
	
			c1 = count[0] / 10;
			crand = count[r] / 10;

			m = count[0];
			for(int i=1; i<10000; i++)
			{
				if(count[i] < m)
					m = count[i];
			}
			cmin = m / 10;
			
			vavgm += cmin;
			vavgr += crand;
			vavg1 += c1;
		}
		vavgm = vavgm / 100000;
		vavgr = vavgr / 100000;
		vavg1 = vavg1 / 100000;
		System.out.println("Average vmin: " + vavgm);
		System.out.println("Average vrandom: " + vavgr);
		System.out.println("Average v1: " + vavg1);
	}
}
