var bridge = require('bindings')('bridge');

setTimeout( () => {
    console.log(bridge.hello());
}, 2000);

// console.log(bridge.hello())
