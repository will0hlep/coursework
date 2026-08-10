//lesson 1
export function calculateTotal(
  price: number,
  quantity: number,
  discount: number,
): number {
  return price * quantity * (1 - discount);
}

//lesson 2
export function combinePrompts(systemPrompt: string, userPrompt: string) {
  return systemPrompt + "\n" + userPrompt
}

//lesson 3
export function logSystemEvent(event: string, 
  severity: "info" | "warning" | "error"
): string {
  return `SYSTEM ${severity.toUpperCase()}: ${event}`;
}

//lesson 5
export type SupportResponse = (name: string) => string;

export function greetCustomer(name: string): string {
  return `Hello ${name}, welcome to Support.ai! How can I assist you today?`;
}

export function farewellCustomer(name: string): string {
  return `Goodbye ${name}, have a great day!`;
}
