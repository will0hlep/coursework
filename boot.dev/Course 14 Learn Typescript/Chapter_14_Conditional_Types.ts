//lesson 1
export type SentimentString<T> = T extends { angry: true } ? "mad" | "furious" : "content" | "happy";

//lesson 2
export type InputTypeOf<T> = T extends (arg: infer R) => any ? R : unknown;

//lesson 3
export type Blank<T> = {
  [K in keyof T]: null;
};

export function resetForm<T>(form: T): Blank<T> {
  const result = {} as Blank<T>;
  for (const key in form) {
    result[key] = null;
  }
  return result;
};

//lesson 4
export type EditableFields<T> = {
  [K in keyof T]: T[K] extends Function | object ? never : T[K];
};

//lesson 5
export type NumberKeys<T> = {
  [K in keyof T]: T[K] extends number ? K : never;
}[keyof T];