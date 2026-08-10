import { initState } from './state.js';


export function startREPL() {
    const programinterface = initState()
    programinterface.interface.prompt();
    programinterface.interface.on('line', async (input) => {
        try {
            for (const command in programinterface.commands) {
                if (input === command) {
                    await programinterface.commands[command].callback(programinterface);
                    break;
                }
            }
        } catch (error) {
            console.error("An error occurred:", error);
        }
        programinterface.interface.prompt();
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