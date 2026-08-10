//lesson 1
export function createTicket(
  prevTicket: number,
  comment: string,
): [number, string, boolean] {
  const isCritical = comment.toLowerCase().includes("critical");
  return [prevTicket + 1, comment, isCritical];
}

//lesson 2
export type Ticket = readonly [number, string, boolean, boolean];

// don't touch above this line

export function resolveTicket(ticket: Ticket): [number, string, boolean, boolean] {
  return [ticket[0], ticket[1], ticket[2], true]
}

//lesson 5
export type Ticket = readonly [id: number, comment: string, label: string];

// don't touch above this line

export function formatTicket(ticket: Ticket) {
  const [id, comment, label] = ticket;
  return `#${id} ${comment} [${label}]`;
}

//lesson 6
export type Ticket = readonly [id: number, comment: string, label?: string];

export function formatTicket(ticket: Ticket): string {
  const [id, comment, label] = ticket;
  return `#${id} ${comment}${label ? ` [${label}]` : ""}`;
}

//lesson 7
export function tokenize(input: string): [number, ...string[]] {
  let tokens = input.split(" ")
  let cost = tokens.length / 100
  return [cost, ...tokens];
}