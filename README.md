# hunter-crud

A simple Hunter.io CRUD service.

## Deployment

Deployed on a Hetzner VPS (CX22) instance and accessible via:
**[https://hunter.rakan.com.tr](https://hunter.rakan.com.tr)**

## How to Run

```bash
git clone git@github.com:Rakanhf/hunter-crud.git
cd hunter-crud
cp .env.sample .env
# Edit the .env file with your configuration
docker compose up
```

## API Endpoints

Base URL: `https://hunter.rakan.com.tr/api/email-verifications/`

* **Create** (POST):

  ```
  POST /api/email-verifications/
  Body: { "email": "example@example.com" }
  ```

  Automatically fetches data from Hunter and stores it.

* **Retrieve** (GET):

  ```
  GET /api/email-verifications/{id}/
  ```

* **Delete** (DELETE):

  ```
  DELETE /api/email-verifications/{id}/
  ```

* **List** (GET):

  ```
  GET /api/email-verifications/
  ```

---

Built and maintained by [Rakan Farhouda](https://rakan.com.tr)
