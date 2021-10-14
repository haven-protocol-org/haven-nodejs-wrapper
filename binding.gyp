{
    "targets": [
        {
            "target_name": "havennodejswrapper",
            "sources": [
                "src/main.cc",
                "haven-main/src/cryptonote_basic/cryptonote_basic_impl.cpp",
                "haven-main/src/cryptonote_basic/cryptonote_format_utils.cpp",
                "haven-main/src/crypto/tree-hash.c",
                "haven-main/src/crypto/crypto.cpp",
                "haven-main/src/crypto/crypto-ops.c",
                "haven-main/src/crypto/crypto-ops-data.c",
                "haven-main/src/crypto/hash.c",
                "haven-main/src/crypto/keccak.c",
                "haven-main/src/common/base58.cpp",
                "haven-main/src/offshore/pricing_record.cpp",
                "haven-main/contrib/epee/src/mlocker.cpp",
            ],
            "include_dirs": [
		"haven-main/src",
                "haven-main/external/easylogging++",
                "haven-main/contrib/epee/include",
                "<!(node -e \"require('nan')\")",
            ],
            "link_settings": {
                "libraries": [
                    "-lboost_system",
                    "-lboost_chrono",
                    "-lboost_date_time",
		    "-lboost_thread",
                ]
            },
            "cflags_c":  [
                "-fno-exceptions -std=gnu11 -march=native -fPIC -DNDEBUG -Ofast -funroll-loops -fvariable-expansion-in-unroller -ftree-loop-if-convert-stores -fmerge-all-constants -fbranch-target-load-optimize2"
            ],
            "cflags_cc": [
                "-fexceptions -frtti -std=gnu++11 -march=native -fPIC -DNDEBUG -Ofast -s -funroll-loops -fvariable-expansion-in-unroller -ftree-loop-if-convert-stores -fmerge-all-constants -fbranch-target-load-optimize2"
            ],
            "xcode_settings": {
                "OTHER_CFLAGS": [ "-fexceptions -frtti" ]
            }
        }
    ]
}
