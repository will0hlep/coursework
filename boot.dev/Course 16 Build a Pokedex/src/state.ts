import { createInterface, type Interface } from "readline";
import { getCommands } from "./command.js";
import { PokeAPI } from "./pokeapi.js";

export type State = {
  interface: Interface;
  commands: Record<string, CLICommand>;
  pokeapi: PokeAPI;
  nextLocationsURL?: string;
  prevLocationsURL?: string;
};

export function initState(): State {
  return ({
    interface: createInterface({
      input: process.stdin,
      output: process.stdout,
      prompt: "Pokedex > "
    }),
    commands: getCommands(),
    pokeapi: new PokeAPI(),
    nextLocationsURL: "",
    prevLocationsURL: ""
  });
}

export type CLICommand = {
  name: string;
  description: string;
  callback: (state: State) => Promise<void>;
};