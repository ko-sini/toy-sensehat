## Install dependencies

Install dependencies:

```bash
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

### Additional package installations on Raspberry Pi
- h5py must be installed with apt-get instead of pip. Remove any pip installations and run `sudo apt-get python3-h5py` to install h5py.
- RTIMULib is needed for SenseHat, and must be installed from source:
    ```bash
    git clone https://github.com/RPi-Distro/RTIMULib
    cd ./RTIMULib/Linux/python/
    python3 setup.py build
    python3 setup.py install
    ```

### Terraform and AWS CLI v2

Follow instructions in **s3/README.md** to get started with AWS CLI v2 and terraform. AWS CLI is needed for both boto3 and terraform.

### Configure AWS for boto3

- Configure AWS credentials for boto3 by running `aws configure`. 
    - You will be asked to input 
        - AWS Access Key ID, 
        - AWS Secret Access Key, 
        - Default region name: `eu-north-1`, 
        - Default output format: `text`.