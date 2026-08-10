//lesson 1
export type SupportRequest = {
  id: string;
  severity: RequestSeverity;
  description: string;
};

// don't touch above this line

export enum RequestSeverity {
  Low,
  Medium,
  High,
  Critical
}

export function isCritical(request: SupportRequest) {
  return (request.severity === RequestSeverity.Critical)
}

//lesson 2
export type SupportRequest = {
  id: string;
  severity: RequestSeverity;
  description: string;
};

// don't touch above this line

export enum RequestSeverity {
  Low = "LOW",
  Medium = "WARN",
  High = "INFO",
  Critical = "DEBUG"
};

export function convertSeverityToLabel(severity: number) {
  if (severity === 0) {
    return RequestSeverity["Low"];
  } else if (severity === 1) {
    return RequestSeverity["Medium"];
  } else if (severity === 2) {
    return RequestSeverity["High"];
  } else if (severity === 3) {
    return RequestSeverity["Critical"];
  }
  throw new Error("Unknown severity");
}

//lesson 3
export enum InternalErrors {
  InvalidPrompt = 1001,
  ContextWindowOverflow = 1004,
  ModelOverload = 1420,
  EthicalGuardrailTriggered = 2233,
  TokenLimitExceeded = 2401,
  SelfAwarenessAchieved = 9999,
}

// don't touch above this line

export function getErrorLabel(error_code: number): string {
  let error_label = InternalErrors[error_code]
  if (error_label) {
    return `${error_code}: ${InternalErrors[error_code]}`
  }
  return `${error_code}: Unknown error`
}

//lesson 5
export type ApiTier = "Free" | "Basic" | "Pro" | "Enterprise";

export function getRateLimitForTier(tier: ApiTier) {
switch (tier) {
    case "Free":
      return 10;
    case "Basic":
      return 100;
    case "Pro":
      return 1000;
    case "Enterprise":
      return 10000;
}
