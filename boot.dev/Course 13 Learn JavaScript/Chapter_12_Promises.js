//lesson 1
const textioSetupCompleteWait = 4;
const errorHandlingWait = 3;
const messageRoutingWait = 2;
const smsProvidersWait = 1;

// don't touch below this line

setTimeout(
  () => console.log("Textio setup complete!"),
  textioSetupCompleteWait,
);
setTimeout(
  () => console.log("Setting up error handling and retries..."),
  errorHandlingWait,
);
setTimeout(
  () => console.log("Configuring message routing..."),
  messageRoutingWait,
);
setTimeout(
  () => console.log("Connecting to SMS providers..."),
  smsProvidersWait,
);

console.log("Starting Textio service initialization...");

await sleep(5);
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

//lesson 5
function updateMessageStatus(messageId, currentStatus, isDelivered) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (currentStatus === "Sending") {
        if (isDelivered) {
          resolve(`Textio Message ${messageId} has been delivered successfully.`)
        } else {
          reject(`Textio Message ${messageId} is still sending and cannot be marked as delivered.`)
        }
      } else {
        resolve(`Textio Message ${messageId} status updated to ${currentStatus}.`)
      }
    }, 500);
  });
}

// don't touch below this line

export { updateMessageStatus };

//lesson 8
let message = await updateMessageStatus("M123", "Sending", true)

// don't touch below this line

console.log(message);

function updateMessageStatus(messageId, currentStatus, isDelivered) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (currentStatus === "Sending") {
        if (isDelivered) {
          resolve(
            `Textio Message ${messageId} has been delivered successfully.`,
          );
        } else {
          reject(
            `Textio Message ${messageId} is still sending and cannot be marked as delivered.`,
          );
        }
      } else {
        resolve(
          `Textio Message ${messageId} status updated to ${currentStatus}.`,
        );
      }
    }, 1000);
  });
}

//lesson 9
async function getMessageHash(sender, content) {
  const hash = await sha256Hex(content);
  return `Sender (${sender}): ${hash}`;
}

// don't touch below this line

async function sha256Hex(str) {
  const encoder = new TextEncoder();
  const data = encoder.encode(str);
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hex = hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
  return hex;
}

export { getMessageHash };
