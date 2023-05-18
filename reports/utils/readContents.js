const { resolve } = require('path');
const { readdir } = require('fs').promises;

const args = process.argv.slice(2);

const [baseDirectory] = args;

run();

async function run() {
    result = await getFiles(baseDirectory);
    console.log(result);
}

async function getFiles(dir) {
  const dirents = await readdir(dir, { withFileTypes: true });
  const files = await Promise.all(dirents.map((dirent) => {
    const res = resolve(dir, dirent.name);
    return dirent.isDirectory() ? getFiles(res) : res;
  }));
  return Array.prototype.concat(...files);
}
