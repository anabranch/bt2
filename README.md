# A minimalist demo

This demo is impressive for its quick setup.

It works with a fresh environment (note 3.7.7 is recommended for stability but im going with newer just for fun)

```
conda env create -f environment.yml
conda activate anyscaledev
```

basic.py has a couple of remote actors.
it demonstrates how ray tasks are related to each other.

tune_mnist.py -- for me, this did not work as written.  ray.init() starts on 'localhost' and does not accept connections from the hosts' actual IP.

50 iterations takes some time, this is fun stuff.
 
```
 2021-03-15 14:59:12,855 INFO tune.py:549 -- Total run time: 248.33 seconds (248.06 seconds for the tuning loop).
```

To run with anyscale.

.anyscale.yaml is key - set this to a scratch project if you have a sandbox (?)

TODO anyscale connect is not operational with the environment I've setup.

To run on from anyscale:

* `anyscale push` to get the project to the sandbox

Open Anyscale terminal
* become ray user `su - ray`
* `cd /home/ray/sandbox`
* `python tune_mnist.py` 

```
2021-03-15 23:04:49,970 INFO tune.py:549 -- Total run time: 85.55 seconds (85.27 seconds for the tuning loop).
```



