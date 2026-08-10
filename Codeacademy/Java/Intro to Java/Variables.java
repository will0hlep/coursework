//part 1
public class Creator {
	public static void main(String[] args) {
    String name = "James Gosling";
    int yearCreated = 1995;
    System.out.println(name);
    System.out.println(yearCreated);
	}
}

//part 2
//This is the class declaration
public class CountComment {
  //This is the main method that runs when you compile
	public static void main(String[] args) {
    //This is where you will define your variable
    int numComments = 6;
    //This is where you will print your variable
    System.out.print(numComments);
	}
  //This is the end of the class
}
//This is outside the class

//part 3
public class MarketShare {
	public static void main(String[] args) {
    double androidShare = 81.7;
    System.out.println(androidShare);
	}
}

//lesson 4
public class Booleans {
	public static void main(String[] args) {    
    boolean intsCanHoldDecimals = false;
    System.out.println(intsCanHoldDecimals);
	}
}

//lesson 5
public class Char {
	public static void main(String[] args) {
    char expectedGrade = 'A';
    System.out.println(expectedGrade);
	}
}

//lesson 6
public class Song {
	public static void main(String[] args) {
    String openingLyrics = "Yesterday, all my troubles seemed so far away";
    System.out.println(openingLyrics);
	}
}

//lesson 7
public class Mess {
	public static void main(String[] args) {   
		int year = 2001;
        String title = "Shrek";
        char genre = 'C';
        double runtime = 1.58;
        boolean isPG = true;
	}
}

//lesson 8
public class BadNames {
	public static void main(String[] args) {   
		String firstName = "Samira";
    String lastName = "Smith";
    String emailAddress = "samira@google.com";
    int salaryExpectation = 100000;
    int yearOfBirth = 1955;
    
    System.out.println("The program runs!");
	}
}

//lesson 9
public class MyProfile {
	public static void main(String[] args) {
    String name = "My Name";
    int age = 27;
    double desiredSalary = 1234567.89;
    char gender = 'm';
    boolean lookingForJob = false;
	}
}

//project
public class MadLibs {
  /*
  This program generates a mad libbed story.
  Author: Laura
  Date: 2/19/2049
  */
  public static void main(String[] args){
    String adjective1 = "alpha";
    String adjective2 = "bravo";
    String adjective3 =  "charlie";
    String name1 = "delta";
    String name2 = "echo";
    String place1 = "foxtrot";
    String verb1 = "golf";
    String noun1 = "hotel";
    String noun2 = "india";
    String noun3 = "juliett";
    String noun4 = "kilo";
    String noun5 = "lima";
    String noun6 = "mike";
    int number = 1;
    
    //The template for the story
    String story = "This morning "+name1+" woke up feeling "+adjective1+". 'It is going to be a "+adjective2+" day!' Outside, a bunch of "+noun1+"s were protesting to keep "+noun2+" in stores. They began to "+verb1+" to the rhythm of the "+noun3+", which made all the "+noun4+"s very "+adjective3+". Concerned, "+name1+" texted "+name2+", who flew "+name1+" to "+place1+" and dropped "+name1+" in a puddle of frozen "+noun5+". "+name1+" woke up in the year "+number+", in a world where "+noun6+"s ruled the world.";

    System.out.println(story);
  }       
}

//lesson 1
public class GuessingGame {
	public static void main(String[] args) {   
		int mystery1 = 8 + 6;
    int mystery2 = 8 - 6;
    System.out.println(mystery2);
	}
}

//lesson 2
public class PlusAndMinus {
	public static void main(String[] args) {   
		int zebrasInZoo = 8;
    int giraffesInZoo = 4;
    int animalsInZoo = zebrasInZoo + giraffesInZoo;
    System.out.println(animalsInZoo);
    int numZebrasAfterTrade = zebrasInZoo - 2;
    System.out.println(numZebrasAfterTrade);
	}
}

