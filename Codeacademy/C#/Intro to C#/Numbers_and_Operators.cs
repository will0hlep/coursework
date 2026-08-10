//part 1:2
using System;

namespace Numbers
{
  class Program
  {
    static void Main(string[] args)
    {
      // Number of pizza shops
      int pizzaShops = 4332;

      // Number of employees
      int totalEmployees = 86928;

      // Revenue
      decimal revenue = 390819.28m;

      // Log the values to the console:
      Console.WriteLine(pizzaShops);
      Console.WriteLine(totalEmployees);
      Console.WriteLine(revenue);

   	}
  }
}

//part 1:3
using System;

namespace PlanetCalculations
{
  class Program
  {
    static void Main(string[] args)
    {  
      // Your Age
      int userAge = 29;

      // Length of years on Jupiter (in Earth years)
      double jupiterYears = 11.86;

      // Age on Jupiter
      double jupiterAge = userAge / jupiterYears;

      // Time to Jupiter
      double journeyToJupiter = 6.142466;

      // New Age on Earth
      double newEarthAge = userAge + journeyToJupiter;

      // New Age on Jupiter
      double newJupiterAge = newEarthAge / jupiterYears;

      // Log calculations to console
      Console.WriteLine(userAge);
      Console.WriteLine(jupiterAge);
      Console.WriteLine(newEarthAge);
      Console.WriteLine(newJupiterAge);

    }
  }
}

//part 1:4
using System;

namespace MakingProgress
{
  class Program
  {
    static void Main(string[] args)
    {
      // Declare steps variable
      int steps = 0;

      // Two steps forward 
      steps += 2;

      // One step back 
      steps--;

      // Print result to the console
      Console.WriteLine(steps);
    }
  }
}

//part 1:5
using System;

namespace ClassTeams
{
  class Program
  {
    static void Main(string[] args)
    {
      // Number of students
      int students = 18;

      // Number of students in a group
      int groupSize = 3;

      // Does groupSize go evenly into students?
      Console.WriteLine(students % groupSize);

    }
  }
}

//part 1:6
using System;

namespace LowestNumber
{
  class Program
  {
    static void Main(string[] args)
    {
      // Starting variables 
      int numberOne = 12932;
      int numberTwo = -2828472;

      // Use built-in methods and save to variable 
      double numberOneSqrt = Math.Floor(Math.Sqrt(Math.Abs(numberOne)));

      // Use built-in methods and save to variable
      double numberTwoSqrt = Math.Floor(Math.Sqrt(Math.Abs(numberTwo)));

      // Print the lowest number
      Console.WriteLine(Math.Min(numberOneSqrt,numberTwoSqrt));
    }
  }
}

//part 2:1
using System;

namespace MoneyMaker
{
  class MainClass
  {
    public static void Main(string[] args)
    {
      Console.WriteLine("Welcome to Money Maker!");
      Console.WriteLine("Amount to convert:");
      double cents = Convert.ToDouble(Console.ReadLine());
      Console.WriteLine($"{cents} cents is equal to...");
      int gold = 10;
      int silver = 5;
      double goldCoins = Math.Floor(cents / gold);
      double remainder = cents % gold;
      double silverCoins = Math.Floor(remainder / silver);
      remainder %= silver;
      double bronzeCoins = Math.Floor(remainder);
      Console.WriteLine($"Gold coins: {goldCoins}");
      Console.WriteLine($"Silver coins: {silverCoins}");
      Console.WriteLine($"Bronze coins: {bronzeCoins}");
    }
  }
}

