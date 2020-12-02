// set this first!!!
PIN_ROOT='/scratch/costa.em/pin-3.17-98314-g0c048d619-gcc-linux'

// example
// first, run program
python hello_world.py
// second, run using pin
$PIN_ROOT/pin -t obj-intel64/pintool.so -- python hello_world.py
