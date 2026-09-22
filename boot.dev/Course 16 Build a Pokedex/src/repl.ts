import { initState, State } from './state.js';


export function startREPL(state: State) {
    state.interface.prompt();
    state.interface.on('line', async (input) => {
        try {
            for (const command in state.commands) {
                if (input.trim().toLowerCase() === command) {
                    await state.commands[command].callback(state);
                    break;
                }
            }
        } catch (error) {
            console.error("An error occurred:", error);
        }
        state.interface.prompt();
    });
}


/*
export function cleanInput(input: string): string[] {
    // logic goes here
    return input.toLowerCase().split(' ').filter(str => str !== "");
}
*/


        /*
        if (input === "exit") {
            commandExit();
        } else if (input === "help") {
            commandHelp();
        } else {
            console.log(`Unknown command`);
        }
        */
        /*
            if (input !== "") {
        console.log(`Your command was: ${cleanInput(input)[0]}`);
        }
        */