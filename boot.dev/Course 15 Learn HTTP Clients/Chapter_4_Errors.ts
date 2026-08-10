//lesson 1
printUserExperience(4);
printUserExperience(10);
printUserExperience(200);

// don't touch below this line

function printUserExperience(level: number) {
  try {
    if (level < 1 || level > 100) {
      throw new Error("Experience level must be between 1 and 100!");
    }
    console.log(`The user has ${level} years of experience!`);
  } catch (err) {
    if (err instanceof Error) {
      console.log(err.message);
    }
  }
}

//lesson 3
try {
  const leaderboard = await fetchLeaderBoard();
  console.log(leaderboard);
} catch (err) {
  console.log("Our servers are down, but we will be up and running soon");
}

// don't touch below this line

async function fetchLeaderBoard(): Promise<any> {
  const response = await fetch("https://jello.servers");
  return response.json();
}

export {};
