//import { cleanInput } from "./repl.js";
import { describe, expect, test } from "vitest";
import { Cache } from "./pokecache.js";

test.concurrent.each([
  {
    key: "https://example.com",
    val: "testdata",
    interval: 500, // 1/2 second
  },
  {
    key: "https://example.com/path",
    val: "moretestdata",
    interval: 700, // 1 second
  },
])("Test Caching $interval ms", async ({ key, val, interval }) => {
  const cache = new Cache(interval);

  cache.add(key, val);
  const cached = await cache.get(key);
  expect(cached).toBe(val);

  await new Promise((resolve) => setTimeout(resolve, 2 * interval));
  const reaped = await cache.get(key);
  expect(reaped).toBe(undefined);

  cache.stopReapLoop();
});
