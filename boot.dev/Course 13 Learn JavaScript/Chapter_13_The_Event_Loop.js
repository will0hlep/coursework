//lesson 2
async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
  }
  
// don't touch below this line

export { sleep };

//lesson 4
function processMessages(messages) {
  let success = true;
  console.log(`Processing messages: ${messages}`);
  setTimeout(() => {
    finalizeJob(success, messages);
  }, 0);
  if (messages < 0) {
    console.log("invalid data: how do we have negative messages??");
    success = false;
    return;
  }
  if (messages > 100) {
    console.log("invalid data: way too many messages");
    success = false;
    return;
  }
  console.log("Doing more stuff...");
}

function finalizeJob(success, messages) {
  const msg = success
    ? `Processed ${messages} successfully!`
    : `Failed to process messages!`;
  console.log(msg);
}

// don't touch below this line

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

processMessages(42);
await sleep(0);
console.log("---");
processMessages(-1);
await sleep(0);
console.log("---");
processMessages(9001);

//lesson 5
async function processAnalytics(data) {
  let analysis = "";

  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(analysis);
    }, 100);

    setTimeout(() => {
      analysis += " - Finished!";
    }, 0);

    // don't touch above this line

    Promise.resolve()
    .then(() => {
      analysis += `- Processing: ${data}`;
    })

    // don't touch below this line

    analysis += "Analyzing...";
  });
}

export { processAnalytics };
