#part 1
public class Store {
     public void buyItems()
     {

     }
}

#part 2
public class Main{
  public static void main(String[] args){
    Store newStore = new Store();
  }
}

public class Store{
  public Store(){
    System.out.println("I am inside the Store constructor");
  }
}

#part 3
public class Dog{
  public String name;
  public String breed;
  public int weight;

  public Dog(){
    //DO NOT WRITE ANYTHING HERE!!
  }
}

#part 4
public class Dog{
  public String name;
  public String breed;
  public int weight;

  public Dog(){
    //DO NOT WRITE ANYTHING HERE!!
  }
}

#part 5
public class Store{
  public String productType;
  public Store(String product){
    productType = product;
  }
}

#part 6
public class Main{
  public static void main(String[] args) {
    Store lemonadeStand = new Store("lemonade");
    System.out.println(lemonadeStand.productType);
  }
}

#part 7
public class Main{
  public static void main(String[] args) {
    Store cookieShop = new Store("cookies", 12, 3.75)
  }
}

public class Store {
  // instance fields
  public String productType;
  public int inventoryCount;
  public double inventoryPrice;

  // constructor method
  public Store(String product, int count, double price) {
    productType = product;
    inventoryCount = count;
    inventoryPrice = price;
  }
}

#part 8
public class Dog {
  String breed;
  boolean hasOwner;
  int age;
  
  public Dog(String dogBreed, boolean dogOwned, int dogYears) {
    System.out.println("Constructor invoked!");
    breed = dogBreed;
    hasOwner = dogOwned;
    age = dogYears;
  }
  
  public static void main(String[] args) {
    System.out.println("Main method started");
    Dog fido = new Dog("poodle", false, 4);
    Dog nunzio = new Dog("shiba inu", true, 12);
    boolean isFidoOlder = fido.age > nunzio.age;
    int totalDogYears = nunzio.age + fido.age;
    System.out.println("Two dogs created: a " + fido.breed + " and a " + nunzio.breed);
    System.out.println("The statement that fido is an older dog is: " + isFidoOlder);
    System.out.println("The total age of the dogs is: " + totalDogYears);
    System.out.println("Main method finished");
  }
}

#lesson 1

public class SavingsAccount {
  int balance;
    
  public SavingsAccount(int initialBalance){
    balance = initialBalance;
  }
    
  public void checkBalance(){
    System.out.println("Hello!");
    System.out.println("Your balance is " + balance);
  }
    
  public void deposit(int amountToDeposit){
    balance = balance + amountToDeposit;
    System.out.println("You just deposited " + amountToDeposit);
  }
    
  public int withdraw(int amountToWithdraw){
    balance = balance - amountToWithdraw;
    System.out.println("You just withdrew " + amountToWithdraw);
    return amountToWithdraw;
    }
    
  public String toString(){
    return "This is a savings account with " + balance + " saved.";
  }
         
}

public class Main {
  public static void main(String[] args) {
    SavingsAccount savings = new SavingsAccount(2000);
        
    //Check balance:
    savings.checkBalance();
        
    //Withdrawing:
    savings.withdraw(300);
        
    //Check balance:
    savings.checkBalance();
        
    //Deposit:
    savings.deposit(600);
        
    //Check balance:
    savings.checkBalance();
        
    //Deposit:
    savings.deposit(600);
        
    //Check balance:
    savings.checkBalance();
        
    System.out.println(savings);
  }
}

#project 1
public class Calculator {
  public Calculator() {

  }

  public int add(int a, int b) {
    return a + b;
  }

  public int subtract(int a, int b) {
    return a - b;
  }

  public int multiply(int a, int b) {
    return a * b;
  }

  public int divide(int a, int b) {
    return a / b;
  }

  public int modulo(int a, int b) {
    return a % b;
  }

  public static void main(String[] args){
    Calculator myCalculator = new Calculator();
    System.out.println(myCalculator.add(5,7));
    System.out.println(myCalculator.subtract(45,11));
  }
}

#project 2
public class Droid {
  String name;
  int batteryLevel;
  
  public Droid(String droidName) {
    name = droidName;
    batteryLevel = 100;
  }

  public String toString() {
    return "Hello, I'm the droid: " + name;
  }

  public void performTask(String task) {
    System.out.println(name + " is performing task: " + task);
    batteryLevel -= 10;
  }

  public static void main(String[] args){
    Droid Codey = new Droid("Codey");
    System.out.println(Codey);
    Codey.performTask("Code Academy kinda sucks. There is no read aloud option for the endless pages of text. The validation of code is either powered by AI, which is lazy, or over specific for some reason. I think someone from Code Academy should try Boot.dev for a few hours to see what they are missing.");
  }
}

