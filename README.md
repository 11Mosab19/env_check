# envcmp

A simple CLI tool to validate and compare `.env` files against an example/template file — with password strength checks and email format validation.

---

## Features

- **Key presence check** — detects missing or extra keys between your `.env` and `example.env`
- **Empty value detection** — flags any key that has no value assigned
- **Password security report** — analyzes sensitive keys (passwords, tokens, secrets) for strength issues
- **Email validation** — verifies that email-related keys contain a valid `@` format

---

## Installation

```bash
pip install envcmp
```

---

## Usage

```bash
envcmp --example example.env --env .env
```

### Arguments

| Argument    | Default       | Description                          |
|-------------|---------------|--------------------------------------|
| `--example` | `example.env` | Path to the template/example env file |
| `--env`     | `.env`        | Path to your actual env file         |

---

## Example Output

```
--------- check for keys ---------
Every key has a value

--------- if files matches ---------
The .env file matches the example file

--------- Password security report ---------
No security issues detected in DB_PASSWORD

--------- Email validation report ---------
The Email SMTP_EMAIL is valid
```

---

## Sensitive Keys Detected

The tool automatically detects keys related to:

- Passwords: `PASSWORD`, `PASS`, `PASSWD`, `PWD`, `DB_PASSWORD`, `MYSQL_PASSWORD` ...
- Secrets & tokens: `SECRET`, `SECRET_KEY`, `API_KEY`, `TOKEN`, `JWT_SECRET`, `ACCESS_KEY` ...
- Cloud credentials: `AWS_SECRET_ACCESS_KEY`, `CLIENT_SECRET`, `ENCRYPTION_KEY` ...

### Password strength rules

A password is considered strong if it has:
- At least **8 characters**
- At least one **uppercase** letter
- At least one **lowercase** letter
- At least one **special symbol** from: `& / \ ! - _ # @ $ %`

---

## Email Keys Detected

Keys like `EMAIL`, `SMTP_USER`, `MAIL_ADDRESS`, `NOREPLY_EMAIL`, `AUTH_EMAIL` and more are validated to ensure they contain a proper `@` sign.

---

## Requirements

- Python 3.7+
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [`rich`](https://pypi.org/project/rich/)

---

## License

MIT