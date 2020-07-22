const decrypt = (str) => Buffer.from(str, "base64").toString();

const fs = require("fs");
const flag = fs.readFileSync("cipher.txt", "utf8").trim();

let ret = flag;
for (let i = 25; i > 0; i--) ret = decrypt(ret);

console.log(ret);
