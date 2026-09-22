import { commandMap, commandMapBack } from "./command_map.js";
import { commandHelp } from "./command_help.js";
import { commandExit } from "./command_exit.js";
import { CLICommand } from "./state.js";

export function getCommands(): Record<string, CLICommand> {
  return {

    exit: {
      name: "exit",
      description: "Exit the Pokedex",
      callback: commandExit
    },

    help: {
        name: "help",
        description: "Display available commands",
        callback: commandHelp
        },

    map: {
        name: "map",
        description: "displays the names of location areas in the Pokemon world",
        callback: commandMap
    },

    mapb: {
        name: "mapb",
        description: "displays the names of location areas in the Pokemon world",
        callback: commandMapBack
    }

    // can add more commands here
  };
}