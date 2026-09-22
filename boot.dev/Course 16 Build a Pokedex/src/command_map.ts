import type { State } from "./state.js";
import { PokeAPI } from "./pokeapi.js";

export async function commandMap(state: State) {
    const locations = await state.pokeapi.fetchLocations(state.nextLocationsURL);
    state.nextLocationsURL = locations.next ?? "";
    state.prevLocationsURL = locations.previous ?? "";
    locations.results.forEach((location) => {
        console.log(location.name);
    });
};

export async function commandMapBack(state: State) {
    if (!state.prevLocationsURL) {
        console.log("you're on the first page");
        return;
    }
    const locations = await state.pokeapi.fetchLocations(state.prevLocationsURL);
    state.nextLocationsURL = locations.next ?? "";
    state.prevLocationsURL = locations.previous ?? "";
    locations.results.forEach((location) => {
        console.log(location.name);
    });
};