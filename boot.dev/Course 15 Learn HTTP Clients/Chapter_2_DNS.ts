//lesson 1
async function fetchIPAddress(domain: string): Promise<string | null> {
  const resp = await fetch(
    `https://1.1.1.1/dns-query?name=${domain}&type=A`,
    {
      headers: {
        accept: "application/dns-json",
      },
    },
  );
  const respObject = await resp.json();

  console.log(respObject);
  return respObject.Answer[0].data;
}

// don't touch below this line

export { fetchIPAddress };

//lesson 4
function getDomainNameFromURL(url: string): string {
  const urlObj = new URL(url)
  return urlObj.hostname
}

// don't touch below this line

export { getDomainNameFromURL };

//lesson 5
const bootdevAPIDomain = "boot.dev";

// don't touch below this line

import { Issue } from "./types";

const apiKey = generateKey();
const issues = await getIssueData(bootdevAPIDomain);

logIssues(issues);

async function getIssueData(domain: string): Promise<Issue[]> {
  const response = await fetch(
    `https://${domain}/v1/courses_rest_api/learn-http/issues`,
    {
      method: "GET",
      mode: "cors",
      headers: {
        "X-API-Key": apiKey,
        "Content-Type": "application/json",
      },
    },
  );
  return response.json();
}

function generateKey(): string {
  const characters = "ABCDEF0123456789";
  let result = "";
  for (let i = 0; i < 16; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

function logIssues(issues: Issue[]): void {
  for (const issue of issues) {
    console.log(issue.title);
  }
}
