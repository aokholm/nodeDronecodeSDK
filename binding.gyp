{
  "targets": [
    {
      "target_name": "bridge",
      "sources": [ "bridge.cc" ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "lib/DronecodeSDK/install/include"
      ],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      'libraries': [
        "lib/DronecodeSDK/install/lib/libdronecode_sdk.a",
        "lib/DronecodeSDK/install/lib/libdronecode_sdk_action.dylib",
        "lib/DronecodeSDK/install/lib/libdronecode_sdk_offboard.dylib",
        "lib/DronecodeSDK/install/lib/libdronecode_sdk_telemetry.dylib"
      ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.14',
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      },
      'conditions': [
        ['OS=="mac"', {
            'cflags+': ['-fvisibility=hidden'],
            'xcode_settings': {
              'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
            }
        }]
      ]
    }
  ]
}

# {
#     'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")"],
#     'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
#     'cflags!': [ '-fno-exceptions' ],
#     'cflags_cc!': [ '-fno-exceptions' ],
#     'xcode_settings': {
#         'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
#         'CLANG_CXX_LIBRARY': 'libc++',
#         'MACOSX_DEPLOYMENT_TARGET': '10.7',
#     },
#     'msvs_settings': {
#         'VCCLCompilerTool': { 'ExceptionHandling': 1 },
#     },
#     ['OS=="mac"', {
#         'cflags+': ['-fvisibility=hidden'],
#         'xcode_settings': {
#           'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
#         }
#     }]
# }
