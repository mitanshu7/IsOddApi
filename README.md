# IsOddAPI
This API tell you whether a number is Odd. It uses [isevenapi.xyz](https://isevenapi.xyz/) in background and inverts the result.

## Requirements
1. [Python](https://www.python.org/)
2. [Docker](https://www.docker.com/) (Optional)

## Usage:

### Without Docker:

1. Clone the repository and enter it.
```bash
git clone https://github.com/mitanshu7/IsOddApi.git
cd IsOddApi/
```

2. Install the requirements.
```bash
pip3  install -r requirements.txt
```

3. Run the app.
```bash
python3 app.py
```

4. Navigate to `127.0.0.1:5010/api/isodd/<number>` to check where `<number>` is odd.

### With Docker:

1. Clone the repository and enter it.
```bash
git clone https://github.com/mitanshu7/IsOddApi.git
cd IsOddApi/
```

2. Build the docker container.
```bash
docker build --tag isoddapi .
```

3. Run the docker container.
```bash
docker run --name isoddapi -d -p 5010:5010 isoddapi
```

4. Navigate to `127.0.0.1:5010/api/isodd/<number>` to check where `<number>` is odd.

