console.log("本日は晴天なり！");
let name = "田中";
console.log(name);
console.log(`${name}さんは部長です！`);
const animals = ["cat", "dog"];
console.log(animals);

const menus = ["caffee", "tea", "bread"];

for(let i = 0; i < 3; i++) {
  console.log(menus[i]);
}

const numbers = [1, 2, 3, 4, 5, 6];

const evenNumbers = numbers.filter((number) =>{
  return number % 2 === 0;
});

console.log(evenNumbers);

const numbers = [1, 2, 3, 4];
const doubledNumbers = numbers.map((number) => {
  return number * 2;
});

import React from 'react';
class App extends React.Component {
  render(){
    <div>
      <button>
        Hello!
      </button>
    </div>
  }
}