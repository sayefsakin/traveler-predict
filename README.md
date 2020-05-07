Check here [https://github.com/hdc-arizona/traveler-integrated], the original Traveler repository for instruction on how to run Traveler.

#### Instruction to run traveler-predict

`./traveler-predict.py <metric> <bins> <begin> <end> <maximum_iterations> <lambda>`

A sample otf2 trace data can be found on `mamba` at the following location
```shell script
/data/otf2_traces/hpx/20191205_fibonacci.tar.gz
```

#### Sample commands for running
To bundle
```shell script
./bundle.py --otf2 data/fib23-n1-20191205/OTF2_archive/APEX.otf2 --label "FIB_23"
```

to serve
```shell script
./serve.py
```

Then
```shell script
./traveler-predict.py PAPI_TOT_CYC 1000 1242233747 1664725001 100 0.7
```

The final report is here at: `report.pdf`