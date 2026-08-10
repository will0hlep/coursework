//lesson 1
function createMessage(phoneNumber, message) {
  const Message = {
    phoneNumber: phoneNumber,
    message: message,
    messageLength: message.length
  };
  return Message;
}

export { createMessage };

//lesson 3
function addID(campaignRecord) {
  campaignRecord.id = campaignRecord.campaignName + "-" + campaignRecord.senderName;
  return campaignRecord;
}

// don't touch below this line

export { addID };

//lesson 4
function getCampaignCreator(campaign) {
  return campaign.creator.firstName;
}

// don't touch below this line

export { getCampaignCreator };

//lesson 6
function getRegion(campaign) {
  return campaign?.location?.region;
}

// don't touch below this line

export { getRegion };

//lesson 9
const campaign = {
  getRemainingMessages() {
    return this.maxMessages - this.sentMessages;
  },
  maxMessages: 100,
  sentMessages: 30,
  name: "Welcome Campaign",
};

// don't touch below this line

export { campaign };

//lesson 10
const campaign = {
  name: "Welcome Campaign",
  maxMessages: 100,
  sentMessages: 30,
  sendMessage() {
    this.sentMessages ++;
  },
};

// don't touch below this line

export { campaign };

//lesson 12
function getProviderCount(provider, counts) {
  return counts[provider] ?? 0
}

// don't touch below this line

export { getProviderCount };

//lesson 14
const isSpamMessage = (message) => {
  if (message.toLowerCase().includes("offer")) {
    return true;
  }
  if (message.toLowerCase().includes("free")) {
    return true;
  }
  return false;
}

// don't touch below this line

function isFunctionType(f) {
  return f.hasOwnProperty("prototype");
}

function test(msg) {
  const isSpam = isSpamMessage(msg);
  console.log(`'${msg}' is spam: ${isSpam}`);
}

test("Get an offer now!");
test("Free beer in your local area");
test("Hey mom, sorry I couldn't make it to your birthday...");
console.log("========================");
if (isFunctionType(isSpamMessage)) {
  console.log("isSpamMessage is a classic function");
} else {
  console.log("isSpamMessage is a fat arrow function");
}

//lesson 15
const campaign = {
  name: "Welcome Campaign",
  maxMessages: 100,
  sentMessages: 30,
  sendMessage() {
    this.sentMessages++;
  },
};

// don't touch below this line

export { campaign };

//lesson 16
function mergeTemplates(defaultTemplates, customTemplates) {
  return {...defaultTemplates, ...customTemplates};
}

// don't touch below this line

export { mergeTemplates };

//lesson 17
function calculateCampaignMetrics(sent, opened, clicked) {
  const openRate = opened / sent;
  const clickRate = clicked / sent;
  const conversionRate = clicked / opened;
  return {openRate, clickRate, conversionRate};
}

// don't touch below this line

export { calculateCampaignMetrics };

//lesson 18
function calculateCampaignMetrics(sent, opened, clicked) {
  const openRate = opened / sent;
  const clickRate = clicked / sent;
  const conversionRate = clicked / opened;
  return {
    openRate,
    clickRate,
    conversionRate,
  };
}

// don't touch above this line

const {openRate, clickRate, conversionRate} = calculateCampaignMetrics(1000, 800, 200);

// don't touch below this line

console.log(`Open Rate:       ${openRate}`);
console.log(`Click Rate:      ${clickRate}`);
console.log(`Conversion Rate: ${conversionRate}`);

//lesson 19
const campaign = {
  name: "Welcome Campaign",
  maxMessages: 100,
  sentMessages: 30,
  sendMessage() {
    this.sentMessages++;
  },
};

function sendWelcome(name, callback) {
  callback();
  console.log(`Sending: "Welcome ${name}! We are so glad you are here."`);
}

console.log("Campaign Messages:", campaign.sentMessages);

// don't touch above this line

sendWelcome("Tyler", campaign.sendMessage.bind(campaign));

// don't touch below this line

console.log("Campaign Messages:", campaign.sentMessages);