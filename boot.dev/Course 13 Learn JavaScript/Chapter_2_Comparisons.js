//lesson 1
let messageLen = 10;
let maxMessageLen = 20;
console.log(
  "Trying to send a message of length:",
  messageLen,
  "and a max length of:",
  maxMessageLen,
);

// don't touch above this line

if (messageLen <= maxMessageLen) {
  console.log("Message sent");
} else {
  console.log("Message not sent");
}

//lesson 2
console.log(5 < 6);
console.log(5 !== 6);
console.log(5 == "5");
console.log(6 >= 6);

//lesson 3
const hasHighOpenRate = true;
const isRecent = true;
const hasStrongReplyRate = false;
const canBeResent = true;
const isFlaggedAsSpam = false;

// don't touch above this line

const isHighEngagement = hasHighOpenRate && isRecent && (hasStrongReplyRate || canBeResent) && !isFlaggedAsSpam

// don't touch below this line

console.log(`The campaign is high-engagement: ${isHighEngagement}`);

//lesson 4
function billingCost(plan) {
  switch (plan) {
    case "basic":
      return 10.0;
    case "pro":
      return 20.0;
    case "enterprise":
      return 50.0
    default:
      return 0.0;
  }
}

// don't touch below this line

console.log(`The cost for a basic plan is $${billingCost("basic").toFixed(2)}`);
console.log(`The cost for a pro plan is $${billingCost("pro").toFixed(2)}`);
console.log(
  `The cost for a enterprise plan is $${billingCost("enterprise").toFixed(2)}`,
);
console.log(`The cost for a free plan is $${billingCost("free").toFixed(2)}`);
console.log(
  `The cost for a unknown plan is $${billingCost("unknown").toFixed(2)}`,
);

//lesson 5
const retryLimit = 10;
const numRetries = 9;

// don't touch above this line

const messageStatus = numRetries < retryLimit? "Processing": "Failed";

// don't touch below this line

console.log(messageStatus);

//lesson 7
const userCredits = -2;

// don't touch above this line

if (userCredits>0) {
  console.log("Sending message...");
} else {
  console.log("Not enough credits.");
}

//lesson 8
const name = "James Holden";
const provider = "AT&T";
const phoneNumber = "555-123-4567";
const subscriptionType = null;

// don't touch above this line

console.log(
  `Creating ${subscriptionType ?? "Guest"} Profile for ${name} with ${provider} at ${phoneNumber}.`,
);
