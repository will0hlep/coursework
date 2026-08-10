//part 1:3
using System;

namespace Form
{
  class Program
  {
    static void Main(string[] args)
    {
      // Create Variables
      string name = "Shadow";
      string breed = "Golden Retriever";
      int age = 5;
      double weight = 65.22;
      bool spayed = true;
      // Print variables to the console
      Console.WriteLine(name);
      Console.WriteLine(breed);
      Console.WriteLine(age);
      Console.WriteLine(weight);
      Console.WriteLine(spayed);
    }
  }
}

//part 1:4
using System;

namespace Form
{
  class Program
  {
    static void Main(string[] args)
    {
      // Create Variables
      var food = "apple";
      var calories = 95;
      var isFruit = true;

      // Print variables to the console
      Console.WriteLine(food);
      Console.WriteLine(calories);
      Console.WriteLine(isFruit);
    }
  }
}

//part 1:5
using System;

namespace BugSquasher
{
  class Program
  {
    static void Main(string[] args)
    {
      double Number = 38498.3222;

      string Dinosaur = "Barney";

      double Lock = 293.000;

      bool IsYes = true;

      string Band = "The Low Anthem";

    }
  }
}

//part 1:6
using System;

namespace FavoriteNumber
{
  class Program
  {
    static void Main(string[] args)
    {
      // Ask user for fave number
      Console.Write("Enter your favorite number!: ");

      // Turn that answer into an int
      int faveNumber = Convert.ToInt32(Console.ReadLine());


    }
  }
}

// part 2:1
using System;

public class GalacticTravelAgency { 
  public static void Main(string[] args) {
    string passengerName = "Zara";
    int passengerAge = 28;
    string ticketType = "First Class";
    string preferredPlanet = "Mars";
    Console.WriteLine(passengerName);
    Console.WriteLine(passengerAge);
    Console.WriteLine(ticketType);
    Console.WriteLine(preferredPlanet);
    passengerAge++;
    Console.WriteLine(passengerAge);
    double passengerAgeDouble2 = (double)passengerAge;
    string passengerAgeString = Convert.ToString(passengerAge);
    Console.WriteLine(passengerAgeString);
  }
}