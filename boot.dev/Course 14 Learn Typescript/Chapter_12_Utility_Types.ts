//lesson 2
export interface User {
  id: string;
  email: string;
}

export function updateUser(user: Partial<User>) {
  if (user.id) {
    return "can't update id";
  }
  if (user.email) {
    return `updating email to ${user.email}`;
  }
  return "nothing to update";
}

//lesson 3
export interface ContactInfo {
  email?: string;
  phoneNumber?: string;
}

export function addBillingInfo(info: Required<ContactInfo>) {
  return `billing info: ${info.email}, ${info.phoneNumber}`
}

//lesson 4
export interface Config {
  apiUrl: string;
  timeout: number;
  debug: boolean;
}

export function importConfig(config: Readonly<Config>) {
  return config
}

//lesson 5
export type ModelStatus = "waiting" | "thinking" | "responding";

const waitingMessage = "Awaiting prompt";
const thinkingMessage = "Cooking";
const respondingMessage = "Sending response";

export function getStatusMessage(status: ModelStatus) {
  const map: Record<ModelStatus, string> = {
    waiting: waitingMessage,
    thinking: thinkingMessage,
    responding: respondingMessage,
  };

  return map[status];
}

//lesson 6
export interface User {
  id: string;
  name: string;
  email: string;
  age: number;
}

export type UserWithoutID = Pick<User, "name" | "email" | "age">;

export function stripID(user: User): UserWithoutID {
  const { name, email, age } = user;
  return { name, email, age };
}

//lesson 7
export interface User {
  id: string;
  name: string;
  email: string;
  age: number;
}

export type UserWithoutID = Omit<User, "id">;

export function stripID(user: User): UserWithoutID {
  const { name, email, age } = user;
  return { name, email, age };
}
