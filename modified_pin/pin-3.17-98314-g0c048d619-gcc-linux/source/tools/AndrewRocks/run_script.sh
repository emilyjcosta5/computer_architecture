// set this first!!!
PIN_ROOT='/scratch/costa.em/computer_architecture/modified_pin/pin-3.17-98314-g0c048d619-gcc-linux'

// example
// first, run program
//python hello_world.py
// second, run using pin
//$PIN_ROOT/pin -t obj-intel64/pintool.so -- python hello_world.py > hello_world_trace.txt

python3 transitive_closure_of_a_graph.py 
$PIN_ROOT/pin -t obj-intel64/pintool.so -- python transitive_closure_of_a_graph.py 
