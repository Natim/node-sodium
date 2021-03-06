{
    'targets': [{
            'target_name': 'libsodium',
            'variables': {
                'naclversion': '0.4.5',
                'target_arch%': 'ia32'
            },
            'type': 'static_library',
            #Overcomes an issue with the linker and thin.a files on SmartOS 'standalone_static_library': 1,
            'dependencies': [],
            'defines': [
                    '__amd64__',
                    '__ELF__',
                    'SODIUM_STATIC',
                    'HAVE_AMD64_ASM=1',
                    'SODIUM_HAVE_AMD64_ASM',
                    'STDC_HEADERS=1',
                    'HAVE_SYS_TYPES_H=1',
                    'HAVE_SYS_STAT_H=1',
                    'HAVE_STDLIB_H=1',
                    'HAVE_STRING_H=1',
                    'HAVE_MEMORY_H=1',
                    'HAVE_STRINGS_H=1',
                    'HAVE_INTTYPES_H=1',
                    'HAVE_STDINT_H=1',
                    'HAVE_UNISTD_H=1',
                    '__EXTENSIONS__=1',
                    '_ALL_SOURCE=1',
                    '_GNU_SOURCE=1',
                    '_POSIX_PTHREAD_SEMANTICS=1',
                    '_TANDEM_SOURCE=1',
                    'HAVE_DLFCN_H=1',
                    'LT_OBJDIR=\".libs/\"',
                    'HAVE_EMMINTRIN_H=1',
                    'HAVE_TMMINTRIN_H=1',
                    'HAVE_SMMINTRIN_H=1',
                    'HAVE_IMMINTRIN_H=1',
                    'HAVE_X86INTRIN_H=1',
                    'HAVE_WMMINTRIN_H=1',
                    'HAVE_FENV_H=1',
                    'NATIVE_LITTLE_ENDIAN=1',
                    'HAVE_AMD64_ASM=1',
                    'HAVE_TI_MODE=1',
                    'HAVE_CPUID=1',
                    'HAVE_LIBM=1'
            ],
            'include_dirs': [
                    'libsodium-<(naclversion)/src/libsodium/include/sodium',
            ],
            'xcode_settings': {
                'OTHER_CFLAGS': [
                        '-fPIC',
                        '-fwrapv',
                        '-fno-strict-aliasing',
                        '-fstack-protector-all',
                        '-Winit-self',
                        '-Wwrite-strings',
                        '-Wdiv-by-zero',
                        '-Wmissing-braces',
                        '-Wmissing-field-initializers',
                        '-Wno-sign-compare',
                        '-Wno-unused-const-variable',
                        '-g',
                        '-O2',
                        '-fvisibility=hidden',
                        '-Wno-missing-field-initializers',
                        '-Wno-missing-braces',
                        '-Wno-unused-function',
                        '-Wno-strict-overflow',
                        '-Wno-unknown-pragmas'
                ],
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
            },
            '!cflags': ['-fno-exceptions'],
            'cflags': [
                    '-fexceptions',

                '-Winit-self',
                    '-Wwrite-strings',
                    '-Wdiv-by-zero',
                    '-Wmissing-braces',
                    '-Wmissing-field-initializers',
                    '-Wno-sign-compare',
                    '-Wno-unused-but-set-variable',
                    '-g',
                    '-O2',
                    '-Wno-unknown-pragmas',
                    '-Wno-missing-field-initializers',
                    '-Wno-missing-braces'
            ],
            'ldflags': [
                    '-pie',
                    '-Wl',
                    '-z',
                    'relro'
                '-z',
                    'now'
                '-Wl',
                    '-z',
                    'noexecstack'
            ],

            'sources': [
                    'libsodium-<(naclversion)/src/libsodium/crypto_auth/crypto_auth.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_auth/hmacsha256/auth_hmacsha256_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_auth/hmacsha256/ref/hmac_hmacsha256.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_auth/hmacsha256/ref/verify_hmacsha256.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_auth/hmacsha512256/auth_hmacsha512256_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_auth/hmacsha512256/ref/hmac_hmacsha512256.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_auth/hmacsha512256/ref/verify_hmacsha512256.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_box/crypto_box.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_box/curve25519xsalsa20poly1305/box_curve25519xsalsa20poly1305_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/after_curve25519xsalsa20poly1305.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/before_curve25519xsalsa20poly1305.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/box_curve25519xsalsa20poly1305.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_box/curve25519xsalsa20poly1305/ref/keypair_curve25519xsalsa20poly1305.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/hsalsa20/ref2/core_hsalsa20.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/hsalsa20/core_hsalsa20_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/salsa20/ref/core_salsa20.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/salsa20/core_salsa20_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/salsa2012/ref/core_salsa2012.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/salsa2012/core_salsa2012_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/salsa208/ref/core_salsa208.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_core/salsa208/core_salsa208_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_generichash/crypto_generichash.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_generichash/blake2/generichash_blake2_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_generichash/blake2/ref/blake2b-ref.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_generichash/blake2/ref/generichash_blake2b.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hash/crypto_hash.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hash/sha256/hash_sha256_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hash/sha256/ref/hash_sha256.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hash/sha512/hash_sha512_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hash/sha512/ref/hash_sha512.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hashblocks/sha256/ref/blocks_sha256.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hashblocks/sha256/hashblocks_sha256_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hashblocks/sha512/ref/blocks_sha512.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_hashblocks/sha512/hashblocks_sha512_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/crypto_onetimeauth.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/poly1305/onetimeauth_poly1305.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/poly1305/onetimeauth_poly1305_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/poly1305/onetimeauth_poly1305_try.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/poly1305/53/auth_poly1305_53.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/poly1305/53/verify_poly1305_53.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/poly1305/donna/auth_poly1305_donna.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_onetimeauth/poly1305/donna/verify_poly1305_donna.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_scalarmult/crypto_scalarmult.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_scalarmult/curve25519/scalarmult_curve25519_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_secretbox/crypto_secretbox.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_secretbox/xsalsa20poly1305/secretbox_xsalsa20poly1305_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_secretbox/xsalsa20poly1305/ref/box_xsalsa20poly1305.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_shorthash/crypto_shorthash.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_shorthash/siphash24/shorthash_siphash24_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_shorthash/siphash24/ref/shorthash_siphash24.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/crypto_sign.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/sign_ed25519_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_0.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_1.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_add.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_cmov.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_copy.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_frombytes.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_invert.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_isnegative.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_isnonzero.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_mul.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_neg.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_pow22523.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_sq.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_sq2.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_sub.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/fe_tobytes.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_add.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_double_scalarmult.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_frombytes.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_madd.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_msub.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p1p1_to_p2.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p1p1_to_p3.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p2_0.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p2_dbl.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p3_0.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p3_dbl.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p3_to_cached.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p3_to_p2.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_p3_tobytes.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_precomp_0.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_scalarmult_base.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_sub.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/ge_tobytes.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/keypair.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/open.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/sc_muladd.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/sc_reduce.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/ed25519/ref10/sign.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/edwards25519sha512batch/sign_edwards25519sha512batch_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/edwards25519sha512batch/ref/fe25519_edwards25519sha512batch.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/edwards25519sha512batch/ref/ge25519_edwards25519sha512batch.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/edwards25519sha512batch/ref/sc25519_edwards25519sha512batch.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_sign/edwards25519sha512batch/ref/sign_edwards25519sha512batch.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/crypto_stream.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/portable/afternm_aes128ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/stream_aes128ctr_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/portable/beforenm_aes128ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/portable/common_aes128ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/portable/consts_aes128ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/portable/int128_aes128ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/portable/stream_aes128ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes128ctr/portable/xor_afternm_aes128ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes256estream/hongjun/aes256-ctr.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/aes256estream/stream_aes256estream_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa20/stream_salsa20_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa20/amd64_xmm6/stream_salsa20_amd64_xmm6.S',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa2012/stream_salsa2012_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa2012/ref/stream_salsa2012.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa2012/ref/xor_salsa2012.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa208/stream_salsa208_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa208/ref/stream_salsa208.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/salsa208/ref/xor_salsa208.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/xsalsa20/stream_xsalsa20_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/xsalsa20/ref/stream_xsalsa20.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_stream/xsalsa20/ref/xor_xsalsa20.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_verify/16/verify_16_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_verify/16/ref/verify_16.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_verify/32/verify_32_api.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_verify/32/ref/verify_32.c',
                    'libsodium-<(naclversion)/src/libsodium/randombytes/randombytes.c',
                    'libsodium-<(naclversion)/src/libsodium/randombytes/salsa20/randombytes_salsa20_random.c',
                    'libsodium-<(naclversion)/src/libsodium/randombytes/sysrandom/randombytes_sysrandom.c',
                    'libsodium-<(naclversion)/src/libsodium/sodium/compat.c',
                    'libsodium-<(naclversion)/src/libsodium/sodium/core.c',
                    'libsodium-<(naclversion)/src/libsodium/sodium/utils.c',
                    'libsodium-<(naclversion)/src/libsodium/sodium/version.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_scalarmult/curve25519/donna_c64/base_curve25519_donna_c64.c',
                    'libsodium-<(naclversion)/src/libsodium/crypto_scalarmult/curve25519/donna_c64/smult_curve25519_donna_c64.c'
            ]
        }
    ]
}