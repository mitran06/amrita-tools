import { parseRollNumber, getBatchDisplay, getProgrammeDisplay } from './rollNumberParser.js';

const sampleRoll = 'BL.EN.U4EAC24041';

console.log(parseRollNumber(sampleRoll));
console.log(getBatchDisplay(sampleRoll));
console.log(getProgrammeDisplay(sampleRoll));
