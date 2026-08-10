//lesson 1
export class Customer {
  firstName: string;
  lastName: string;

  constructor(firstName: string, lastName: string) {
    this.firstName = firstName
    this.lastName = lastName
  }

  getFullName() {
    return `${this.firstName} ${this.lastName}`
  }
}

//lesson 2
export class Customer {
  firstName: string;
  lastName: string;
  #balance: number;

  constructor(firstName: string, lastName: string, balance: number) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.#balance = balance;
  }

  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }

  purchase(cost: number) {
    this.#balance -= cost;
    return this.#balance
  }
}

//lesson 4
export class Customer {
  firstName: string;
  lastName: string;
  protected balance: number;

  constructor(firstName: string, lastName: string, balance: number) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.balance = balance;
  }

  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
}

export class RegularCustomer extends Customer {
  constructor(firstName: string, lastName: string, balance: number) {
    super(firstName, lastName, balance);
  }

  getBalance() {
    return this.balance;
  }
}

//lesson 5
export abstract class Customer {
  firstName: string;
  lastName: string;
  protected balance: number;

  constructor(firstName: string, lastName: string, balance: number) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.balance = balance;
  }

  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
}

export class RegularCustomer extends Customer {
  constructor(firstName: string, lastName: string, balance: number) {
    super(firstName, lastName, balance)
  }

  getBalance(): number {
    return this.balance;
  }
}

//lesson 6
interface User {
  firstName: string;
  lastName: string;

  getFullName(): string;
}

interface Customer {
  getBalance(): number;
}

export class RegularCustomer implements Customer, User {
  firstName: string;
  lastName: string;
  protected balance: number;

  constructor(firstName: string, lastName: string, balance: number) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.balance = balance;
  }

  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }

  getBalance() {
    return this.balance;
  }
}

//lesson 8
interface User {
  firstName: string;
  lastName: string;
  
  getFullName(): string;
}

interface Customer {
  getBalance(): number;
}

export class RegularCustomer implements User, Customer {
  firstName: string;
  lastName: string;
  protected balance: number;
  private balanceQueries: number;

  constructor(firstName: string, lastName: string, balance: number) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.balance = balance;
    this.balanceQueries = 0;
  }
  
  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }

  getBalance(this: RegularCustomer): number {
    this.balanceQueries ++;
    return this.balance;
  }

  getBalanceQueries(): number {
    return this.balanceQueries;
  }
}

//lesson 9
export class ExecutiveMember {
  constructor(
    private balance: number,
    private points: number,
  ) {}

  isVIP(): boolean {
    return (this.balance>=10000)
  }

  redeemPoints(cost: number): boolean {
    if (this.points>=cost) {
      this.points -= cost;
      return true;
    }
    return false;
  }
}
