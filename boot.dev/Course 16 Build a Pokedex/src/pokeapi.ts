export class PokeAPI {
  private static readonly baseURL = "https://pokeapi.co/api/v2";

  constructor() {}

  async fetchLocations(pageURL?: string): Promise<ShallowLocations> {
    const url = (pageURL === "" || pageURL === undefined ? `${PokeAPI.baseURL}/location-area?offset=0&limit=20` : pageURL);
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  }

  async fetchLocation(locationName: string): Promise<Location> {
    const url = `${PokeAPI.baseURL}/location-area/${locationName}`;
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  }
}

export type ShallowLocations = {
  count: number;
  next: string | null;
  previous: string | null;
  results: {
    name: string;
    url: string;
  }[];
};

export type Location = {
  id: number;
  name: string;
  game_index: number;
  encounter_method_rates: {
    encounter_method: {
      name: string;
      url: string;
    };
    version_details: {
      rate: number;
      version: {
        name: string;
        url: string;
      };
    }[];
  }[];
  location: {
    name: string;
    url: string;
  };
  names: {
    name: string;
    language: {
      name: string;
      url: string;
    }
  }[]
  pokemon_encounters: {
    pokemon: {
      name: string;
      url: string;
    };
    version_details: {
      version: {
        name: string;
        url: string;
      };
      max_chance: number;
      encounter_details: {
        min_level: number;
        max_level: number;
        chance: number;
        method: {
          name: string;
          url: string;
        };
        condition_values: any[];
        pokemon_details: any;
      }[];
    }[];
  }[];
};
