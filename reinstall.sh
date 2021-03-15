# conda activate nightly-work
pip uninstall -y anyscale ray
pip install anyscale
pip install https://s3-us-west-2.amazonaws.com/ray-wheels/master/2ba49c27016aea0e5bf22a673e316fad22e9cb36/ray-2.0.0.dev0-cp37-cp37m-macosx_10_13_intel.whl