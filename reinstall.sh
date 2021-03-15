# conda activate nightly-work
pip uninstall -y anyscale ray
pip install anyscale
pip install https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-2.0.0.dev0-cp37-cp37m-macosx_10_13_intel.whl