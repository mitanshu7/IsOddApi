# Usage:
1. Clone the repository and enter it.
```bash
git clone https://github.com/mitanshu7/IsOddApi.git
cd IsOddApi/
```
2. Build the podman/docker container
```bash
podman build --tag isoddapi:0.1 .
```
or
```bash
docker build --tag isoddapi:0.1 .
```
3. Run the container.
```bash
podman run --name isoddapi -d -p 5010:5010 isoddapi:0.1
```
or
```bash
docker run --name isoddapi -d -p 5010:5010 isoddapi:0.1
```
