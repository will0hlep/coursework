//lesson 1
import { Project } from "./types";

async function getProjects(): Promise<Project[]> {
  const url = "https://api.boot.dev/v1/courses_rest_api/learn-http/projects";
  const response = await fetch(url, {
    method: "GET",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
      "Content-Type": "application/json",
    },
  });
  const javascriptObjectResponse = await response.json();
  return javascriptObjectResponse;
}

// Don't touch below this line

const apiKey = generateKey();

const projects = await getProjects();
console.log("Got some projects from the server.");
for (const project of projects) {
  console.log(`- title: ${project.title}, assignees: ${project.assignees}`);
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
import { Project } from "./types";

async function updateProjectById(id: string, projectObj: Project) {
  const path = `https://api.boot.dev/v1/courses_rest_api/learn-http/projects/${id}`;
  const response = await fetch(path, {
    method: "PUT",
    mode: "cors",
    headers: getHeaders(),
    body: JSON.stringify(projectObj),
  });
  return response.json();
}

// Don't touch below this line

const apiKey = generateKey();
const projectID = "0194fdc2-fa2f-4cc0-81d3-ff12045b73c8";

const project = await getProjectById(projectID);
console.log(
  `Project '${project.title}' fetched. Data: ${JSON.stringify(project)}`,
);

project.completed = true;
await updateProjectById(projectID, project);
console.log(`Project '${project.title}' was completed!`);

const updatedProject = await getProjectById(projectID);
console.log(
  `Project '${updatedProject.title}' fetched. Data: ${JSON.stringify(updatedProject)}`,
);

function generateKey(): string {
  const characters = "ABCDEF0123456789";
  let result = "";
  for (let i = 0; i < 16; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  return result;
}

async function getProjectById(id: string): Promise<Project> {
  const path = `https://api.boot.dev/v1/courses_rest_api/learn-http/projects/${id}`;
  const response = await fetch(path, {
    method: "GET",
    mode: "cors",
    headers: {
      "X-API-Key": apiKey,
      "Content-Type": "application/json",
    },
  });
  return response.json();
}

function getHeaders(): Record<string, string> {
  return {
    "X-API-Key": apiKey,
    "Content-Type": "application/json",
  };
}

//lesson 4
function parseProject(projectString: string): void {
  try {
    const parsedproject = JSON.parse(projectString);
    printProjectObj(parsedproject)
  } catch {
    console.log("invalid json string")
  }
}

// don't touch below this line

import { Project } from "./types";

function printProjectObj(parsed: Project) {
  console.log(`id: ${parsed.id}`);
  console.log(`completed: ${parsed.completed}`);
  console.log(`title: ${parsed.title}`);
  console.log(`assignees: ${parsed.assignees}`);
}

parseProject(`
{
  "completed": false,
  "id": "0194fdc2-fa2f-4cc0-81d3-ff12045b73c8",
  "title": "Unfidget the widget",
  "assignees": 14
}
`);

console.log("---");

parseProject(`
{
  "completed":true,
  "id":"2f8282cb-e2f9-496f-b144-c0aa4ced56db",
  "title":"Re-spaghettify the codebase - things broke",
  "assignees": 2
}
`);

console.log("---");

parseProject(`
{
  "completed": false,
  "id":"0f12951e-0a74-4846-a1e0-10b33b13112f"
  "title":"Report quarterly earnings",
  "assignees": 1
}
`);
