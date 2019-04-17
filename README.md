# DronecodeSDK included in Node C++ Addons.

## install
1. Clone with submodules
```
git clone --recurse-submodules https://github.com/aokholm/nodeDronecodeSDK
```

2. Install DronecodeSDK - WIP
```
cd nodeDronecodeSDK/lib/DronecodeSDK/
INSTALL_PREFIX=../../install make default install
```
3. Install node packages
```
cd ../..
npm install
```

4. Start a simulator

Start a (local PX4 simulator)[https://dev.px4.io/en/simulation/jmavsim.html] (in another terminal). For instance:
```
make px4_sitl_default jmavsim
```

5. Run

```
node main.js

```

6. Fail...

Output:

```
before running[12:57:37|Info ] DronecodeSDK version: 0.15.0-18-gac0c1fde (dronecode_sdk_impl.cpp:25)
Wait for system to connect via heartbeat
[12:57:37|Info ] New system on: 127.0.0.1:14580 (udp_connection.cpp:225)
[12:57:37|Debug] New: System ID: 1 Comp ID: 1 (dronecode_sdk_impl.cpp:338)
[12:57:37|Debug] Component Autopilot (1) added. (system_impl.cpp:385)
[12:57:38|Debug] Discovered 1 component(s) (UUID: 5283920058631409231) (system_impl.cpp:548)
Segmentation fault: 11
```


:(

## Debug using XCODE
- change *binding.gyp* from

```
"../lib/DronecodeSDK/install/lib/libdronecode_sdk.a",
"../lib/DronecodeSDK/install/lib/libdronecode_sdk_action.dylib",
"../lib/DronecodeSDK/install/lib/libdronecode_sdk_offboard.dylib",
"../lib/DronecodeSDK/install/lib/libdronecode_sdk_telemetry.dylib"
```

to
```
"lib/DronecodeSDK/install/lib/libdronecode_sdk.a",
"lib/DronecodeSDK/install/lib/libdronecode_sdk_action.dylib",
"lib/DronecodeSDK/install/lib/libdronecode_sdk_offboard.dylib",
"lib/DronecodeSDK/install/lib/libdronecode_sdk_telemetry.dylib"
```

- Follow (this video guide)[https://youtu.be/DND2H2-XfAc] or the below instructions:

- run
```
node-gyp condigure -- -f xcode
```

- open `build/binding.xcodeproject`

- Add a run configuration:

Select `target`, edit scheme
Under, Run>Info>Executable: Select Other
Use cmd-shift-G to enter your path to node.

You can your path to node by entering the retult of `which node`: /usr/local/bin/node

- Edit Arguments
Under, Run>Arguments>Arguments passed on Launch: +
enter path to *main.js* file. for instance `/Users/aokholm/src/kitex/_3_GroundStation/nodeDronecodeSDK/main.js`

- build

Press build.
