/*
function main() {
  console.log("Hello, world!");
}

main();
*/

// repl.js actually refers to repl.ts
import { startREPL } from "./repl.js";
import { initState } from "./state.js";

function main() {
  const state = initState();
  startREPL(state);
}

main();