//lesson 1
export function getFirst<T>(arr: T[]): T | undefined {
  if (arr) {
    return arr[0];
  }
  return undefined;
}

//lesson 2
export function pair<A, B>(a: A[], b: B[]): [A, B][] {
  let list_length = Math.min(a.length,b.length);
  let output_list: [A, B][] = []
  for (let i = 0; i < list_length; i++) {
    output_list.push([a[i], b[i]])
  }
  return output_list
}

//lesson 3
interface Email{
  email: string
}

export function pluckEmails<T extends Email>(arr: T[]) {
  let output_list = []
  for (let element of arr) {
    output_list.push(element.email)
  }
  return output_list
}

//lesson 4
interface JobQueue<T> {
  push(job: T): void;
  next(): T | undefined;
}

export function runNext<T>(jobQueue: JobQueue<T>): T | undefined {
  return jobQueue.next()
}

export function createQueue<T>(): JobQueue<T> {
  const jobs: T[] = [];
  return {
    push(job) {
      jobs.push(job);
    },
    next() {
      return jobs.shift();
    },
  };
}

//lesson 5
type ObjectWithText = {
  text: string;
};

const Transformer = <T>(data: { text: string }): string => data.text;

export function summarizeFeedback<T>(
  data: { text: string }[],
): string[] {
  return transform(data, Transformer);
}

// don't touch below this line

function transform<T, R>(inputs: T[], fn: (item: T) => R): R[] {
  const result: R[] = [];
  for (const item of inputs) {
    result.push(fn(item));
  }
  return result;
}

//lesson 6
export class FeatureFlag<T extends string> {
  #flags: Set<T>;

  constructor() {
    this.#flags = new Set<T>();
  }

  enable(flag: T): void {
    this.#flags.add(flag);
  }

  isEnabled(flag: T): boolean {
    return this.#flags.has(flag);
  }
}