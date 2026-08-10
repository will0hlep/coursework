//lesson 1
export function getTicketInfo(id: string | number): string {
  if (typeof id == "string") {
    id = id.split("-")[1];
  }
  return `Processing ticket: ${id}`;
}

//lesson 2
export function calculateApiCost(numReqs: number, tier?: string) {
  if (tier === "enterprise") {
    return 0.03*numReqs
  } else if (tier === "pro") {
    return 0.05*numReqs
  }
  return 0.1*numReqs
}

//lesson 3
export function estimateResponseTime(promptLength = 100, modelType = "text"): number {
  if (modelType === "text") {
    return estimate(2, 0.01, promptLength);
  } else if (modelType === "image") {
    return estimate(5, 0.02, promptLength);
  } else if (modelType === "code") {
    return estimate(3, 0.05, promptLength);
  } else {
    return 0;
  }
}

function estimate(intercept: number, gradient: number, promptlength: number): number {
  return Math.round(intercept + gradient*promptlength)
}

//leson 5
export type Priority = "low" | "medium" | "high" | "critical";

export function setPriority(level: Priority) {
  if (level === "critical") {
    return 3;
  } else if (level === "high") {
    return 2;
  } else if (level === "medium") {
    return 1;
  } else {
    return 0;
  }
}

//lesson 6
export type LogLevel = "info" | "warn" | "error";
export type LogSourceType = "api" | "database" | "auth";

export type LogMessage = `${LogLevel}: ${string}`
export type LogSource = `${LogSourceType}_${number}`

export function createLogEntry(message: LogMessage, source: LogSource): string {
  return `[${source}] LOG - ${message}`;
}
