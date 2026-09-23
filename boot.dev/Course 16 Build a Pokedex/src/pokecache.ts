export type CacheEntry<T> = {
    createdAt: number;
    val: T;
};

export class Cache {
  #cache = new Map<string, CacheEntry<any>>();
  #reapIntervalId: NodeJS.Timeout | undefined = undefined;
  #interval: number;

  async add<T>(key: string, val: T) {
    const entry: CacheEntry<T> = {
      createdAt: Date.now(),
      val
    };
    this.#cache.set(key, entry);
  }

  async get<T>(key: string) {
    return this.#cache.get(key)?.val;
  }

  #reap() {
    const now = Date.now() - this.#interval;
    for (const [key, entry] of this.#cache.entries()) {
      if (entry.createdAt < now) {
        this.#cache.delete(key);
      }
    }
  }

  #startReapLoop() {
    this.#reapIntervalId = setInterval(() => this.#reap(), this.#interval);
  }

  stopReapLoop() {
    if (this.#reapIntervalId) {
      clearInterval(this.#reapIntervalId);
      this.#reapIntervalId = undefined;
    }
  }

  constructor(interval: number) {
    this.#interval = interval;
    this.#startReapLoop();
  }
}
