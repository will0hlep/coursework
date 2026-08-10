//lesson 1
interface JelloIssue {
  id: string;
  title: string;
}

export function validateIssue(data: any): JelloIssue {
  if (typeof data.id !== "string") {
    throw new Error("Invalid id");
  }
  if (typeof data.title !== "string") {
    throw new Error("Invalid title");
  }
  return data as JelloIssue;
}

//lesson 2
import { z } from "zod";

export const JelloIssueSchema = z.object({
  id: z.string(),
  title: z.string().min(1)
})

//lesson 3
import { z } from "zod";

const JelloIssueSchema = z.object({
  id: z.string(),
  title: z.string().min(1),
  status: z.string(),
});

export type JelloIssue = z.infer<typeof JelloIssueSchema>;

export async function fetchJelloIssue(): Promise<JelloIssue[]> {
  const res = await fetch("https://api.boot.dev/v1/courses_rest_api/learn-http/issues");
  const data = await res.json();
  if (!Array.isArray(data)) {
    throw new Error("bollocks");
  }
  var output = [];
  for (var issue of data) {
    output.push(JelloIssueSchema.parse(issue))
  }
  return output
}
