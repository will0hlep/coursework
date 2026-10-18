//lesson 2
public class Order {
  
  public static void main(String[] args) {
    
    double itemCost = 30.99;
    
    // Write an if-then statement:
    if (itemCost > 24) {
      System.out.println("High value item!");
    }
    
  }
  
}

//lesson 3
public class Order {
  
  public static void main(String[] args) {
    
    boolean isFilled = false;
    
    // Write an if-then-else statement:
    if (isFilled) {
      System.out.println("Shipping");
    } else {
      System.out.println("Order not ready");
    }
    
  }
  
}

//lesson 4
public class Order {
  boolean isFilled;
  double billAmount;
  String shipping;
  
  public Order(boolean filled, double cost, String shippingMethod) {
		if (cost > 24.00) {
      System.out.println("High value item!");
    }
    isFilled = filled;
    billAmount = cost;
    shipping = shippingMethod;
  }
  
  public void ship() {
    if (isFilled) {
      System.out.println("Shipping");
      System.out.println("Shipping cost: " + calculateShipping());
    } else {
      System.out.println("Order not ready");
    }
  }
  
  public double calculateShipping() {
	 	// declare conditional statement here
    if (shipping == "Regular") {
      return 0;
    } else if (shipping == "Express") {
      return 1.75;
    } else {
      return 0.50;
    }
 	}
  
  public static void main(String[] args) {
    // do not alter the main method!
    Order book = new Order(true, 9.99, "Express");
    Order chemistrySet = new Order(false, 72.50, "Regular");
    
    book.ship();
    chemistrySet.ship();
  }
}

//lesson 5
public class Order {
  boolean isFilled;
  double billAmount;
  String shipping;
  String couponCode;
  
  public Order(boolean filled, double cost, String shippingMethod, String coupon) {
		if (cost > 24.00) {
      System.out.println("High value item!");
    }
    isFilled = filled;
    billAmount = cost;
    shipping = shippingMethod;
    couponCode = coupon;
  }
  
  public void ship() {
    if (isFilled) {
      System.out.println("Shipping");
      System.out.println("Shipping cost: " + calculateShipping());
    } else {
      System.out.println("Order not ready");
    }
  }
  
  public double calculateShipping() {
    if (shipping.equals("Regular")) {
      return 0;
    }
    if (shipping.equals("Express")) {
      // Add your code here
      if (couponCode == "ship50") {
        return 0.85;
      }
      return 1.75;
    }
    return 0.50;
 	}
  
  public static void main(String[] args) {
    // do not alter the main method!
    Order book = new Order(true, 9.99, "Express", "ship50");
    Order chemistrySet = new Order(false, 72.50, "Regular", "freeShipping");
    
    book.ship();
    chemistrySet.ship();
  }
}

//lesson 6
public class Order {
  boolean isFilled;
  double billAmount;
  String shipping;
  
  public Order(boolean filled, double cost, String shippingMethod) {
		if (cost > 24.00) {
      System.out.println("High value item!");
    }
    isFilled = filled;
    billAmount = cost;
    shipping = shippingMethod;
  }
  
  public void ship() {
    if (isFilled) {
      System.out.println("Shipping");
      System.out.println("Shipping cost: " + calculateShipping());
    } else {
      System.out.println("Order not ready");
    }
  }
  
  public double calculateShipping() {
    double shippingCost;
	 	// declare switch statement here
    switch (shipping) {
      case "Regular":
        return 0;
      case "Express":
        return 1.75;
      default:
        return 0.5;
    }
 	}
  
  public static void main(String[] args) {
    // do not alter the main method!
    Order book = new Order(true, 9.99, "Express");
    Order chemistrySet = new Order(false, 72.50, "Regular");
    
    book.ship();
    chemistrySet.ship();
  }
}


//lesson 7
public class Order {
  boolean isFilled;
  double billAmount;
  String shipping;
  
  public Order(boolean filled, double cost, String shippingMethod) {
		if (cost > 24.00) {
      System.out.println("High value item!");
    } else {
      System.out.println("Low value item!");
    }
    isFilled = filled;
    billAmount = cost;
    shipping = shippingMethod;
  }
  
  public void ship() {
    if (isFilled) {
      System.out.println("Shipping");
    } else {
      System.out.println("Order not ready");
    }
    
    double shippingCost = calculateShipping();
    
    System.out.println("Shipping cost: ");
    System.out.println(shippingCost);
  }
  
  public double calculateShipping() {
    double shippingCost;
    switch (shipping) {
      case "Regular":
        shippingCost = 0;
        break;
      case "Express":    
        shippingCost = 1.75;
        break;
      default:
        shippingCost = .50; 
    }
    return shippingCost;
 	}
  
  public static void main(String[] args) {
    // create instances and call methods here!
    Order newOrder = new Order(true, 25, "Express");
    newOrder.ship();
  }
}

