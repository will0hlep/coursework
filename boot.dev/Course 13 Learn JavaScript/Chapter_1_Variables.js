//lesson 1
console.log("Starting Textio server...");

//lesson 2
var smsSendingLimit = 1000;
var hasPermission = true;
var username = 'kevin';
var nothing = undefined;

// don't touch below this line
console.log("smsSendingLimit is a " + typeof smsSendingLimit);
console.log("hasPermission is a " + typeof hasPermission);
console.log("username is a " + typeof username);
console.log("nothing is " + typeof nothing);

//lesson 3
let messageText = "Welcome to Textio!";
let isBirthday = true;

if (isBirthday) {
  let messageText = "Happy Birthday!";

  console.log("sending birthday message...");
  console.log("messageText: ", messageText);
}

// don't touch below this line

console.log("sending welcome message...");
console.log("messageText: ", messageText);

//lesson 5
// Attention!
/*
  We are increasing the maximum message length from 140 to 280 characters.
  Very reluctantly, I might add.
  Users actually want to write more than 140 characters?!? Madness.
*/

const maxMessageLength = 140;
const newMaxMessageLength = 280;
console.log(
  `Textio is increasing the maximum message length from ${maxMessageLength} to ${newMaxMessageLength} characters.`,
);

//lesson 6
const promoMessages = 12;
const reminderMessages = 15;
const welcomeMessages = 8;
const supportMessages = 5;

// don't touch above this line

let totalMessagesSent = promoMessages + reminderMessages + welcomeMessages + supportMessages;
let averageMessagesSent = totalMessagesSent / 4;

// don't touch below this line

console.log("Total messages:", totalMessagesSent);
console.log("Average messages:", averageMessagesSent);

//lesson 8
let numFailedMessages = 1336;

// don't touch above this line

numFailedMessages++;

// don't touch below this line

console.log(numFailedMessages + " failed messages");

//lesson 9
let sentMessages
let deliveredMessages
let failedMessages

// don't touch below this line

console.log("Sent is:", sentMessages);
console.log("Delivered is:", deliveredMessages);
console.log("Failed is:", failedMessages);

//lesson 10
let sentMessages = null;
let deliveredMessages = null;
let failedMessages = null;

// don't touch below this line

console.log("Sent is null:", sentMessages === null);
console.log("Delivered is null:", deliveredMessages === null);
console.log("Failed is null:", failedMessages === null);

//lesson 11
let totalSentMessages = 100;
let totalReceivedMessages = 50;

// don't touch below this line

const totalMessages = totalSentMessages + totalReceivedMessages;

console.log("Total sent messages:", totalSentMessages);
console.log("Total received messages:", totalReceivedMessages);
console.log("Total messages:", totalMessages);

//lesson 12
const averageOpenRate = 0.23, displayMessage = "is the average open rate of your messages";

// don't touch below this line

console.log("Average open rate:", averageOpenRate);
console.log("Display message:", displayMessage);

//lesson 14
const email = "stoob@boot.dev";

// print the first character in the string here
console.log(email[0]);

// print the last character in the string here
console.log(email[email.length - 1]);

// print the entire string here
console.log(email);

//lesson 15
const name = "Saul Goodman";
const openRate = 30.5;

let msg = `Hi ${name}, your open rate is ${openRate} percent`

// don't touch below this line

console.log(msg);

//lesson 18
console.log("contacting cell tower..."); console.log("sending message...")
// don't go past line 1 with your code

//lesson 19
let name = "🐻";
console.log(`constant 'name' UTF-16 unit length: ${name.length}`);
console.log(`constant 'name' character length: ${[...name].length}`);
console.log("=====================================");
console.log(`Hi ${name}, welcome to Textio!`);
