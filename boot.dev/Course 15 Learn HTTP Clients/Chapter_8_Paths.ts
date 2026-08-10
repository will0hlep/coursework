//lesson 1
import { Resource } from "./types";

async function getResources(path: string): Promise<Resource[]> {
  const fullURL = `https://api.boot.dev/${path}`;
  const response = await fetch(fullURL, {
    method: "GET",
    mode: "cors",
    headers: {
      "X-API-Key": generateKey(),
      "Content-Type": "application/json",
    },
  });
  return response.json();
}

// don't touch below this line

const projects = await getResources("/v1/courses_rest_api/learn-http/projects");
console.log("Projects:");
logResources(projects);
console.log(" --- ");

const issues = await getResources("/v1/courses_rest_api/learn-http/issues");
console.log("Issues:");
logResources(issues);
console.log(" --- ");

const users = await getResources("/v1/courses_rest_api/learn-http/users");
console.log("Users:");
logResources(users);

function logResources(resources: Resource[]) {
  for (const resource of resources) {
    console.log(` - ${JSON.stringify(resource)}`);
  }
}

function generateKey(): string {
  const characters = "ABCDEF0123456789";
  let result = "";
  for (let i = 0; i < 16; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

//lesson 3
import { UserProfile } from "./types";

async function getUsers(url: string, apiKey: string): Promise<UserProfile[]> {
  const fullURL = `${url}?sort=experience`;
  const response = await fetch(fullURL, {
    method: "GET",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
    },
  });
  return response.json();
}

// don't touch below this line

const baseURL = "https://api.boot.dev/v1/courses_rest_api/learn-http/users";

const apiKey = generateKey();

const users = await getUsers(baseURL, apiKey);
for (const user of users) {
  console.log(
    `got user with name: ${user.user.name}, and experience: ${user.experience}`,
  );
}

function generateKey(): string {
  const characters = "ABCDEF0123456789";
  let result = "";
  for (let i = 0; i < 16; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

//lesson 5
import { Availability, Issue } from "./types";

async function fetchTasks(
  baseURL: string,
  availability: Availability,
): Promise<Issue[]> {
  var limit = 5;
  if (availability == "Low") {
    var limit = 1;
  } else if (availability == "Medium") {
    var limit = 3;
  };
  const fullURL = `${baseURL}?sort=estimate&limit=${limit}`;
  return getIssues(fullURL, apiKey);
}

// don't touch below this line

const url = "https://api.boot.dev/v1/courses_rest_api/learn-http/issues";
const apiKey = generateKey();

const lowIssues = await fetchTasks(url, "Low");
console.log("Getting issues for low availability user...");
for (const issue of lowIssues) {
  console.log(`Issue: ${issue.title} - estimate: ${issue.estimate}`);
}
console.log("---");

const mediumIssues = await fetchTasks(url, "Medium");
console.log("Getting issues for medium availability user...");
for (const issue of mediumIssues) {
  console.log(`Issue: ${issue.title} - estimate: ${issue.estimate}`);
}
console.log("---");

console.log("Getting issues for high availability user...");
const highIssues = await fetchTasks(url, "High");
for (const issue of highIssues) {
  console.log(`Issue: ${issue.title} - estimate: ${issue.estimate}`);
}

async function getIssues(url: string, apiKey: string): Promise<Issue[]> {
  const response = await fetch(url, {
    method: "GET",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
    },
  });
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
