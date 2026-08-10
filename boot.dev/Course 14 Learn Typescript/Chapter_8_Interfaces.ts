//lesson 1
export interface UserFeedback {
  rating: number;
  comment: string;
}

export interface SupportSession {
  id: string;
  startedAt: number;
  endedAt: number;
  feedback: UserFeedback;
}

export function getSessionDuration(session: SupportSession) {
  return session.endedAt - session.startedAt;
}

//lesson 2
export interface Message {
  id: string;
  sender: string;
  recipient: string;
  timestamp: number;
}

// don't touch above this line

export interface TextMessage extends Message {
  text: string;
  carrier: string;
}

export interface EmailMessage extends Message {
  subject: string;
  body: string;
}

export function getEmailDescription(email: EmailMessage): string {
  return `[EMAIL] ${email.subject}: ${email.body}`;
}

export function getTextMessageDescription(text: TextMessage): string {
  return `[TEXT] ${text.text}` + ` - Sent via ${text.carrier}`;
}

//lesson 3
export interface CanReply {
  reply(text: string): string;
}

export interface CanSummarize {
  summarize(conversation: string[]): string;
}

export interface CanAct {
  takeAction(action: string): void;
}

// don't touch above this line

export interface SmartReplyBot extends CanReply, CanSummarize, CanAct {
  name: string
  status: "online" | "offline" | "starting"
  shutdown: () => string;
}

//lesson 4
export interface SystemEvent {
  type: string;
  timestamp: number;
  payload: string | object;
  affectedService: string;
  severity: "low" | "medium" | "high" | "critical";
}

// don't touch above this line

export interface ErrorEvent extends SystemEvent {
  type: "error";
  payload: string;
  code: number;
}

export interface OutageEvent extends SystemEvent {
  type: "outage";
  durationSeconds: number;
  severity: "critical";
}

export function getHighPriorityEvents(events: SystemEvent[]) {
  return events.filter(
    (event) => event.severity === "high" || event.severity === "critical",
  );
}
