//lesson 1
function concat(str1, str2) {
  return str1 + str2;
}

// don't touch below this line

console.log(concat("Lane,", " happy birthday!"));
console.log(concat("Naomi,", " can you call me?"));
console.log(concat("Juliette,", " where did you go?"));

//lesson 4
function getMonthlyPrice(tier) {
  switch(tier) {
  case "basic":
    return 10000
  case "premium":
    return 15000
  case "enterprise":
    return 50000
  default:
    return 0
}
}

// don't touch below this line

export { getMonthlyPrice };

//lesson 5
function isClean(review) {
  let clean = true;
  if (review.includes("dang")) {
    clean = false;
  }
  if (review.includes("shoot")) {
    clean = false;
  }
  if (review.includes("heck")) {
    clean = false;
  }
  return clean;
}

// don't touch below this line

export { isClean };

//lesson 6
function reformat(message, formatter) {
  return "TEXTIO: " + formatter(formatter(formatter(message)))
}

// don't touch below this line

export { reformat };

//lesson 7
function getMessageStatus(message) {
  let messageStatus = "processing";

  function isValidLength(message) {
    let messageStatus = "invalid";

    if (message.length > 0) {
      messageStatus = "valid";
    }

    return messageStatus;
  }

  // don't touch above this line

  messageStatus = isValidLength(message);
  return messageStatus;
}

// don't touch below this line

export { getMessageStatus };

//lesson 8
function printReports(intro, body, outro) {
  printCostReport(function(message) {return 2*message.length}, intro)
  printCostReport(function(message) {return 3*message.length}, body)
  printCostReport(function(message) {return 4*message.length}, outro)
}

// don't touch below this line

function printCostReport(costCalculator, message) {
  const cost = costCalculator(message);
  console.log(`Message: "${message}" Cost: ${cost} cents`);
}

printReports(
  "Welcome to the Hotel California",
  "Such a lovely place",
  "Plenty of room at the Hotel California",
);

//lesson 9
function createContact(phoneNumber, name = 'Anonymous', avatar = 'default.jpg') {
  if (!phoneNumber) {
    return `Invalid phone number`;
  }
  return `Contact saved! Name: ${name}, Phone number: ${phoneNumber}, Avatar: /public/pictures/${avatar}`;
}

// don't touch below this line

export { createContact };


//lesson 10
function getBillForMonth(costPerSend, messagesSent) {
  return costPerSend * messagesSent;
}

function monthlyBillIncrease(costPerSend, numLastMonth, numThisMonth) {
  let lastMonthBill = getBillForMonth(costPerSend, numLastMonth);
  let thisMonthBill = getBillForMonth(costPerSend, numThisMonth);
  return thisMonthBill - lastMonthBill;
}

// don't touch below this line

export { getBillForMonth, monthlyBillIncrease };


//lesson 11
const total = function calculateTotal(numMessages, bytesPerMessage) {
  return numMessages * bytesPerMessage;
}(100, 24);

// don't touch below this line

console.log("Total message cost:", total);

//lesson 12
const user = {
  name: "Default User",
  type: "user",
};

const adminUser = Object.create(user);
adminUser.type = "admin";

function isAdmin (user) {
  return "admin" === Object.getPrototypeOf(user).type;
}

// don't touch below this line

export { user, adminUser, isAdmin };
