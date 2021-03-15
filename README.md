# Initial setup
>1. Clone this repository.  

>2. Create virtual environment.  
```bash
virtualenv <name> && source <name>/bin/activate
```

>3. Move to root directory.(There is manage.py)

>4. Install initial librares from requirements.txt.
```bash
pip install -r requirements.txt
```

>5. Create `.env` file in the root directory and set variables.
```bash
SECRET_KEY={*Generate secret own secret key}
DEBUG=True
```
>* [Generate the Secret Key](https://djecrety.ir/)