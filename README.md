## Install

```bash
pip3 install -r requirements.txt
```

On raspberry pi 4, h5py must be installed with apt-get instead of pip. Remove any pip installations and install with `sudo apt-get python3-h5py`

RTIMULib must be installed from source:

```bash
git clone https://github.com/RPi-Distro/RTIMULib
cd ./RTIMULib/Linux/python/
python3 setup.py build
python3 setup.py install
```

### Configure AWS for boto3

- Configure AWS credentials for boto3 by running `aws configure`. You will be asked to input AWS Access Key ID, AWS Secret Access Key, Default region name (recommended: `eu-north-1`), Default output format (recommended: `text`)