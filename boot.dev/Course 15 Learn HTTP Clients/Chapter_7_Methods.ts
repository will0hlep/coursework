//lesson 1
import { UserProfile } from "./types";

async function getUsers(url: string, apiKey: string): Promise<UserProfile[]> {
  const response = await fetch(url, {method: "GET", mode: "cors", headers: {"X-API-Key": apiKey}});
  return response.json();
}

// Don't touch below this line

const generatedKey = generateKey();
const url = "https://api.boot.dev/v1/courses_rest_api/learn-http/users";
const users = await getUsers(url, generatedKey);
logUsers(users);

function generateKey(): string {
  const characters = "ABCDEF0123456789";
  let result = "";
  for (let i = 0; i < 16; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

function logUsers(users: UserProfile[]) {
  for (const user of users) {
    console.log(
      `User name: ${user.user.name}, Role: ${user.role}, experience: ${user.experience}, Remote: ${user.remote}`,
    );
  }
}

//lesson 3
import { UserProfile } from "./types";

async function createUser(
  apiKey: string,
  url: string,
  data: UserProfile,
): Promise<UserProfile> {
  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data)
  })
  return response.json();
}

// Don't touch below this line

const userToCreate: UserProfile = {
  role: "Junior Developer",
  experience: 2,
  remote: true,
  user: {
    name: "Dan",
    location: "NOR",
    age: 29,
  },
};

const generatedKey = generateKey();
const url = "https://api.boot.dev/v1/courses_rest_api/learn-http/users";

async function getUsers(url: string, apiKey: string): Promise<UserProfile[]> {
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

function logUsers(users: UserProfile[]) {
  for (const user of users) {
    console.log(
      `User name: ${user.user.name}, Role: ${user.role}, experience: ${user.experience}, Remote: ${user.remote}`,
    );
  }
}

console.log("Retrieving user data...");
const userDataFirst = await getUsers(url, generatedKey);
logUsers(userDataFirst);
console.log("---");

console.log("Creating new user account...");
const creationResponse = await createUser(generatedKey, url, userToCreate);
console.log(`Creation response body: ${JSON.stringify(creationResponse)}`);
console.log("---");

console.log("Retrieving user data...");
const userDataSecond = await getUsers(url, generatedKey);
logUsers(userDataSecond);
console.log("---");

//lesson 5
async function getUserCode(url: string, apiKey: string): Promise<number> {
  const response = await fetch(url, {
    method: "GET",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
    },
  });
  return response.status
}

// Don't touch below this line

const generatedKey = generateKey();

const invalidId = "invalid-id";
const codeFirst = await getUserCode(
  `https://api.boot.dev/v1/courses_rest_api/learn-http/users/${invalidId}`,
  generatedKey,
);
console.log(`id: ${invalidId}, status code: ${codeFirst}`);

const validId = "0194fdc2-fa2f-4cc0-81d3-ff12045b73c8";
const codeSecond = await getUserCode(
  `https://api.boot.dev/v1/courses_rest_api/learn-http/users/${validId}`,
  generatedKey,
);
console.log(`id: ${validId}, status code: ${codeSecond}`);

function generateKey(): string {
  const characters = "ABCDEF0123456789";
  let result = "";
  for (let i = 0; i < 16; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

export {};

//lesson 6
import { UserProfile } from "./types";

async function updateUser(
  baseURL: string,
  id: string,
  data: UserProfile,
  apiKey: string,
): Promise<UserProfile> {
  const fullURL = `${baseURL}/${id}`;
  const response = await fetch(fullURL, {
    method: "PUT",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
    },
    body: JSON.stringify(data)
  });
  return response.json();
}

async function getUserById(
  baseURL: string,
  id: string,
  apiKey: string,
): Promise<UserProfile> {
  const fullURL = `${baseURL}/${id}`;
  const response = await fetch(fullURL, {
    method: "GET",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
    }
  });
  return response.json();
}

// don't touch below this line

const userId = "2f8282cb-e2f9-496f-b144-c0aa4ced56db";
const generatedKey = generateKey();
const baseURL = "https://api.boot.dev/v1/courses_rest_api/learn-http/users";

function generateKey(): string {
  const characters = "ABCDEF0123456789";
  let result = "";
  for (let i = 0; i < 16; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

function logUser(user: UserProfile) {
  console.log(
    `User name: ${user.user.name}, Role: ${user.role}, experience: ${user.experience}, Remote: ${user.remote}`,
  );
}

const userData = await getUserById(baseURL, userId, generatedKey);
logUser(userData);

console.log(`Updating user with id: ${userId}`);
userData.experience = 2;
userData.role = "Junior Developer";
userData.remote = true;
userData.user.name = "Dan";
const updatedUser = await updateUser(baseURL, userId, userData, generatedKey);
logUser(updatedUser);

//lesson 8
import { UserProfile } from "./types";

async function deleteUser(
  baseURL: string,
  id: string,
  apiKey: string,
): Promise<void> {
  const fullURL = `${baseURL}/${id}`;
  await fetch(fullURL, {
  method: "DELETE",
  mode: "cors",
  headers: {
    "X-API-Key": apiKey,
  }
});
}

// don't touch below this line

const userId = "0194fdc2-fa2f-4cc0-81d3-ff12045b73c8";
const generatedKey = generateKey();
const url = "https://api.boot.dev/v1/courses_rest_api/learn-http/users";

async function getUsers(url: string, apiKey: string): Promise<UserProfile[]> {
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

function logUsers(users: UserProfile[]) {
  console.log("Logging user records:");
  for (const user of users) {
    console.log(
      `User name: ${user.user.name}, Role: ${user.role}, experience: ${user.experience}, Remote: ${user.remote}`,
    );
  }
}

const users = await getUsers(url, generatedKey);
logUsers(users);
console.log("---");

await deleteUser(url, userId, generatedKey);
console.log(`Deleted user with id: ${userId}`);
console.log("---");

const newUsers = await getUsers(url, generatedKey);
logUsers(newUsers);
console.log("---");
