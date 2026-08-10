//lesson 1
function bulkSendCost(numMessages) {
  var combinedCost = 0
  for (let i = 0; i < numMessages; i++) {
    combinedCost += 1 + i*.01
  }
  return combinedCost
}

export { bulkSendCost };

//lesson 2
function maxMessagesWithinBudget(budget) {
  var totalCost = 0
  var count = 0
  for (let i = 0; ; i++) {
    totalCost += 1 + .01*i
    if (totalCost > budget) {
      break
    }
    count ++
  }
  return count
}

export { maxMessagesWithinBudget };

//lesson 3
function printPrimes(max) {
  for (let i = 2; i <= max; i++) {
    if (i === 2) {
      console.log(i)
    }
    else if (i%2 !== 0){
      let test = true
      for (let j = 3; j * j <= i; j+=2) {
        if (i%j === 0) {
          test = false
          break
        }
      }
      if (test) {
        console.log(i)
      }
    }
  }
}
// don't touch below this line

function test(max) {
  console.log(`Primes up to ${max}:`);
  printPrimes(max);
  console.log(
    "===============================================================",
  );
}

test(10);
test(20);
test(30);

//lesson 4
function getMaxMessagesToSend(costMultiplier, maxCostInPennies) {
  let actualCostInPennies = 1.0;
  let maxMessagesToSend = 1;
  let balance = maxCostInPennies - actualCostInPennies;
  while (balance > 0) {
    actualCostInPennies *= costMultiplier;
    balance -= actualCostInPennies;
    maxMessagesToSend++;
  }
  if (balance < 0) {
    maxMessagesToSend--;
  }
  return maxMessagesToSend;
}

export { getMaxMessagesToSend };

//lesson 5
const printMatchingProperties = (messageLog, searchTerm) => {
  for (const key in messageLog) {
    if (key.startsWith(searchTerm)) {
      console.log(`Found: ${key} -> ${messageLog[key]}`);
    }
  }
};

// don't touch below this line

const messageLogs = [
  {
    messageId: "abc123",
    messageText: "Your order has shipped",
    timestamp: "2025-02-06T12:34:56Z",
    sender: "TextioBot",
  },
  {
    messageId: "def456",
    messageSender: "Textio",
  },
  {
    tomsBrilliantIdea: "Messages now have unique tracking codes",
    trackingCode: "trk-555888",
    loggedAt: "2025-02-07T09:30:00Z",
  },
];

for (const log of messageLogs) {
  printMatchingProperties(log, "message");
  printMatchingProperties(log, "log");
}