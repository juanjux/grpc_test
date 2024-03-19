# grpc_test

- Run the server: `python server.py`.
- On another shell or console, run the app: `gunicorn --log-level=debug  -w4 -b 127.0.0.1:5000 app:app`
- Do some requests: `curl http://127.0.0.1:5000`
