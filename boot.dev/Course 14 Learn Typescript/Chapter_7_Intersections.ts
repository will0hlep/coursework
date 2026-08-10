//lesson 1
export type SupportBot = {
  id: string;
  name: string;
  status: string;
  language: string;
};

// don't touch above this line

export type TextBot = SupportBot & {
  messageLog: string[];
  sendMessage: (message: string) => string;
}

export type VoiceBot = SupportBot & {
  callLog: string[];
  phoneNumber: string;
  dialNumber: (phoneNumber: string) => string;
}

//lesson 2
type slashCommands = "greet" | "info" | "help";

const greetMessage = "Hello! How can I assist you?";
const infoMessage = "Sure! Here's a list of things I can do...";
const helpMessage = "I can help you with that!";

// don't touch above this line

export function handleSlashCommand(command: slashCommands) {
  if (command === "greet") {
    return greetMessage;
  }
  if (command === "info") {
    return infoMessage;
  }
  if (command === "help") {
    return helpMessage;
  }
  const err: never = command;
  return err;
}

//lesson 3
export type SentimentTag = {
  type: "positive" | "neutral" | "negative";
  score: number;
  flagged: boolean;
};

export type ChannelTag = {
  type: "chat" | "email" | "phone";
  receivedAt: string;
  verified: boolean;
};

export type ReviewMethod = "manual_review" | "auto_process";

// don't touch above this line

export type TicketMetadata = {
  sentiment: SentimentTag;
  channel: ChannelTag;
};

export function getReviewMethod(metadata: TicketMetadata): ReviewMethod {
  const needsReview = metadata.sentiment.flagged || !metadata.channel.verified || metadata.channel.type === "phone";
  return needsReview ? "manual_review" : "auto_process";
}

//lesson 4
export type SupportAgent = {
  id: number;
  role: "agent";
  assignedTickets: number;
};

export type EndUser = {
  id: number;
  role: "customer";
  submittedTickets: number;
};

// don't touch above this line

export type SupportAdmin = {
  id: number;
  role: "admin";
  assignedTickets: number;
};

export type SupportAgentUser = SupportAdmin | SupportAgent | EndUser;

export function getTicketCount(user: SupportAgentUser): number {
  if (user.role === "agent" || user.role === "admin") {
    return user.assignedTickets;
  }
  return user.submittedTickets;
}

//lesson 5
export type EmploymentStatus =
  | "employed"
  | "unemployed"
  | "student"
  | (string & {});

// don't touch below this line

export function updateEmploymentStatus(status: EmploymentStatus) {
  return `Employment status updated: ${status}`;
}