//lesson 3
public class MultAndDivide {
	public static void main(String[] args) {   
		double subtotal = 30;
    double tax = 0.0875;
    double total = subtotal + subtotal*tax;
    double perPerson = total/4;
    System.out.println(total);
    System.out.println(perPerson);
	}
}

//lesson 4
public class Modulo {
	public static void main(String[] args) {   
		int students = 26;
    int leftOut = students%3;
    System.out.println(leftOut);
	}
}

//lesson 5
public class BakeSale {
	public static void main(String[] args) {   
		int numCookies = 17;
    numCookies -= 3;
    numCookies /= 2;
    // Add your code above
    System.out.println(numCookies);
	}
}

//lesson 6
public class Operations {
	public static void main(String[] args) { 
    int expression1 = 5 % 2 - (4 * 2 - 1);
    System.out.println(expression1);
    int expression2 = (3 + (2 * 2 - 5)) + 6 - 5;
    System.out.println(expression2);
    int expression3 = 5 * 4 % 3 - 2 + 1;
    System.out.println(expression3);
	}
}

//lesson 7
public class GreaterLessThan {
	public static void main(String[] args) {   
		double creditsEarned = 176.5;
    double creditsOfSeminar = 8;
    double creditsToGraduate = 180;
    System.out.println(creditsEarned > creditsToGraduate);
    double creditsAfterSeminar = creditsEarned + creditsOfSeminar;
    System.out.println(creditsAfterSeminar > creditsToGraduate);
	}
}

//lesson 8
public class EqualNotEqual {
	public static void main(String[] args) {   
		int songsA = 9;
    int songsB = 9;
    int albumLengthA = 41;
    int albumLengthB = 53;
    boolean sameNumberOfSongs = songsA == songsB;
    boolean differentLength = albumLengthA != albumLengthB;
	}
}

//lesson 9
public class GreaterThanEqualTo {
  	public static void main(String[] args){
      double recommendedWaterIntake = 8;
      double daysInChallenge = 30;
      double yourWaterIntake = 235.5;
      double totalRecommendedAmount = recommendedWaterIntake*daysInChallenge;
      boolean isChallengeComplete = yourWaterIntake>=totalRecommendedAmount;
      System.out.println(isChallengeComplete);
    }       
}

//lesson 10
public class Song {
  	public static void main(String[] args){
      String line1 = "Nah nah nah nah nah nah nah nah nah yeah";
      String line2 = "Nah nah nah nah nah nah, nah nah nah, hey Jude";
      String line3 = "Nah nah nah nah nah nah, nah nah nah, hey Jude";
      System.out.println(line1.equals(line2));
      System.out.println(line2.equals(line3));
    }       
}

//lesson 11
public class Zoo {
  	public static void main(String[] args){
      int animals = 12;
      String species = "zebra";
      String zooDescription = "Our zoo has " + animals + " " + species + "s!";
      System.out.println(zooDescription);
    }       
}

//lesson 12
public class Final {
	public static void main(String[] args) { 
    final double pi = 3.14;
    System.out.println(pi);
    //pi += 1; Illegal since pi is marked as final
	}
}

//lesson 13
public class BankAccount {
  	public static void main(String[] args){
      double balance = 1000.75;
      double amountToWithdraw = 250;
      double updatedBalance = balance - amountToWithdraw;
      double amountForEachFriend = updatedBalance / 3;
      boolean canPurchaseTicket = amountForEachFriend >= 250;
      System.out.println(canPurchaseTicket);
      System.out.println("I gave each friend " + amountForEachFriend + "...");
    }       
}

//project 2
public class Magic {
	public static void main(String[] args) {
    int myNumber = 78;
    //We will refer to myNumber as the original number from now on
    int stepOne = myNumber * myNumber;
    int stepTwo = stepOne + myNumber;
    int stepThree = stepTwo / myNumber;
    int stepFour = stepThree + 17;
    int stepFive = stepFour - myNumber;
    int stepSix = stepFive / 6;
    System.out.println(stepSix);
	}
}