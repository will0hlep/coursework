//lesson 1
class Message {
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
  }
}

// don't touch below this line

export { Message };

//lesoson 2
class Message {
  #createdAt
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
    this.#createdAt = new Date();
  }
}

// don't touch below this line

const message = new Message("555-1234", "555-5678", "Hi there!");

console.log("Attempting to access the property createdAt...");
console.log("createdAt: " + message.createdAt);

const messageClass = Message.toString();
console.log("has private createdAt: " + messageClass.includes("#createdAt"));

//lesson 3
class Message {
  static numMsg = 0;
  static totalMsgLength = 0;
  
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
    Message.numMsg ++;
    Message.totalMsgLength += body.length;
  }

  static getAverageMessageLength() {
    return Math.round(100*Message.totalMsgLength/Message.numMsg)/100;
  }
}

// don't touch below this line

export { Message };

//lesson 4
class Contact {
  constructor(name, phoneNumber) {
    this.name = name;
    this._phoneNumber = phoneNumber;
  }

  set phoneNumber(value) {
    if (value.length !== 10) {
      throw new Error("Invalid phone number.");
    }
    this._phoneNumber = value
  }

  get phoneNumber() {
    return "(" + this._phoneNumber.slice(0,3) + ") " + this._phoneNumber.slice(3,6) + "-" + this._phoneNumber.slice(6)
  }
}

// don't touch below this line

export { Contact };

//lesson 5
class Sender {
  constructor(recipient) {
    this.recipient = recipient;
  }

  sendMessage(message) {
    throw new Error("sendMessage method must be implemented by subclasses");
  }
}

// don't touch above this line

class SMSSender extends Sender {
  sendMessage(message) {
    console.log(`Sending SMS to ${this.recipient}: ${message}`);
  }
}

class EmailSender extends Sender {
  sendMessage(message) {
    console.log(`Sending email to ${this.recipient}: ${message}`);
  }
}

// don't touch below this line

export { Sender, SMSSender, EmailSender };

//lesson 6
class Sender {
  constructor(recipient) {
    this.recipient = recipient;
  }

  formatMessage(message) {
    return `To: ${this.recipient}, Message: ${message}`;
  }
}

// don't touch above this line

class SMSSender extends Sender {
  formatMessage(message) {
    return `${super.formatMessage(message)} [SMS]`;
  }
}

class EmailSender extends Sender {
  formatMessage(message) {
    return `${super.formatMessage(message)} [Email]`;
  }
}

// don't touch below this line

export { Sender, SMSSender, EmailSender };
