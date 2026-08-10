//lesson 1
type RegularCustomer = {
  plan: "regular";
  tickets: number;
  aboveLimit: boolean;
};

type PremiumCustomer = {
  plan: "premium";
  tickets: number;
};

export type Customer = RegularCustomer | PremiumCustomer;

export function openTicket(customer: Customer): number {
  if (customer.plan === "regular" && customer.aboveLimit) {
    return -1;
  }
  return customer.tickets + 1;
}

//lesson 2
export type CustomerMessage = {
  content: string;
  source: "chat" | "email" | "unknown";
}

export function parseCustomerMessage(input: unknown): CustomerMessage {
  if (typeof input === "string") {
    return {content: input, source: "email"};
  } else if (Array.isArray(input)) {
    return {content: input.join("\n"), source: "chat"};
  } else {
    return {content: "", source: "unknown"};
  }
}

//lesson 3
type PositiveSentiment = "happy" | "satisfied";
type NegativeSentiment = "dissatisfied" | "angry";

export type Sentiment = PositiveSentiment | NegativeSentiment;
export type Response = { message: string; notify: boolean };

export function respondToSentiment(sentiment: Sentiment): Response {
  if (sentiment === "happy" || sentiment === "satisfied") {
    return handlePositiveSentiment(sentiment);
  } else if (sentiment === "dissatisfied" || sentiment === "angry") {
    return handleNegativeSentiment(sentiment);
  } else {
    return {message: "We don't understand.", notify: true}
  }
}

function handlePositiveSentiment(sentiment: PositiveSentiment): Response {
  if (sentiment == "happy") {
    return {message: "Hooray!", notify: false}
  } else {
    return {message: "We are glad.", notify: false}
  }
}

function handleNegativeSentiment(sentiment: NegativeSentiment): Response {
  if (sentiment == "dissatisfied") {
    return {message: "We are sorry.", notify: false}
  } else {
    return {message: "We apologize. A manager will contact you.", notify: true}
  }
}

//lesson 4
type ImageAttachment = {
  fileSize: number;
  width: number;
  height: number;
};

type DocumentAttachment = {
  fileSize: number;
  numPages: number;
};

type FileAttachment = {
  fileSize: number;
};

export type Attachment = ImageAttachment | DocumentAttachment | FileAttachment;

export function processAttachment(attachment: Attachment) {
  if ("width" in attachment) {
    return `Attached image, size: ${attachment.fileSize}, dimensions: ${attachment.width}x${attachment.height}`
  } else if ("numPages" in attachment) {
    return `Attached document, size: ${attachment.fileSize}, pages: ${attachment.numPages}`
  } else {
    return `Attached file, size: ${attachment.fileSize}`
  }
}

//lesson 5
type ModelSkippity = {
  version: "3.5" | "4" | "4s";
  search: boolean;
};

type ModelJean = {
  version: "2" | "3" | "3.14";
  think: boolean;
};

export type Model = ModelSkippity | ModelJean;

function isModelSkippity(model: Model): model is ModelSkippity {
  return (
    "search" in model &&
    (model.version === "3.5" || model.version === "4" || model.version === "4s")
  );
}

function isModelJean(model: Model): model is ModelJean {
  return (
    "think" in model &&
    (model.version === "2" || model.version === "3" || model.version === "3.14")
  );
}

export function activateModel(model: Model) {
  if (isModelSkippity(model)) {
    return `Activated model Skippity version ${model.version} with searching ${model.search? "enabled": "disabled"}`
  } else if (isModelJean(model)) {
    return `Activated model Jean version ${model.version} with thinking ${model.think? "enabled": "disabled"}`
  }
}

//lesson 6
export type Topic = "question" | "complaint" | "upgrade" | "refund";

type Chat = {
  topic: Topic;
  userId: string;
};

type CountReport = {
  questions: number;
  complaints: number;
  upgrades: number;
  refunds: number;
};

export function countComplaints(chats: Chat[]): CountReport {
  let counts = { questions: 0, complaints: 0, upgrades: 0, refunds: 0 };
  for (const chat of chats) {
    counts = incrementCount(chat, counts);
  }
  return counts;
}

function incrementCount(chat: Chat, counts: CountReport): CountReport {
  switch (chat.topic) {
    case "question":
      counts.questions++;
      return counts;
    case "complaint":
      counts.complaints++;
      return counts;
    case "refund":
      counts.refunds++;
      return counts;
    case "upgrade":
      counts.upgrades++;
      return counts;
  }
}

//lesson 7
export type UserFeedback = {
  email?: string;
  rating?: number;
};

export function handleFeedback(feedback: UserFeedback) {
  if (feedback.rating === undefined || !isValidRating(feedback.rating)) {
    return "Give a rating between 1 and 5.";
  } else if (feedback.email === undefined || !feedback.email.includes("@")) {
    return "Provide a valid email address.";
  }
  return `Thanks, ${getEmailUsername(feedback.email)}! Rating: ${ratingToString(feedback.rating)}`;
}

function getEmailUsername(email: string): string {
  const atIndex = email.indexOf("@");
  return atIndex !== -1 ? email.slice(0, atIndex) : email;
}

function isValidRating(rating: number): rating is 1 | 2 | 3 | 4 | 5 {
  return (
    rating === 1 || rating === 2 || rating === 3 || rating === 4 || rating === 5
  );
}

function ratingToString(rating: 1 | 2 | 3 | 4 | 5): string {
  switch (rating) {
    case 1:
      return "Very Bad";
    case 2:
      return "Bad";
    case 3:
      return "Average";
    case 4:
      return "Good";
    case 5:
      return "Excellent";
  }
}

//lesson 8
export type OrderData = {
  id: string;
  accountType: "free" | "premium";
  amount: number;
  contact: {
    email: string;
    phone: string;
  };
};

export function handleSuccessfulOrder(orderResponse: unknown): string {
  const { accountType, contact } = orderResponse as OrderData;

  let welcome: string;
  switch (accountType) {
    case "free":
      welcome = "Welcome to Support.ai!";
      break;
    case "premium":
      welcome = "Thanks for giving us money!";
      break;
  }

  return `To ${contact.email}: ${welcome}`;
}

//lesson 10
export type OrderData = {
  id: string;
  accountType: "free" | "premium";
  amount: number;
  contact: {
    email: string;
    phone: string;
  };
};

export function reportOrders(orders: OrderData[] | null): string {
  /*
  let total = 0;
  for (let order of orders!) {
    total += order.amount;
  }
  */
  return `Total amount for orders: ${orders!.reduce((acc, o) => o.amount + acc, 0)}`
}
