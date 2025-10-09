# Fuzzing example

## Prerequisites

- Linux (preferably Arch Linux or an Arch Linux based distribution such as Manjaro) or MacOS

## Instructions using [juCi++](https://gitlab.com/cppit/jucipp)

1. Clone this repository
2. Run juCi++ with the following arguments from a terminal:
   - Linux: `CC=clang juci fuzzing-example`
   - MacOS: `CC=/opt/homebrew/opt/llvm/bin/clang juci fuzzing-example`
3. Open `tests/utility_fuzzer_test.c` and choose Compile and Run in the Project menu

## Instructions using a terminal on Linux

```sh
git clone https://gitlab.com/ntnu-tdat3020/fuzzing-example
mkdir fuzzing-example/build
cd fuzzing-example/build
CC=clang cmake ..
make
./tests/utility_fuzzer_test -max_total_time=60  # Cancel fuzzing after 60 seconds
```

## Instructions using a terminal on MacOS

```sh
git clone https://gitlab.com/ntnu-tdat3020/fuzzing-example
mkdir fuzzing-example/build
cd fuzzing-example/build
CC=/opt/homebrew/opt/llvm/bin/clang cmake ..
make
./tests/utility_fuzzer_test -max_total_time=60  # Cancel fuzzing after 60 seconds
```
