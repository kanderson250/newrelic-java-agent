const { resolve } = require('path');
const { createWriteStream } = require('fs');
const { readdir, writeFile } = require('fs').promises;

const args = process.argv.slice(2);

const [baseDirectory, destinationPath] = args;

run();

async function run() {
    result = await getFiles(baseDirectory);
    console.log(result);
    writeFilesTo(result, destinationPath);
}

function writeFilesTo(files, destinationPath) {
  var stream = createWriteStream(destinationPath);
  files.forEach(file => {
    stream.write(file + '\n')
  });
  stream.end();
}

async function getFiles(dir) {
  const dirents = await readdir(dir, { withFileTypes: true });
  const files = await Promise.all(dirents.map((dirent) => {
    const res = resolve(dir, dirent.name);
    return dirent.isDirectory() ? getFiles(res) : res;
  }));
  return Array.prototype.concat(...files);
}
