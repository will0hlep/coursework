//lesson 1
const sentMessages = [];
sentMessages.push("Welcome to Textio!")
logArray(sentMessages)
sentMessages.push("Reminder: Your payment is due soon.")
logArray(sentMessages)

// don't touch below this line

function logArray(arr) {
  console.log("Array contents:");
  for (const el of arr) {
    console.log(` - ${el}`);
  }
  console.log("=======================================");
}

//lesson 2
const getMostRecentUser = (usernames) => {
  const users = usernames.length;
  if (users === 0) {
    return null;
  }
  return usernames[users-1];
};

export { getMostRecentUser };

//lesson 3
const uploadNewMessages = (oldMessages, newMessages) => {
  return [...oldMessages, ...newMessages];
};

export { uploadNewMessages };

//lesson 4
function getCleanRank(reviewWords) {
  let rating = 0;
  let badWords = ["dang", "shoot", "heck"];
  for (let i = 0; i < badWords.length; i++) {
    if (reviewWords.includes(badWords[i])) {
      rating++;
      if (rating >= 2) {
        return "filthy";
      }
    }
  }
  if (rating === 1) {
    return "dirty";
  }
  return "clean";
};

export { getCleanRank };

//lesson 5
const getCleanMessages = (messages, badWord) => {
  let cleanMessages = [];
  for (let message of messages) {
    if (!message.toLowerCase().includes(badWord.toLowerCase())) {
      cleanMessages.push(message);
    }
  }
  return cleanMessages;
};

export { getCleanMessages };

//lesson 6
function splitLogs(logs, slug) {
  for (let i=0; i<logs.length; i++) {
    if (logs[i].includes(slug)) {
      return {before:logs.slice(0,i), after:logs.slice(i+1), i:i};
    }
  }
  return {before:[], after:[], i:-1};
}

export { splitLogs };

//lesson 9
function getPrimaryAndBackupMessages(messages) {
  if (messages.length === 0) {
    return {primary: undefined, backups: []};
  }
  const [primary, ...backups] = messages
  return {primary: primary, backups: backups};
}

export { getPrimaryAndBackupMessages };
