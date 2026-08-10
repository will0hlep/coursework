let NAME = "test"

//const {moo} = require("./moo.js");
import {moo} from "./moo.js";
import {say} from "./node_modules/cowsay";

console.log(say({ text: moo(NAME)}));