// lesson 1
public class Reservation {
  int guestCount;
  int restaurantCapacity;
  boolean isRestaurantOpen;
  boolean isConfirmed;
  
  public Reservation(int count, int capacity, boolean open) {
    guestCount = count;
		restaurantCapacity = capacity;
		isRestaurantOpen = open;
  }  
  
  public void confirmReservation() {
    if (isRestaurantOpen && restaurantCapacity >= guestCount) {
      System.out.println("Reservation confirmed");
      isConfirmed = true;
    } else {
      System.out.println("Reservation denied");
      isConfirmed = false;
    }
  }
  
  public void informUser() {
    System.out.println("Please enjoy your meal!");
  }
  
  public static void main(String[] args) {
    Reservation partyOfThree = new Reservation(3, 12, true);
    Reservation partyOfFour = new Reservation(4, 3, true);
    partyOfThree.confirmReservation();
    partyOfThree.informUser();
    partyOfFour.confirmReservation();
    partyOfFour.informUser();
  }
}

//lesson 3
public class Reservation {
  int guestCount;
  int restaurantCapacity;
  boolean isRestaurantOpen;
  boolean isConfirmed;
  
  public Reservation(int count, int capacity, boolean open) {
    if (count < 1 || count > 8) {
      System.out.println("Invalid reservation!");
    }
    guestCount = count;
		restaurantCapacity = capacity;
		isRestaurantOpen = open;
  }  
  
  public void confirmReservation() {
    if (restaurantCapacity >= guestCount && isRestaurantOpen) {
      System.out.println("Reservation confirmed");
      isConfirmed = true;
    } else {
      System.out.println("Reservation denied");
			isConfirmed = false;
    }
  }
  
  public void informUser() {
    System.out.println("Please enjoy your meal!");
  }
  
  public static void main(String[] args) {
    Reservation partyOfThree = new Reservation(3, 12, true);
    Reservation partyOfFour = new Reservation(4, 3, true);
    partyOfThree.confirmReservation();
    partyOfThree.informUser();
    partyOfFour.confirmReservation();
    partyOfFour.informUser();
  }
}

//lesson 4
public class Reservation {
  int guestCount;
  int restaurantCapacity;
  boolean isRestaurantOpen;
  boolean isConfirmed;
  
  public Reservation(int count, int capacity, boolean open) {
    if (count < 1 || count > 8) {
      System.out.println("Invalid reservation!");
    }
    guestCount = count;
		restaurantCapacity = capacity;
		isRestaurantOpen = open;
  }  
  
  public void confirmReservation() {
    if (restaurantCapacity >= guestCount && isRestaurantOpen) {
      System.out.println("Reservation confirmed");
      isConfirmed = true;
    } else {
      System.out.println("Reservation denied");
			isConfirmed = false;
    }
  }
  
  public void informUser() {
    // Write conditional here
    if (isConfirmed) {
      System.out.println("Please enjoy your meal!");
    } else {
      System.out.println("Unable to confirm reservation, please contact restaurant.");
    }
  }
  
  public static void main(String[] args) {
    Reservation partyOfThree = new Reservation(3, 12, true);
    Reservation partyOfFour = new Reservation(4, 3, true);
    partyOfThree.confirmReservation();
    partyOfThree.informUser();
    partyOfFour.confirmReservation();
    partyOfFour.informUser();
  }
}

//lesson 5
public class Operators {
  public static void main(String[] args) {
    int a = 6;
    int b = 3;

    boolean ex1 = !(a == 7 && (b >= a || a != a));
    System.out.println(ex1);

    boolean ex2 = a == b || !(b > 3);
    System.out.println(ex2);

    boolean ex3 = !(b <= a && b != a + b);
    System.out.println(ex3); 

  }
}

//lesson 6
public class Reservation {
  int guestCount;
  int restaurantCapacity;
  boolean isRestaurantOpen;
  boolean isConfirmed;
  
  public Reservation(int count, int capacity, boolean open) {
    if (count < 1 || count > 8) {
      System.out.println("Invalid reservation!");
    }
    guestCount = count;
		restaurantCapacity = capacity;
		isRestaurantOpen = open;
  }  
  
  public void confirmReservation() {
    if (restaurantCapacity >= guestCount && isRestaurantOpen) {
      System.out.println("Reservation confirmed");
      isConfirmed = true;
    } else {
      System.out.println("Reservation denied");
			isConfirmed = false;
    }
  }
  
  public void informUser() {
    if (!isConfirmed) {
      System.out.println("Unable to confirm reservation, please contact restaurant.");
    } else {
      System.out.println("Please enjoy your meal!");
    }
  }
  
  public static void main(String[] args) {
    Reservation newReservation = new Reservation(4, 8, true);
    newReservation.confirmReservation();
    newReservation.informUser();
  }
}
