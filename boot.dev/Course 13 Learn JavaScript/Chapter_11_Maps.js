//lesson 1
function addToPhonebook(phoneNumber, name, phoneBook) {
  const mapCopy = new Map(phoneBook);
  mapCopy.set(phoneNumber, name)
  return mapCopy
}

// don't touch below this line

export { addToPhonebook };

//lesson 2
function createUserMap(users) {
  const map = new Map();
  for (let user of users) {
    map.set(user.fname + " " + user.lname, user);
  }
  return map;
}

export { createUserMap };

//lesson 3
function fixUserMap(brokenMap) {
  const fixedMap = new Map();
  for (const [key, value] of brokenMap) {
    fixedMap.set(key.fname + " " + key.lname, value);
  }
  return fixedMap;
}

export { fixUserMap };
